from fastapi import FastAPI


app = FastAPI()


@app.get("/api/healthz")
async def health_check():
    return {"api_healthy": True}
