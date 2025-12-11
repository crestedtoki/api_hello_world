from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_index() -> str:
    return """
    <html>
      <head>
        <title>FastAPI Hello</title>
      </head>
      <body>
        <h1>Welcome</h1>
        <p>Open the interactive API docs at http://URL/docs.</p>
      </body>
    </html>
    """


from datetime import datetime
@app.get("/current_time")
async def get_current_time() -> dict[str, str]:
    now = datetime.now()
    return {
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "Asia/Tokyo"
    }
