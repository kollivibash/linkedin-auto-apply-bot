from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class JobApplication(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    job_title = Column(String)
    company = Column(String)
    status = Column(String)
    applied_at = Column(DateTime, default=datetime.utcnow)
