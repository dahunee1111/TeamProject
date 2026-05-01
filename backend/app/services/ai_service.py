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
