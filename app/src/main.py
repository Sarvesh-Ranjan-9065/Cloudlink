from fastapi import FastAPI
from routes import router

app = FastAPI(title="CloudLink API")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "CloudLink is running"}
