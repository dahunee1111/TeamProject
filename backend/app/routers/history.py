from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.db_service import get_all_results, get_result_by_video_id

router = APIRouter(tags=["History"])


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    results = get_all_results(db)

    return {
        "status": "success",
        "count": len(results),
        "data": [
            {
                "video_id": result.video_id,
                "behavior_result": result.behavior_result,
                "behavior_confidence": result.behavior_confidence,
                "object_detected": result.object_detected,
                "object_label": result.object_label,
                "object_confidence": result.object_confidence,
                "risk_score": result.risk_score,
                "action": result.action,
                "created_at": result.created_at
            }
            for result in results
        ]
    }


@router.get("/result/{video_id}")
def get_result(video_id: str, db: Session = Depends(get_db)):
    result = get_result_by_video_id(db, video_id)

    if not result:
        raise HTTPException(status_code=404, detail="Result not found")

    return {
        "status": "success",
        "data": {
            "video_id": result.video_id,
            "behavior_result": result.behavior_result,
            "behavior_confidence": result.behavior_confidence,
            "object_detected": result.object_detected,
            "object_label": result.object_label,
            "object_confidence": result.object_confidence,
            "risk_score": result.risk_score,
            "action": result.action,
            "created_at": result.created_at
        }
    }
