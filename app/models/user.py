from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class DB_Table(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    register = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    status = Column(Boolean, default=True)