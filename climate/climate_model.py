"""
Climate Module
Handles climate risk analysis and scoring using Linear Regression.
"""

import numpy as np
from sklearn.linear_model import LinearRegression


def train_climate_model():
    np.random.seed(13)
    n = 200
    temperature = np.random.uniform(10, 50, n).reshape(-1, 1)
    ccf = np.random.uniform(0.5, 3.0, n).reshape(-1, 1)
    X = np.hstack([temperature, ccf])
    noise = np.random.normal(0, 4, n)
    y = np.clip(100 - temperature.flatten() * 1.2 - ccf.flatten() * 10 + noise, 0, 100)
    model = LinearRegression()
    model.fit(X, y)
    return model


_climate_model = train_climate_model()


def predict_climate_score(temperature: float, climate_change_factor: float) -> float:
    raw = _climate_model.predict([[temperature, climate_change_factor]])[0]
    return float(np.clip(raw, 0, 100))


def get_climate_suggestions(score: float, temperature: float, ccf: float) -> list:
    tips = []
    if score >= 70:
        tips += [
            "🌍 Good climate resilience. Keep monitoring regional weather patterns.",
            "🌳 Plant native trees as windbreaks and carbon sinks.",
            "♻️ Maintain recycling and composting to reduce landfill emissions.",
        ]
    elif score >= 40:
        tips += [
            "🌤️ Moderate climate risk. Develop a local adaptation plan.",
            "💧 Build community rainwater tanks to buffer against dry spells.",
            "🏘️ Encourage green rooftops to reduce the urban heat-island effect.",
            "🌬️ Install wind monitors and subscribe to early-warning alert systems.",
        ]
    else:
        tips += [
            "🚨 High climate risk! Immediate mitigation strategies required.",
            "🛡️ Establish an emergency preparedness kit and evacuation plan.",
            "🌊 Map flood-prone areas and reinforce local drainage systems.",
            "☀️ Install reflective roofing to reduce indoor temperatures by 3–5°C.",
            "📡 Engage with district disaster-management authorities.",
        ]
    if ccf > 2.0:
        tips.append("⚠️ Very high CCF: advocate for renewable energy in your region.")
    if temperature > 38:
        tips.append("🌡️ Extreme heat: establish cooling centres and ensure hydration access.")
    return tips