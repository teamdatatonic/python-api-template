from fastapi import FastAPI


app = FastAPI()


@app.get("/api/healthz")
def health_check():
    return {"api_healthy": True}
