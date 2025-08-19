# import altair as alt
# from pydantic import BaseModel, Field
# from typing import List, Dict, Optional
# import os
# import uuid
# from pathlib import Path
# import base64
# from io import BytesIO

# # Configuration
# OUTPUT_DIR = Path("./static/charts")
# OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
# BASE_URL = "http://localhost:8000/static/charts"  # Adjust for your server

# # Pydantic models for input validation
# class ChartData(BaseModel):
#     label: str
#     value: float

# class ChartInput(BaseModel):
#     data: List[ChartData]
#     color: Optional[str] = Field(default="steelblue")

# def save_chart(chart: alt.Chart, chart_id: str) -> str:
#     """Save chart as PNG and return URL."""
#     output_path = OUTPUT_DIR / f"{chart_id}.png"
#     chart.save(output_path, format="png")
#     return f"{BASE_URL}/{chart_id}.png"



from pydantic import BaseModel, Field

class ChartData(BaseModel):
    label: str = Field(description="Label for the data point")
    value: float = Field(description="Value for the data point")

class ChartInput(BaseModel):
    data: list[ChartData] = Field(description="List of data points")
    color: str = Field(description="Color scheme for the chart")