"""
Agriculture Module
Handles agricultural sustainability scoring using Linear Regression.
"""

import numpy as np
from sklearn.linear_model import LinearRegression


def train_agriculture_model():
    np.random.seed(7)
    n = 200
    rainfall = np.random.uniform(50, 300, n).reshape(-1, 1)
    temperature = np.random.uniform(10, 45, n).reshape(-1, 1)
    X = np.hstack([rainfall, temperature])
    noise = np.random.normal(0, 4, n)
    rain_score = -((rainfall.flatten() - 150) ** 2) / 150
    temp_score = -((temperature.flatten() - 25) ** 2) / 8
    y = np.clip(50 + rain_score + temp_score + noise, 0, 100)
    model = LinearRegression()
    model.fit(X, y)
    return model


_agri_model = train_agriculture_model()


def predict_agriculture_score(rainfall: float, temperature: float) -> float:
    raw = _agri_model.predict([[rainfall, temperature]])[0]
    return float(np.clip(raw, 0, 100))


def get_agriculture_suggestions(score: float, rainfall: float, temperature: float) -> list:
    tips = []
    if score >= 70:
        tips += [
            "🌾 Excellent conditions! Maintain current soil management practices.",
            "🐛 Introduce integrated pest management (IPM) to reduce chemicals.",
            "💧 Implement drip irrigation to improve water-use efficiency by 40–60%.",
        ]
    elif score >= 40:
        tips += [
            "🌱 Moderate sustainability. Consider crop rotation every 2–3 seasons.",
            "🧪 Conduct annual soil testing and supplement micronutrients.",
            "🌿 Intercrop with nitrogen-fixing legumes to enrich soil fertility.",
        ]
    else:
        tips += [
            "⚠️ Poor sustainability. Urgent soil and water management needed.",
            "🏗️ Build contour bunds and check dams to prevent erosion.",
            "🌱 Apply organic compost (5–10 tonnes/hectare) to restore soil.",
            "📋 Consult an agronomist for a customised crop calendar.",
        ]
    if rainfall < 80:
        tips.append("💦 Low rainfall: adopt rainwater harvesting and mulching.")
    elif rainfall > 250:
        tips.append("🌊 High rainfall: improve drainage and use flood-tolerant varieties.")
    if temperature > 35:
        tips.append("🌡️ Heat stress: use shade nets and irrigate in early morning.")
    elif temperature < 15:
        tips.append("❄️ Cool temps: use row covers and cold-hardy crop varieties.")
    return tips