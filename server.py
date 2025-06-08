from fastmcp import FastMCP

mcp = FastMCP(name="MyMcpServer")

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http",
            host="0.0.0.0",
            port=8000)