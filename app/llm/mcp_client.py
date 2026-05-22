from __future__ import annotations

from typing import Any

import mcp.types


class MCPClient:
    """
    A stubbed client for the Model Context Protocol (MCP).

    In this example phase, tool execution is performed manually via curl
    to keep the orchestration logic simple and educational.
    """

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def call_tool(
        self,
        name: str,
        arguments: dict[str, Any],
    ) -> mcp.types.CallToolResult:
        """Stub: Logic for automated tool calls would go here."""
        raise NotImplementedError(
            "Manual tool execution required via curl for this example."
        )
