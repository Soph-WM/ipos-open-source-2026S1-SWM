from hypothesis import given
from hypothesis import strategies as st

from app.models.gemini_models import (
    Content,
    FunctionCall,
    FunctionCallPart,
    GenerateContentRequest,
    GenerateContentResponse,
    Role,
    TextPart,
    is_function_call_part,
    is_text_part,
)


@given(st.text())
def test_text_part_property(t):
    """Property: TextPart should accept any string."""
    part = TextPart(text=t)
    assert part.text == t


def test_text_part_parsing():
    """Verify that TextPart is correctly identified and narrowed."""
    data = TextPart(text="Hello Gemini")
    content = Content(role=Role.USER, parts=[data])
    part = content.parts[0]

    assert isinstance(part, TextPart)
    assert part.text == "Hello Gemini"
    assert is_text_part(part) is True
