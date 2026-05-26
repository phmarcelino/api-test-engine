from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.rest_request import RestRequestInput, RestRequestOutput
from app.services.rest_service import rest_request
from app.models.rest_request import RestRequest

router = APIRouter(prefix="/teste", tags=["Rest Tester"])

@router.post("/rest", response_model=RestRequestOutput)
def test_rest_api(request_data: RestRequestInput, db: Session = Depends(get_db)):
    return rest_request(data=request_data, db=db)

@router.get("/rest/history", response_model=list[RestRequestOutput])
def get_history(db: Session = Depends(get_db)):
    return db.query(RestRequest).order_by(RestRequest.id.desc()).limit(20).all()