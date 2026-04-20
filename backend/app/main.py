from fastapi import FastAPI
from app.routers import upload, analysis, history

app = FastAPI()

app.include_router(upload.router)
app.include_router(analysis.router)
app.include_router(history.router)

@app.get("/")
def root():
    return {"message": "Server is running"}
