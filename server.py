import uuid
from pathlib import Path
from typing_extensions import TypedDict

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from starlette.routing import Mount

from charts.bar_chart import create_bar_chart
from charts.pie_chart import create_pie_chart
from model.main import ChartData, ChartInput

# Define constants
OUTPUT_DIR = Path("static/charts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
BASE_URL = "http://localhost:8000/static/charts"

# FastAPI app to serve static files
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# MCP server
mcp = FastMCP(name="ChartVisualizationServer")

# Structured output models
class ChartResult(BaseModel):
    """Structured output for chart tools."""
    url: str = Field(description="URL of the generated chart")
    chart_type: str = Field(description="Type of chart (bar or pie)")

class ChartInputDict(TypedDict):
    """TypedDict for chart input."""
    data: list[dict[str, float | str]]
    color: str

# MCP tool for creating bar chart
@mcp.tool()
def create_bar_chart_tool(input_data: ChartInputDict) -> ChartResult:
    """Create a bar chart from the provided data."""
    # Convert input dict to ChartInput
    chart_data = [
        ChartData(label=str(item["label"]), value=float(item["value"]))
        for item in input_data["data"]
    ]
    chart_input = ChartInput(data=chart_data, color=input_data["color"])
    
    # Generate chart and save
    chart_url = create_bar_chart(chart_input)
    
    return ChartResult(url=chart_url, chart_type="bar")

# MCP tool for creating pie chart
@mcp.tool()
def create_pie_chart_tool(input_data: ChartInputDict) -> ChartResult:
    """Create a pie chart from the provided data."""
    # Convert input dict to ChartInput
    chart_data = [
        ChartData(label=str(item["label"]), value=float(item["value"]))
        for item in input_data["data"]
    ]
    chart_input = ChartInput(data=chart_data, color=input_data["color"])
    
    # Generate chart and save
    chart_url = create_pie_chart(chart_input)
    
    return ChartResult(url=chart_url, chart_type="pie")

# Mount MCP server to FastAPI app
app.mount("/mcp", mcp.streamable_http_app())

# Run both FastAPI and MCP server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)