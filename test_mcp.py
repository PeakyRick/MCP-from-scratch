#! /Users/eric8/Desktop/Gakkel/MCP from Scratch/venv/Scripts/python.exe

from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import SKLearnVectorStore
from Embedder import get_embedder
from Retriever import get_context_store, format_context

mcp = FastMCP("RSWall-wiki-MCP-Server")

@mcp.tool()
def RSWall_greetings_tool(name: str):
    """ Act as a helpful assistant, called RSWall that greets the user."""
    return f"Hello {name}! I am RSWall wiki MCP 69 69."

@mcp.tool()
def RSWall_goodbye_tool(name: str):
    """ Act as a helpful assistant, called RSWall that says goodbye to the user."""
    return f"Goodbye {name}! I am RSWall wiki MCP. See you next time!"

if __name__ == "__main__":
    mcp.run(transport="stdio")
