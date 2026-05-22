from typing import Any, Literal, TypeIs

from pydantic import BaseModel, Field


class JSONRPCBase(BaseModel):
    jsonrpc: Literal["2.0"] = "2.0"


class JSONRPCError(BaseModel):
    code: int
    message: str
    data: Any | None = None


class JSONRPCRequest(JSONRPCBase):
    id: int | str
    method: str
    params: dict[str, Any] | None = None


class JSONRPCNotification(JSONRPCBase):
    method: str
    params: dict[str, Any] | None = None


class JSONRPCResponse(JSONRPCBase):
    id: int | str
    result: Any | None = None
    error: JSONRPCError | None = None


# --- MCP Specific Structures ---


class Implementation(BaseModel):
    name: str
    version: str


class ServerCapabilities(BaseModel):
    tools: dict[str, Any] | list[str] | None = None
    resources: dict[str, Any] | list[str] | None = None
    prompts: dict[str, Any] | list[str] | None = None
    logging: dict[str, Any] | None = None


class InitializeResult(BaseModel):
    protocol_version: str = Field(..., alias="protocolVersion")
    capabilities: ServerCapabilities
    server_info: Implementation = Field(..., alias="serverInfo")
    instructions: str | None = None


class MCPTool(BaseModel):
    name: str
    description: str | None = None
    input_schema: dict[str, Any] = Field(..., alias="inputSchema")


class ToolsListResult(BaseModel):
    tools: list[MCPTool]
    next_cursor: str | None = Field(None, alias="nextCursor")


class MCPTextContent(BaseModel):
    type: Literal["text"] = "text"
    text: str


class MCPImageContent(BaseModel):
    type: Literal["image"] = "image"
    data: str
    mime_type: str = Field(..., alias="mimeType")


class MCPResourceContent(BaseModel):
    type: Literal["resource"] = "resource"
    uri: str
    mime_type: str | None = Field(None, alias="mimeType")
    text: str | None = None
    blob: str | None = None


type MCPContent = MCPTextContent | MCPImageContent | MCPResourceContent


class CallToolResult(BaseModel):
    content: list[MCPContent]
    is_error: bool = Field(False, alias="isError")


# --- Type Narrowing Helpers ---


def is_initialize_result(result: Any) -> TypeIs[InitializeResult]:
    return isinstance(result, dict) and "protocolVersion" in result


def is_tools_list_result(result: Any) -> TypeIs[ToolsListResult]:
    return isinstance(result, dict) and "tools" in result


def is_call_tool_result(result: Any) -> TypeIs[CallToolResult]:
    return isinstance(result, dict) and "content" in result
