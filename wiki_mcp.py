#! /Users/eric8/Desktop/Gakkel/MCP from Scratch/venv/Scripts/python.exe

from mcp.server.fastmcp import FastMCP
from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import SKLearnVectorStore
from Embedder import get_embedder
from Retriever import get_context_store, format_context

