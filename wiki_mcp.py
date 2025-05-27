#! /Users/eric8/Desktop/Gakkel/MCP from Scratch/venv/Scripts/python.exe
 
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import SKLearnVectorStore
from Embedder import get_embedder
from Retriever import get_context_store, format_context

mcp = FastMCP(
    name="RSWall-wiki-MCP-Server",
    instructions="When asked about Rocscience or related products such as RSWall, call `retrieve_from_RSWall_wiki` and pass in the user's query."
    )

@mcp.tool()
def retrieve_from_RSWall_wiki(query: str):
    """Retrieve information from the RSWall wiki which is saved in the context store."""
    embedder = get_embedder()
    context_store = get_context_store()

    query_vector = embedder.embed_query(query)
    context = context_store.search(query_vector, 10)
    formatted_context = format_context(context)
    return formatted_context

if __name__ == "__main__":
    import asyncio
    port = int(os.getenv("PORT", "8000"))
    # TODO: finish this, so it runs on Render
    asyncio.run(
        mcp.run_sse_async(
        host="0.0.0.0",
        port=port,
        log_level="debug"
        )
    )
