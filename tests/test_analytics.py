import numpy as np

from analytics.anomaly import detect_anomaly
from analytics.forecast import forecast_price


def test_forecast_returns_requested_steps():
    values = np.array([100, 110, 120, 130])
    result = forecast_price(values, steps=3)
    assert len(result) == 3
    assert result[0] > values[-1]


def test_anomaly_detection_finds_outlier():
    values = np.array([100, 102, 101, 99, 320])
    result = detect_anomaly(values, z_threshold=1.9)
    assert result
    assert result[-1]["value"] == 320
