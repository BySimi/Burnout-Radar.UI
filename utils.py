# utils.py
import numpy as np
from datetime import datetime, timedelta

# -----------------------------
# Burnout score calculation
# -----------------------------
def calculate_burnout_score(sleep, screen_time, workload, mood):
    """
    Inputs:
    - sleep (hours)
    - screen_time (hours)
    - workload: 1=low, 2=medium, 3=high
    - mood: 1 (very low) → 5 (very good)

    Output:
    - burnout score (0–100)
    """

    # Normalize inputs
    sleep_factor = max(0, (7 - sleep) * 8)
    screen_factor = max(0, (screen_time - 5) * 6)
    workload_factor = workload * 10
    mood_factor = (5 - mood) * 8

    score = sleep_factor + screen_factor + workload_factor + mood_factor

    return int(min(100, max(0, score)))


# -----------------------------
# Burnout trend prediction
# -----------------------------
def predict_future_burnout(current_score, days=5):
    """
    Simple linear projection.
    Replace later with ML model.
    """
    trend = np.random.uniform(1, 3)  # mild upward drift
    return [
        min(100, int(current_score + trend * i))
        for i in range(1, days + 1)
    ]


# -----------------------------
# Human-readable interpretation
# -----------------------------
def interpret_burnout(score):
    if score < 30:
        return "Low risk — you're managing well."
    elif score < 60:
        return "Moderate risk — stay attentive to recovery."
    elif score < 80:
        return "High risk — early burnout signals detected."
    else:
        return "Critical — strong burnout likelihood."


# -----------------------------
# Recommendation logic
# -----------------------------
def generate_recommendation(sleep, screen_time, workload):
    if sleep < 6:
        return "Increase sleep duration tonight by at least 45 minutes."
    if screen_time > 8:
        return "Reduce screen exposure in the last hour before sleep."
    if workload == 3:
        return "Schedule one short break between study blocks today."
    return "Maintain your current routine and monitor recovery."


# -----------------------------
# Utility: date range
# -----------------------------
def last_n_days(n=7):
    today = datetime.today()
    return [today - timedelta(days=i) for i in range(n)][::-1]
