from enum import StrEnum
from typing import Annotated, Any, TypeIs

from pydantic import BaseModel, ConfigDict, Field


class Role(StrEnum):
    USER = "user"
    MODEL = "model"


class FunctionCall(BaseModel):
    name: str
    args: dict[str, Any]


class FunctionResponse(BaseModel):
    name: str
    response: dict[str, Any]


class InlineData(BaseModel):
    mime_type: str
    data: str


class TextPart(BaseModel):
    text: str


class FunctionCallPart(BaseModel):
    function_call: FunctionCall = Field(..., alias="functionCall")


class FunctionResponsePart(BaseModel):
    function_response: FunctionResponse = Field(..., alias="functionResponse")


class InlineDataPart(BaseModel):
    inline_data: InlineData = Field(..., alias="inlineData")


# Python 3.14 Runtime Type Narrowing Helpers
def is_text_part(part: Part) -> TypeIs[TextPart]:
    return hasattr(part, "text")


def is_function_call_part(part: Part) -> TypeIs[FunctionCallPart]:
    return hasattr(part, "function_call")


def is_function_response_part(part: Part) -> TypeIs[FunctionResponsePart]:
    return hasattr(part, "function_response")


# Use Pydantic V2 Annotated Union with left-to-right matching,
# Since Gemini parts are mutually exclusive keys (can change in the future)
Part = Annotated[
    TextPart | FunctionCallPart | FunctionResponsePart | InlineDataPart,
    Field(union_mode="left_to_right"),
]


class Content(BaseModel):
    role: Role | str
    parts: list[Part]


# --- Tools and Configuration ---


class FunctionDeclaration(BaseModel):
    name: str
    description: str
    parameters: dict[str, Any]


class Tool(BaseModel):
    function_declarations: list[FunctionDeclaration] = Field(
        default_factory=list, alias="functionDeclarations"
    )


class FunctionCallingConfigMode(StrEnum):
    AUTO = "AUTO"
    ANY = "ANY"
    NONE = "NONE"


class FunctionCallingConfig(BaseModel):
    mode: FunctionCallingConfigMode = FunctionCallingConfigMode.AUTO
    allowed_function_names: list[str] | None = Field(None, alias="allowedFunctionNames")


class ToolConfig(BaseModel):
    function_calling_config: FunctionCallingConfig = Field(
        ..., alias="functionCallingConfig"
    )


# --- Request/Response Payloads ---


class GenerationConfig(BaseModel):
    candidate_count: int | None = Field(None, alias="candidateCount")
    stop_sequences: list[str] | None = Field(None, alias="stopSequences")
    max_output_tokens: int | None = Field(None, alias="maxOutputTokens")
    temperature: float | None = None
    top_p: float | None = None
    top_k: int | None = None


class GenerateContentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contents: list[Content]
    tools: list[Tool] | None = None
    tool_config: ToolConfig | None = Field(None, alias="toolConfig")
    generation_config: GenerationConfig | None = Field(None, alias="generationConfig")
    system_instruction: Content | None = Field(None, alias="systemInstruction")


class Candidate(BaseModel):
    content: Content
    finish_reason: str | None = Field(None, alias="finishReason")
    index: int | None = None
    # safety_ratings: list[dict] | None = Field(None, alias="safetyRatings")


class UsageMetadata(BaseModel):
    prompt_token_count: int = Field(..., alias="promptTokenCount")
    candidates_token_count: int = Field(..., alias="candidatesTokenCount")
    total_token_count: int = Field(..., alias="totalTokenCount")


class GenerateContentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    candidates: list[Candidate] = Field(default_factory=list)
    usage_metadata: UsageMetadata | None = Field(None, alias="usageMetadata")
