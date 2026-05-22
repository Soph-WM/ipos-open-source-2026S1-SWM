from __future__ import annotations

from typing import Any

import mcp.types

from app.models.gemini_models import (
    FunctionCall,
    FunctionResponse,
)

# this is the simplest possible implementation to support translation between
# MCP and Gemini models api, this must be refactored into a more robust solution
class MCPBridge:
    """A simple translator between MCP and Gemini models."""

    @staticmethod
    def gemini_call_to_mcp_args(gemini_call: FunctionCall) -> dict[str, Any]:
        """Extract arguments from a Gemini function call."""
        return gemini_call.args

    @staticmethod
    def mcp_result_to_gemini_response(
        call_name: str, mcp_result: mcp.types.CallToolResult
    ) -> FunctionResponse:
        """Translate an MCP result into a Gemini response."""
        # Simple translation for the manual example
        text_content = ""
        for item in mcp_result.content:
            if isinstance(item, mcp.types.TextContent):
                text_content += item.text

        return FunctionResponse(
            name=call_name,
            response={"result": text_content, "is_error": mcp_result.isError},
        )
