from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime

from app.database.connection import Base


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String, unique=True, index=True, nullable=False)
    behavior_result = Column(Integer, nullable=False)
    behavior_confidence = Column(Float, nullable=False)
    object_detected = Column(Boolean, nullable=False)
    object_label = Column(String, nullable=True)
    object_confidence = Column(Float, nullable=True)
    risk_score = Column(Float, nullable=False)
    action = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
