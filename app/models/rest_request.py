from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.database import Base

class RestRequest(Base):
    __tablename__ = "rest_requests"
    id = Column(Integer, primary_key=True, index=True)
    method = Column(String, nullable=False)
    url = Column(String, nullable=False)
    header = Column(Text, nullable=True)
    body = Column(Text, nullable=True)
    status_code = Column(Integer, nullable=True)
    response_body = Column(Text, nullable=True)
    response_header = Column(Text, nullable=True)
    response_time = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)