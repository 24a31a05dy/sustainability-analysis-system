def predict_sustainability(energy, water, waste):
    # Simple intelligent formula (acts like ML logic)
    carbon = (energy * 1.5) + (water * 2.0) + (waste * 2.5)

    if carbon < 250:
        status = "Green 🌱"
        advice = "Good! Maintain current usage."
    elif carbon < 350:
        status = "Moderate ⚠️"
        advice = "Reduce energy and water consumption."
    else:
        status = "Critical 🔴"
        advice = "Immediate action needed! Optimize all resources."

    return {
        "predicted_carbon": round(carbon, 2),
        "status": status,
        "advice": advice
    }

<h2>{{ score }}/100</h2>

<!-- ✅ ADD THIS BELOW -->
<div style="width: 80%; background: gray; margin: auto; border-radius:10px;">
    <div style="width: {{ score }}%; background: green; color: white; padding: 10px; border-radius:10px;">
        {{ score }}%
    </div>
</div>