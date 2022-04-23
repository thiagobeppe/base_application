from fastapi import FastAPI

from routes.flight import flights_router

app = FastAPI(
    title="Base Flight Application" , openapi_url="/openapi.json"
)


@app.get("/", status_code=200)
def root() -> dict:
    """
    Home route of the API
    """
    return {"message": "Hello, World!"}


app.include_router(flights_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")