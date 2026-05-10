<<<<<<< HEAD
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import User
from app.routers.auth import get_current_user
from app.services.ai_service import run_ai_pipeline
from app.services.db_service import save_analysis_result
from app.services.model_service import calculate_risk_and_action
from app.services.response_action_service import execute_response_action
from app.services.rag_service import search_response_guide


router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

security = HTTPBearer(auto_error=False)


class AnalysisRequest(BaseModel):
    file_path: str


def extract_video_id(file_path: str) -> str:
    filename = Path(file_path).name

    if "_" in filename:
        return filename.split("_")[0]

    return filename


@router.post("/")
async def analyze_video(
    request: AnalysisRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        video_id = extract_video_id(request.file_path)

        ai_result = run_ai_pipeline(request.file_path)

        behavior_result = ai_result["behavior_result"]
        behavior_confidence = ai_result["behavior_confidence"]

        object_detected = ai_result["object_detected"]
        object_label = ai_result["object_label"]
        object_confidence = ai_result["object_confidence"]

        risk_score, action = calculate_risk_and_action(
            behavior_result=behavior_result,
            behavior_confidence=behavior_confidence,
            object_detected=object_detected,
            object_label=object_label,
            object_confidence=object_confidence
        )

        if risk_score < 30:
            status = "safe"
        elif risk_score < 60:
            status = "warning"
        else:
            status = "danger"

        saved_result = save_analysis_result(
            db=db,
            video_id=video_id,
            user_id=current_user.id,
            camera_name="UPLOAD",
            camera_location="영상 업로드 분석",
            behavior_result=behavior_result,
            behavior_confidence=behavior_confidence,
            object_detected=object_detected,
            object_label=object_label,
            object_confidence=object_confidence,
            risk_score=risk_score,
            action=action
        )

        action_result = execute_response_action(
            action=action,
            video_id=video_id,
            risk_score=risk_score
        )

        rag_guide = search_response_guide(
            object_label=object_label,
            behavior_result=behavior_result,
            action=action,
            risk_score=risk_score
        )

        return {
            "success": True,
            "video_id": saved_result.video_id,
            "user_id": saved_result.user_id,
            "behavior_result": (
                "abnormal"
                if behavior_result == 1
                else "normal"
            ),
            "behavior_confidence": behavior_confidence,
            "object_detected": object_detected,
            "object_label": object_label,
            "object_confidence": object_confidence,
            "risk_score": risk_score,
            "status": status,
            "action": action,
            "action_result": action_result,
            "created_at": saved_result.created_at,
            "camera_name": saved_result.camera_name,
            "camera_location": saved_result.camera_location,
            "rag_guide": rag_guide,
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"영상 분석 실패: {str(e)}"
        )
=======
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.model_service import calculate_risk_and_action
from app.services.db_service import save_analysis_result
from app.services.response_action_service import execute_response_action
from app.services.file_service import get_uploaded_file_path
from app.services.ai_service import run_ai_pipeline
from app.database.connection import get_db

router = APIRouter(tags=["Analysis"])


@router.post("/analyze/{video_id}")
def analyze_video(video_id: str, db: Session = Depends(get_db)):
    # 1. 업로드된 파일 확인
    file_path = get_uploaded_file_path(video_id)

    if not file_path:
        raise HTTPException(status_code=404, detail="Uploaded video not found")

    # 2. AI 파이프라인 실행
    ai_result = run_ai_pipeline(file_path)

    # 3. 결과 분리
    behavior_result = ai_result["behavior_result"]
    behavior_confidence = ai_result["behavior_confidence"]
    object_detected = ai_result["object_detected"]
    object_label = ai_result["object_label"]
    object_confidence = ai_result["object_confidence"]

    # 4. 위험도 계산
    risk_score, action = calculate_risk_and_action(
        behavior_result=behavior_result,
        behavior_confidence=behavior_confidence,
        object_detected=object_detected,
        object_label=object_label,
        object_confidence=object_confidence,
    )

    # 5. DB 저장
    saved_result = save_analysis_result(
        db=db,
        video_id=video_id,
        behavior_result=behavior_result,
        behavior_confidence=behavior_confidence,
        object_detected=object_detected,
        object_label=object_label,
        object_confidence=object_confidence,
        risk_score=risk_score,
        action=action
    )

    # 6. 대응 실행
    action_result = execute_response_action(
        action=saved_result.action,
        video_id=saved_result.video_id,
        risk_score=saved_result.risk_score
    )

    return {
        "video_id": saved_result.video_id,
        "file_path": file_path,
        "behavior_result": behavior_result,
        "behavior_confidence": behavior_confidence,
        "object_detected": object_detected,
        "object_label": object_label,
        "object_confidence": object_confidence,
        "risk_score": saved_result.risk_score,
        "action": saved_result.action,
        "action_result": action_result,
        "message": "AI analysis completed successfully"
    }
>>>>>>> 4e4caf4b230f5e7c87c7b89a2e3173b75c8bc5ef
