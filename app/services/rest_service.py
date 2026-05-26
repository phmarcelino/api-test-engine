import httpx
import json
import time
from sqlalchemy.orm import Session
from app.models.rest_request import RestRequest
from app.schemas.rest_request import RestRequestInput

def rest_request(data: RestRequestInput, db: Session) -> RestRequest:

    start_time = time.time()

    try:
        with httpx.Client(timeout=30) as client:
            response = client.request(
                method=data.method.upper(),
                url=data.url,
                headers=data.headers or {},
                json=data.body or None
            )

        response_time = time.time() - start_time

        db_request = RestRequest(
            method=data.method.upper(),
            url=data.url,
            header=json.dumps(data.headers) if data.headers else None,
            body=json.dumps(data.body) if data.body else None,
            status_code=response.status_code,
            response_body=response.text,
            response_header=json.dumps(dict(response.headers)),
            response_time=round(response_time, 4)
        )

    except httpx.RequestError as e:
        response_time = time.time() - start_time

        db_request = RestRequest(
            method=data.method.upper(),
            url=data.url,
            header=json.dumps(data.headers) if data.headers else None,
            body=json.dumps(data.body) if data.body else None,
            status_code=None,
            response_body=f"Request error:  {str(e)}",
            response_header=None,
            response_time=round(response_time, 4)
        )

    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    
    return db_request