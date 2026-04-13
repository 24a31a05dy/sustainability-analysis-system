def predict_score(energy, water, waste, carbon):
    # Simple weighted formula (acts like ML logic)
    
    score = 100 - (
        0.3 * energy +
        0.2 * water +
        0.2 * waste +
        0.3 * carbon
    )

    return max(0, round(score, 2))