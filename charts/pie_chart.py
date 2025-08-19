# import altair as alt
# from src.hook.main import ChartInput, save_chart
# import uuid

# def create_pie_chart(input_data: ChartInput) -> str:
#     """Create a pie chart and return image URL."""
#     chart_id = str(uuid.uuid4())
#     data_dicts = [d.model_dump() for d in input_data.data]
#     valid_schemes = [
#         'accent', 'category10', 'category20', 'category20b', 'category20c', 'dark2',
#         'paired', 'pastel1', 'pastel2', 'set1', 'set2', 'set3', 'tableau10', 'tableau20'
#     ]
#     scheme = input_data.color if input_data.color in valid_schemes else 'set2'
#     chart = alt.Chart(alt.Data(values=data_dicts)).mark_arc().encode(
#         theta=alt.Theta("value:Q", stack=True),
#         color=alt.Color("label:N", scale=alt.Scale(scheme=scheme)),
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

def create_pie_chart(chart_input: ChartInput) -> str:
    """Create a pie chart and return its URL."""
    data = [{"label": item.label, "value": item.value} for item in chart_input.data]
    chart = alt.Chart(alt.Data(values=data)).mark_arc().encode(
        theta="value:Q",
        color=alt.Color("label:N", scale=alt.Scale(scheme=chart_input.color))
    )
    chart_id = str(uuid.uuid4())
    output_path = OUTPUT_DIR / f"{chart_id}.png"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    chart.save(output_path, format="png")
    return f"{BASE_URL}/{chart_id}.png"