import os
import sys
sys.path.append(os.getcwd())

from Retriever import mirror_rswall_wiki_query_tool

query = "What is RSWall? Does it have gabion wall options?"

print(mirror_rswall_wiki_query_tool(query))