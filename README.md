# 🚨 AI CCTV Behavior & Danger Detection System

> AI 기반 실시간 CCTV 이상행동 및 위험물체 감지 시스템  
> FastAPI · YOLO · MediaPipe · LSTM · RAG · Docker · Render

---

# 🌐 Live Demo

## Web Service
https://ai-behavior-system.onrender.com/

---

# 📌 Project Overview

AI CCTV Behavior & Danger Detection System은  
실시간 CCTV 영상 및 업로드 영상을 분석하여:

- 이상행동 감지
- 위험물체 탐지
- 위험도 점수 계산
- 자동 대응 시스템 실행
- Discord 위험 알림
- RAG 기반 대응 가이드 제공

까지 수행하는 AI 기반 통합 관제 시스템입니다.

단순 영상 분석 프로젝트가 아니라,  
행동 분석 AI 모델과 위험물체 탐지 AI 모델을 결합하고,  
분석 결과를 관리자 시스템과 대응 흐름까지 연결한  
실제 서비스형 AI 관제 시스템 구조를 목표로 개발했습니다.

또한 Docker 기반 환경에서 GitHub + Render를 연동하여  
실제 배포 및 운영까지 진행했습니다.

---

# 🎯 Main Features

## 🧠 AI Behavior Analysis

- MediaPipe Pose 기반 관절 좌표 추출
- LSTM 기반 이상행동 감지
- 정상 / 위험 행동 분석
- 행동 기반 위험도 계산

---

## 🔥 Dangerous Object Detection

- YOLO 기반 위험물체 탐지
- 칼, 둔기 등 위험 요소 감지
- 객체 탐지 기반 위험도 반영

---

## 📹 CCTV Monitoring System

- 실시간 CCTV 웹캠 감지
- CCTV 등록 및 관리
- CCTV 위치 설정
- CCTV 선택 연동
- 실시간 위험 상황 분석

---

## 🚨 Risk Score System

- 행동 분석 결과 + 객체 탐지 결과 결합
- risk_score 기반 위험도 계산
- 위험 단계 자동 분류

---

## 🤖 Automated Response System

- 위험 단계별 대응 액션 결정
- Discord 위험 알림 전송
- 관리자 관제 화면 반영
- 위험 상황 기록 저장

---

## 📚 RAG Response Guide System

- 위험 상황별 대응 가이드 제공
- 상황 기반 대응 절차 출력
- 관리자 대응 지원 시스템

---

## 📊 Admin Dashboard

- 전체 사용자 조회
- 분석 로그 조회
- 위험 탐지 현황 확인
- 관리자 통계 그래프
- 위험도 분포 시각화
- 업로드 / 실시간 비율 통계
- 액션 유형 통계
- 위험물체 TOP 통계

---

# 🧠 AI Pipeline

```text
영상 입력
        ↓
행동 분석 (MediaPipe + LSTM)
        ↓
위험물체 탐지 (YOLO)
        ↓
위험도 계산 (risk_score)
        ↓
대응 액션 결정
        ↓
Discord 위험 알림
        ↓
RAG 대응 가이드 제공
        ↓
DB 저장
        ↓
관리자 대시보드 표시
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite

---

## AI / Deep Learning

- PyTorch
- MediaPipe Pose
- OpenCV
- YOLO
- NumPy
- LSTM

---

## Frontend

- HTML
- CSS
- JavaScript
- Chart.js

---

## Notification

- Discord Webhook

---

## Deployment

- Docker
- Render
- GitHub

---

# 🧩 System Architecture

```text
Frontend (Render)
        ↓
FastAPI Backend API
        ↓
AI Analysis Pipeline
        ↓
SQLite Database
        ↓
Admin Dashboard / Alert System
```

---

# 🌐 Deployment Architecture

```text
User Browser
        ↓
Render Web Service
        ↓
Docker Container
        ↓
FastAPI Backend
        ↓
AI Analysis System
        ↓
SQLite Database
```

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

# 1️⃣ Backend 실행

```bash
cd backend

(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned)

.\venv\Scripts\Activate.ps1

python -m uvicorn app.main:app --reload
```

---

## Backend Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# 2️⃣ Frontend 실행

```bash
python -m http.server 5500
```

---

## Frontend URL

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

# 🔥 Core Implementation Points

## 1. AI Behavior + Object Fusion

- 행동 분석 결과와 객체 탐지 결과를 결합
- 단일 모델이 아닌 복합 위험 판단 구조 구현
- 위험 상황에 대한 정확도 향상 목표

---

## 2. Risk Score Logic

- 행동 분석 결과
- 위험물체 탐지 결과
- 상황 정보

를 종합하여 위험도를 계산하는 구조 설계

---

## 3. Real-Time Monitoring Flow

- CCTV 입력
- AI 분석
- 위험 판단
- 대응 시스템
- 관리자 관제

까지 이어지는 전체 흐름 구현

---

## 4. Admin Dashboard Integration

- 분석 결과 저장
- 관리자 통계 시각화
- 위험 로그 관리
- 관리자 기반 관제 시스템 구성

---

## 5. Real Deployment Experience

- Docker 기반 배포 환경 구성
- GitHub + Render 연동
- 실제 서비스 배포 및 운영 경험
- 웹 기반 AI 관제 시스템 운영 구조 경험

---

# 📈 Future Plans

- 실제 CCTV 스트리밍 연동
- 다중 CCTV 동시 분석
- 위험도 AI 고도화
- 관리자 실시간 알림 시스템 강화
- 음성 경고 시스템 추가
- PostgreSQL 도입
- Redis 기반 실시간 처리 개선
- 클라우드 운영 환경 확장

---

# 👨‍💻 Team Project

AI 기반 실시간 위험 감지 및 대응 시스템을 목표로 한 팀 프로젝트입니다.

단순 영상 분석이 아니라:

- 행동 분석
- 위험물체 탐지
- 위험도 계산
- 대응 시스템
- 관리자 관제 기능
- 알림 시스템
- RAG 대응 가이드

까지 연결한 실제 서비스형 AI 관제 시스템 구조를 목표로 개발했습니다.

---

# 🧠 What We Learned

이 프로젝트를 통해:

- AI 모델 연결
- FastAPI 기반 API 설계
- 관리자 시스템 구성
- 실시간 데이터 흐름 처리
- 위험도 계산 구조 설계
- Docker 기반 배포 환경 구성
- Render 기반 서비스 운영

등 실제 서비스 개발 과정에서 필요한 구조를 경험할 수 있었습니다.

특히 AI 분석 결과를 단순 출력이 아니라  
관리자 화면, 알림 시스템, 대응 흐름까지 연결하는 과정에서  
서비스형 AI 시스템 구조에 대한 이해를 높일 수 있었습니다.

---

# 📄 License

This project is for educational and portfolio purposes.
