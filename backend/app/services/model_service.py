def calculate_risk_and_action(
    behavior_result: int,
    behavior_confidence: float,
    object_detected: bool,
    object_label: str | None,
    object_confidence: float | None
) -> tuple[float, str]:
<<<<<<< HEAD

    """
    행동 분석 + 위험물체 감지 기반 위험도 계산
=======
    """
    행동 분석 결과와 위험물품 분석 결과를 기반으로
    위험도 점수(risk_score)와 대응 액션(action)을 계산한다.

    Parameters
    ----------
    behavior_result : int
        정상(0) / 이상(1)
    behavior_confidence : float
        행동 분석 신뢰도 (0.0 ~ 1.0)
    object_detected : bool
        위험물품 감지 여부
    object_label : str | None
        감지된 위험물품 이름
    object_confidence : float | None
        위험물품 감지 신뢰도 (0.0 ~ 1.0)

    Returns
    -------
    tuple[float, str]
        (risk_score, action)
>>>>>>> 4e4caf4b230f5e7c87c7b89a2e3173b75c8bc5ef
    """

    risk_score = 0.0

<<<<<<< HEAD
    # =====================================================
    # 1. 행동 이상 여부 반영
    # =====================================================

    if behavior_result == 1:
        risk_score += behavior_confidence * 60

    # =====================================================
    # 2. 위험물체 감지 반영
    # =====================================================

    if object_detected and object_confidence is not None:
        risk_score += object_confidence * 40

    # =====================================================
    # 3. 위험물체 종류별 가중치
    # =====================================================

    dangerous_object_weights = {

        # 칼
        "knife": 35,

        # 너클
        "knuckle duster": 30,

        # 망치
        "hammer": 25,

        # 공구류
        "tool": 15,

        # 야구방망이
        "bat": 20
    }

    if object_label is not None:

        label = object_label.lower()

        if label in dangerous_object_weights:

            risk_score += dangerous_object_weights[label]

    # =====================================================
    # 4. 최대 점수 제한
    # =====================================================

    risk_score = min(risk_score, 100.0)

    risk_score = round(risk_score, 2)

    # =====================================================
    # 5. 대응 액션 결정
    # =====================================================

    if risk_score < 30:

        action = "none"

    elif risk_score < 60:

        action = "alert"

    elif risk_score < 85:

        action = "broadcast"

    else:

        action = "report"

    return risk_score, action
=======
    # 1) 행동 이상 여부 반영
    if behavior_result == 1:
        risk_score += behavior_confidence * 60

    # 2) 위험물품 감지 여부 반영
    if object_detected and object_confidence is not None:
        risk_score += object_confidence * 40

    # 3) 특정 위험물품은 추가 가중치 부여
    dangerous_objects = {"knife", "gun", "bat", "hammer"}

    if object_label is not None and object_label.lower() in dangerous_objects:
        risk_score += 10

    # 최대 점수 제한
    risk_score = min(risk_score, 100.0)
    risk_score = round(risk_score, 2)

    # 4) 점수에 따라 액션 결정
    if risk_score < 30:
        action = "none"
    elif risk_score < 60:
        action = "alert"
    elif risk_score < 85:
        action = "broadcast"
    else:
        action = "report"

    return risk_score, action
>>>>>>> 4e4caf4b230f5e7c87c7b89a2e3173b75c8bc5ef
