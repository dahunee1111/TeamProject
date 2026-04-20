from fastapi import APIRouter

router = APIRouter(tags=["History"])

@router.get("/history")
def get_history():
    return {
        "status": "success",
        "data": []
    }
