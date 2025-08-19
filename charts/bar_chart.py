# import altair as alt
# from  src.hook.main import ChartInput, save_chart
# import uuid

# def create_bar_chart(input_data: ChartInput) -> str:
#     """Create a bar chart and return image URL."""
#     chart_id = str(uuid.uuid4())
#     data_dicts = [d.model_dump() for d in input_data.data]
#     chart = alt.Chart(alt.Data(values=data_dicts)).mark_bar().encode(
#         x=alt.X("label:N", title="Label"),
#         y=alt.Y("value:Q", title="Value"),
#         color=alt.value(input_data.color)
#     ).properties(
#         width=400,
#         height=300
#     )
#     return save_chart(chart, chart_id)


import uuid
from pathlib import Path

import altair as alt
from hook.main import ChartInput

OUTPUT_DIR = Path("static/charts")
BASE_URL = "http://localhost:8000/static/charts"

def create_bar_chart(chart_input: ChartInput) -> str:
    """Create a bar chart and return its URL."""
    data = [{"label": item.label, "value": item.value} for item in chart_input.data]
    chart = alt.Chart(alt.Data(values=data)).mark_bar().encode(
        x="label:N",
        y="value:Q",
        color=alt.Color("label:N", scale=alt.Scale(scheme=chart_input.color))
    )
    chart_id = str(uuid.uuid4())
    output_path = OUTPUT_DIR / f"{chart_id}.png"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    chart.save(output_path, format="png")
    return f"{BASE_URL}/{chart_id}.png"