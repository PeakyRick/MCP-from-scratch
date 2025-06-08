import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

URL = "3.14.254.6"

async def main():
    transport = StreamableHttpTransport(url=f"http://{URL}:8000/mcp")
    async with Client(transport=transport) as client:
        await client.ping()
        print("Server is running")

        tools = await client.list_tools()
        print(f"Available Tools: {tools}")

        greeting = await client.call_tool("greet", {"name": "Bean"})
        print(greeting)

if __name__ == "__main__":
    asyncio.run(main())