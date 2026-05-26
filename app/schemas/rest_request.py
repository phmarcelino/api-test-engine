from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class RestRequestInput(BaseModel):
    method: str
    url: str
    headers: Optional[Dict[str, str]] = None
    body: Optional[Dict[str, Any]] = None

class RestRequestOutput(BaseModel):
    id: int
    method: str
    url: str
    status_code: Optional[int]
    response_body: Optional[str]
    response_time: Optional[float]
    created_at: datetime

    class Config:
        form_attributes = True
        