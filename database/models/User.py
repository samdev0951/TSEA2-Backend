import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.mysql import CHAR
from database.dborm import Base

class User(Base):
    __tablename__ = "users"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    
    email = Column(String(255), unique=True, nullable=False, index=True)
    google_id = Column(String(255), unique=True, nullable=False)

    points = Column(Integer, default=0)