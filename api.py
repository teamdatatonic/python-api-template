from fastapi import FastAPI


app = FastAPI(
    title="DT Python API Template",
    description="Example of a FastAPI application to use as a template for Rest API based projects on GCP",
    version="0.1.0",
    contact={"name": "Your Name", "email": "your.email@domain.com"}
)


@app.get("/api/healthz")
async def health_check():
    return {"api_healthy": True}
