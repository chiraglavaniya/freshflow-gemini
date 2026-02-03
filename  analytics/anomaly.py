import numpy as np

def detect_anomaly(prices):
    mean = np.mean(prices)
    std = np.std(prices)
    return [p for p in prices if abs(p - mean) > 2 * std]
