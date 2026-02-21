import numpy as np


def detect_anomaly(prices, z_threshold: float = 2.0) -> list[dict[str, float | int]]:
    series = np.asarray(prices, dtype=float)
    if series.size < 3:
        return []

    mean = float(np.mean(series))
    std = float(np.std(series))
    if std == 0:
        return []

    anomalies = []
    for i, value in enumerate(series):
        z_score = abs((float(value) - mean) / std)
        if z_score > z_threshold:
            anomalies.append({"index": i, "value": float(value), "z_score": round(z_score, 2)})

    return anomalies
