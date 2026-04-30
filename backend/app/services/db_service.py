from sqlalchemy.orm import Session

from app.database.models import AnalysisResult


def save_analysis_result(
    db: Session,
    video_id: str,
    behavior_result: int,
    behavior_confidence: float,
    object_detected: bool,
    object_label: str | None,
    object_confidence: float | None,
    risk_score: float,
    action: str
):
    existing = db.query(AnalysisResult).filter(AnalysisResult.video_id == video_id).first()

    if existing:
        existing.behavior_result = behavior_result
        existing.behavior_confidence = behavior_confidence
        existing.object_detected = object_detected
        existing.object_label = object_label
        existing.object_confidence = object_confidence
        existing.risk_score = risk_score
        existing.action = action
        db.commit()
        db.refresh(existing)
        return existing

    new_result = AnalysisResult(
        video_id=video_id,
        behavior_result=behavior_result,
        behavior_confidence=behavior_confidence,
        object_detected=object_detected,
        object_label=object_label,
        object_confidence=object_confidence,
        risk_score=risk_score,
        action=action
    )

    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result


def get_result_by_video_id(db: Session, video_id: str):
    return db.query(AnalysisResult).filter(AnalysisResult.video_id == video_id).first()


def get_all_results(db: Session):
    return db.query(AnalysisResult).order_by(AnalysisResult.created_at.desc()).all()
