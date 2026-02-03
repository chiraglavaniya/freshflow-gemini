import numpy as np

def forecast_price(prices, steps=7):
    trend = np.polyfit(range(len(prices)), prices, 1)
    future = [trend[0] * (len(prices) + i) + trend[1] for i in range(steps)]
    return future
