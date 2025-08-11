import fastapi
import os

app = fastapi.FastAPI()


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
