from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy import Enum as SqlEnum
from app.enum.reocrd_type import RecordType


class Record(Base):
    table_name = "records"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    created_by = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(SqlEnum(RecordType), nullable=False, index=True)
    category = Column(String, nullable=False, index=True)
    date = Column(DateTime, nullable=False, index=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)