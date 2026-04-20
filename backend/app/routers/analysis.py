from fastapi import APIRouter

router = APIRouter(tags=["Analysis"])

@router.post("/analyze/{video_id}")
def analyze_video(video_id: str):
    return {
        "video_id": video_id,
        "status": "success",
        "result": "analysis placeholder"
    }
