import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def run():
    # Connect to the MCP server using Streamable HTTP
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")
            
            # Call bar chart tool
            bar_result = await session.call_tool(
                "create_bar_chart_tool",
                arguments={
                    "data": [
                        {"label": "A", "value": 10},
                        {"label": "B", "value": 20},
                        {"label": "C", "value": 30}
                    ],
                    "color": "set2"
                }
            )
            print(f"Bar Chart Result: {bar_result.structuredContent}")
            
            # Call pie chart tool
            pie_result = await session.call_tool(
                "create_pie_chart_tool",
                arguments={
                    "data": [
                        {"label": "A", "value": 10},
                        {"label": "B", "value": 20},
                        {"label": "C", "value": 30}
                    ],
                    "color": "set2"
                }
            )
            print(f"Pie Chart Result: {pie_result.structuredContent}")

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()