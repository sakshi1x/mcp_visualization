# Charts Visualization

This project provides a web-based service for generating and visualizing bar and pie charts from structured data using FastAPI and Altair. Charts are generated as PNG images and served via a REST API.

## Features
- Generate bar and pie charts from input data
- Save charts as PNG images in a static directory
- Access generated charts via unique URLs
- Extensible with new chart types

## Project Structure
```
charts_visualization/
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── src/
│   ├── server.py            # FastAPI server and MCP integration
│   ├── client.py            # Example client for interacting with the server
│   ├── charts/
│   │   ├── bar_chart.py     # Bar chart generation logic
│   │   ├── pie_chart.py     # Pie chart generation logic
│   │   └── __init__.py
│   └── model/
│       └── main.py          # Data models and shared logic
├── static/
│   └── charts/              # Generated chart images (PNG)
```

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd charts_visualization
   ```
2. **Create a virtual environment and install dependencies:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Running the Server
Start the FastAPI server (from the project root):
```bash
python src/server.py
```
Or with Uvicorn:
```bash
uvicorn src.server:app --host 0.0.0.0 --port 8000
uv run python server.py

```
for inspection : 

```
 uv run mcp dev server.py
```
## Usage
- Use the provided client (`src/client.py`) or send requests to the `/mcp` endpoint to generate charts.
- Generated charts are saved in `static/charts/` and accessible via URLs like `http://localhost:8000/static/charts/<chart_id>.png`.

## Requirements
- Python 3.9+
- FastAPI
- Uvicorn
- Altair
- (See `requirements.txt` for full list)

## Extending
To add new chart types, implement a new function in `src/charts/`, register it as an MCP tool in `src/server.py`, and update the client as needed.

## License
MIT License
