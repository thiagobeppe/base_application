from app.database.schemas import Flight

from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Base Flight Application" , openapi_url="/openapi.json"
)

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Home route of the API
    """
    return {"message": "Hello, World!"}


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")