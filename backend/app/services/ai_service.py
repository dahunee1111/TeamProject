<<<<<<< HEAD
import os
import warnings

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

warnings.filterwarnings(
    "ignore",
    message="SymbolDatabase.GetPrototype.*"
)

warnings.filterwarnings(
    "ignore",
    category=UserWarning
)
from pathlib import Path

import cv2
import joblib
import mediapipe as mp
import numpy as np
import torch
import torch.nn as nn

from app.services.object_detection_service import detect_objects


# =========================================================
# 경로 설정
# =========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "behavior" / "lstm_model.pth"
SCALER_PATH = BASE_DIR / "behavior" / "scaler.pkl"

SEQUENCE_LEN = 30


# =========================================================
# LSTM 모델 정의
# =========================================================

class LSTMClassifier(nn.Module):
    def __init__(self, input_size=99, hidden_size=128, num_layers=2):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.3
        )

        self.fc = nn.Sequential(
            nn.Linear(hidden_size, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :]).squeeze()


# =========================================================
# 디바이스 설정
# =========================================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# =========================================================
# 모델 로드
# =========================================================

model = LSTMClassifier().to(device)

model.load_state_dict(
    torch.load(MODEL_PATH, map_location=device)
)

model.eval()

print("✅ LSTM 모델 로드 완료")


# =========================================================
# scaler 로드
# =========================================================

scaler = joblib.load(SCALER_PATH)

print("✅ scaler 로드 완료")


# =========================================================
# MediaPipe Pose 초기화
# =========================================================

pose = mp.solutions.pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5
)

print("✅ MediaPipe Pose 초기화 완료")


# =========================================================
# 행동 분석 모델
# =========================================================

def run_behavior_model(video_path: str):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise Exception(f"영상 열기 실패: {video_path}")

    frame_buffer = []
    results_list = []

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        image_rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        result = pose.process(image_rgb)

        if result.pose_landmarks:

            landmarks = []

            for lm in result.pose_landmarks.landmark:
                landmarks.extend([
                    lm.x,
                    lm.y,
                    lm.z
                ])

            frame_buffer.append(landmarks)

            # 30프레임 단위 분석
            if len(frame_buffer) == SEQUENCE_LEN:

                seq = np.array(
                    frame_buffer,
                    dtype=np.float32
                )

                # 정규화
                seq = scaler.transform(seq)

                seq_tensor = (
                    torch.tensor(
                        seq,
                        dtype=torch.float32
                    )
                    .unsqueeze(0)
                    .to(device)
                )

                with torch.no_grad():

                    prob = model(seq_tensor).item()

                    pred = 1 if prob > 0.5 else 0

                    results_list.append(
                        (pred, prob)
                    )

                frame_buffer = []

    cap.release()

    # 관절 인식 실패
    if not results_list:
        return 0, 0.0

    abnormal_count = sum(
        1
        for pred, _ in results_list
        if pred == 1
    )

    total_sequences = len(results_list)

    abnormal_ratio = (
        abnormal_count / total_sequences
    )

    avg_confidence = float(
        np.mean([
            prob
            for _, prob in results_list
        ])
    )

    final_pred = (
        1 if abnormal_ratio >= 0.3 else 0
    )

    return final_pred, avg_confidence


# =========================================================
# 전체 AI 파이프라인
# =========================================================

def run_ai_pipeline(video_path: str):

    # 1. 행동 분석
    behavior_result, behavior_confidence = (
        run_behavior_model(video_path)
    )

    # 2. YOLO 위험물체 감지
    object_detected, object_label, object_confidence = (
        detect_objects(video_path)
    )

    return {
        "behavior_result": behavior_result,
        "behavior_confidence": round(
            behavior_confidence,
            4
        ),
        "object_detected": object_detected,
        "object_label": object_label,
        "object_confidence": object_confidence
    }
=======
import random


def run_ai_pipeline(file_path: str) -> dict:
    """
    현재는 실제 모델 대신 더미 AI 결과를 반환한다.
    나중에 이 함수 내부를 실제 Pose 모델 + 위험물품 탐지 모델로 교체하면 된다.
    """

    behavior_result = random.choice([0, 1])
    behavior_confidence = round(random.uniform(0.6, 0.95), 2)

    object_detected = random.choice([True, False])

    if object_detected:
        object_label = random.choice(["knife", "bat", "hammer"])
        object_confidence = round(random.uniform(0.7, 0.95), 2)
    else:
        object_label = None
        object_confidence = None

    return {
        "behavior_result": behavior_result,
        "behavior_confidence": behavior_confidence,
        "object_detected": object_detected,
        "object_label": object_label,
        "object_confidence": object_confidence
    }


def judge_action(
    behavior_result: int,
    behavior_confidence: float,
    object_detected: bool,
    object_label: str | None,
    object_confidence: float | None
) -> dict:
    """
    행동 분석 결과 + 위험물품 탐지 결과를 기반으로
    safe / signal / report 중 하나로 최종 판단한다.
    """

    risk_score = 0.0

    if behavior_result == 1:
        risk_score += behavior_confidence * 60

    if object_detected and object_confidence is not None:
        risk_score += object_confidence * 40

    dangerous_objects = {"knife", "gun", "bat", "hammer", "stick"}

    if object_label and object_label.lower() in dangerous_objects:
        risk_score += 10

    risk_score = min(round(risk_score, 2), 100)

    if risk_score < 30:
        action = "safe"
        action_label = "안전"
    elif risk_score < 85:
        action = "signal"
        action_label = "주의"
    else:
        action = "report"
        action_label = "신고"

    return {
        "risk_score": risk_score,
        "action": action,
        "action_label": action_label
    }
>>>>>>> 4e4caf4b230f5e7c87c7b89a2e3173b75c8bc5ef
