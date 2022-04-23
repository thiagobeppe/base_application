from requests import Session

import deps
from database.models.flights import Flight as F_model
from database.schemas.flights import Flight as F_schema

from fastapi import Depends, FastAPI, APIRouter
from typing import Optional,List

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

@api_router.get("/flights", status_code=200, response_model=List[F_schema])
def get_all_flights(
        *,
        db: Session = Depends(deps.get_db)
    ):
    flights = db.query(F_model).all()
    return flights

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")