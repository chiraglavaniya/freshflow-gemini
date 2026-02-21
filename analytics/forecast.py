import numpy as np


def forecast_price(prices, steps: int = 7) -> list[float]:
    prices = np.asarray(prices, dtype=float)
    if prices.size == 0:
        return [0.0] * steps

    if prices.size == 1:
        return [float(prices[0])] * steps

    slope, intercept = np.polyfit(np.arange(prices.size), prices, 1)
    return [float(slope * (prices.size + i) + intercept) for i in range(steps)]
