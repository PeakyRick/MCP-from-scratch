from pinecone import Pinecone
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()
################################################################
#### Pinecone Client Manager ####
################################################################
class PineconeClientManager:
    def __init__(self, api_key: str):
        self.pc_connet = Pinecone(api_key=api_key)
    
    def get_client(self):
        return self.pc_connet

client_manager = PineconeClientManager(api_key=os.getenv("PINECONE_API_KEY"))
def get_client_manager():
    return client_manager

################################################################
#### Pinecone Context Store ####
################################################################
# config
NAMESPACE = "Custom-0324"
INDEX_NAME = "rsgpt-mar"

class PineconeContextStore:
    def __init__(self, namespace: str, index_name: str):
        self.namespace = namespace
        self.index_name = index_name
        self.pc_connect = get_client_manager().get_client()
        self.index = self.pc_connect.Index(self.index_name)

    def search(self, query_vector: List[float], top_k: int):
        pc_outputs = self.pc_connect.Index(self.index_name).query(namespace=self.namespace,
                                                         vector=query_vector,
                                                         top_k=top_k,
                                                         include_metadata=True)
        
        return pc_outputs['matches']
    
context_store = PineconeContextStore(NAMESPACE, INDEX_NAME)
def get_context_store():
    return context_store

################################################################
#### Retriever ####
################################################################
def mock_embedder(query: str):
    return [0.1] * 1536

def format_context(context: List[dict]) -> str:
    result_ls = []
    for i, match in enumerate(context):
        content_str = f"Context Entry {i+1}:\n"
        content_str += f"Header: {match['metadata']['header']}\n"
        content_str += f"Content: {match['metadata']['text']}\n"
        result_ls.append(content_str)
    return "\n".join(result_ls)

from Embedder import get_embedder
embedder = get_embedder()

from langchain_core.tools import tool

@tool
def rswall_wiki_query_tool(query: str):
    """
    Query the RSWall Wiki
    """
    print(f"Querying RSWall Wiki with query: {query}")
    context_store = get_context_store()
    query_vector = embedder.embed_query(query)
    context = context_store.search(query_vector, 3)
    return format_context(context)

def mirror_rswall_wiki_query_tool(query: str):  # TODO: remove this after the decorated function is tested
    context_store = get_context_store()
    query_vector = embedder.embed_query(query)
    context = context_store.search(query_vector, 3)
    return format_context(context)