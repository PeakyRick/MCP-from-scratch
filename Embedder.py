from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Embedder:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    def embed_query(self, query: str):
        """
        Embed a single query string using OpenAI's text-embedding-3-small model.
        
        Args:
            query (str): The text to embed
            
        Returns:
            list: The embedding vector
        """
        return self.embeddings.embed_query(query)

# Create a singleton instance
embedder = Embedder()

def get_embedder():
    return embedder


