# 🚨 AI CCTV Behavior & Danger Detection System

> AI 기반 실시간 CCTV 이상행동 및 위험물체 감지 시스템  
> FastAPI + YOLO + MediaPipe + LSTM + RAG 기반 통합 관제 프로젝트

---

# 📌 Project Overview

이 프로젝트는 CCTV 영상 및 업로드 영상을 분석하여:

- 이상행동 감지
- 위험물체 탐지
- 위험도 점수 계산
- 자동 대응 시스템 실행
- RAG 기반 대응 가이드 제공

까지 수행하는 AI 기반 통합 관제 시스템입니다.

실시간 CCTV 환경을 가정하여 제작되었으며,  
행동 분석과 위험물체 탐지를 결합하여  
보다 정확한 위험 상황 판단을 목표로 합니다.

---

# 🎯 Main Features

- MediaPipe Pose 기반 행동 분석
- LSTM 기반 이상행동 감지
- YOLO 기반 위험물체 탐지
- 실시간 CCTV 웹캠 감지
- 위험도 점수 계산 시스템
- 자동 대응 액션 시스템
- RAG 기반 대응 가이드
- Discord 위험 알림 시스템
- 관리자 대시보드
- 관리자 통계 그래프
- CCTV 등록 및 관리 시스템
- CCTV 선택 연동
- 분석 기록 저장 및 조회

---

# 🧠 AI Pipeline

```text
영상 입력
→ 행동 분석 (LSTM)
→ 위험물체 탐지 (YOLO)
→ 위험도 계산
→ 대응 액션 결정
→ Discord 알림
→ RAG 대응 가이드 제공
→ DB 저장
→ 관리자 대시보드 표시
```

---

# 🛠 Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### AI / Deep Learning
- PyTorch
- MediaPipe Pose
- OpenCV
- YOLO
- NumPy

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Notification
- Discord Webhook

---

# 📂 Project Structure

```text
backend/
 ┣ app/
 ┃ ┣ routers/
 ┃ ┣ services/
 ┃ ┣ database/
 ┃ ┣ rag_data/
 ┃ ┗ main.py
 ┣ behavior/
 ┣ uploads/
 ┣ realtime_frames/
 ┗ requirements.txt

frontend/
 ┣ index.html
 ┣ login.html
 ┣ signup.html
 ┣ admin.html
 ┣ cctv_settings.html
 ┗ mypage.html
```

---

# 🚀 Run Project

## 1️⃣ Backend 실행

```bash
cd backend

(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned)

.\venv\Scripts\Activate.ps1

python -m uvicorn app.main:app --reload
```

### Backend Docs

```text
http://127.0.0.1:8000/docs
```

---

## 2️⃣ Frontend 실행

```bash
python -m http.server 5500
```

### Frontend

```text
http://127.0.0.1:5500/frontend/index.html
```

---

# 📊 Admin Features

- 전체 사용자 조회
- 전체 분석 로그 조회
- 위험 탐지 현황 확인
- 관리자 통계 그래프
- 위험도 분포 그래프
- 업로드 / 실시간 비율 그래프
- 액션 유형 통계
- 위험물체 TOP 통계

---

# 📸 CCTV Features

- CCTV 등록
- CCTV 위치 설정
- 활성 / 비활성 관리
- 실시간 CCTV 선택
- CCTV 기반 위험 기록 저장
- CCTV 기반 위험 알림

---

# 🔥 RAG Response System

위험 상황 발생 시:

- 대응 절차 제공
- 위험 상황별 가이드 출력
- 관리자 대응 지원

예시:

- 칼 감지 대응
- 둔기 감지 대응
- 폭행 상황 대응
- 쓰러짐 감지 대응

---

# 🔔 Discord Alert System

위험 상황 발생 시:

- Discord Webhook 자동 전송
- 실시간 위험 알림 제공
- CCTV 정보 포함 알림 전송
- 위험 시간 및 위치 기록

---

# 📜 History System

- 업로드 영상 기록 저장
- 실시간 CCTV 기록 저장
- 행동 분석 결과 저장
- 위험물체 탐지 결과 저장
- 위험도 점수 기록
- 대응 액션 기록

---

# 📌 Future Plans

- 실제 CCTV 스트리밍 연동
- 다중 CCTV 동시 분석
- 위험도 AI 고도화
- 관리자 실시간 알림 시스템 강화
- 음성 경고 시스템 추가
- 클라우드 배포 및 운영 환경 구축

---

# 👨‍💻 Team Project

AI 기반 실시간 위험 감지 및 대응 시스템을 목표로 한 팀 프로젝트입니다.

단순 영상 분석이 아닌:

- 행동 분석
- 위험물체 탐지
- 대응 시스템
- 관리자 관제 기능

까지 통합한 실제 관제 시스템 형태로 개발 중입니다.

---

# 📄 License

This project is for educational and portfolio purposes.
