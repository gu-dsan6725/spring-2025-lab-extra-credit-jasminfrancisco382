"""
Google Search MCP Server

This server creates MCP tools to interact with Google search API
and  perform Google search queries.
"""

import requests
import os
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union
from dotenv import load_dotenv
from readability import Document
from bs4 import BeautifulSoup
from googlesearch import search
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("google_search")


@mcp.tool()
async def query_google_top_results(params: str) -> List[str]:
    """
    Execute a Google search query and return the top results.

    Args:
        params (str): The query  to search for.

    Returns:
        List[str]: A list of the top URLs return by the google search engine.
    """
    results = list(search(params))
    return results


@mcp.tool()
async def parse_google_html(params: str) -> str:
    """
    Retrieve  a web page from URl and return its content.

    Args:
        params (str): The URL of the web page.

    Returns:
        str: The clean and structured text extracted from content of the page.
    """

    response = requests.get(params, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    page_text = soup.get_text(separator="\n", strip=True)
    return page_text


def main():
    # Run the FastMCP server with SSE transport
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

