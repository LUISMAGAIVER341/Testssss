import fastapi
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou lista de domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get():
    try:
        with open("app/db.json", "rb") as f:
            content = f.read()
    except FileNotFoundError:
        content = b"{}"
    return fastapi.Response(content=content, media_type="application/json")


@app.put("/")
async def overwrite_file(req: fastapi.Request):
    data = await req.body()
    os.makedirs("app", exist_ok=True)
    with open("app/db.json", "wb") as f:
        f.write(data)
    return fastapi.Response("ok", status_code=200)
