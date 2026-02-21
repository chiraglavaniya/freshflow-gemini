from dataclasses import dataclass
from typing import Optional

import numpy as np

from agents.analyst_agent import analyst_view
from agents.farmer_agent import farmer_view
from agents.trader_agent import trader_view
from analytics.anomaly import detect_anomaly
from analytics.forecast import forecast_price
from live_api.mandi_api import fetch_mandi_data


@dataclass
class DashboardPayload:
    average_price: float
    forecast_price: float
    volatility: float
    trend: str
    series: list[float]
    anomaly_indices: list[int]


def _classify_trend(series: np.ndarray) -> str:
    if len(series) < 2:
        return "Stable"

    slope, _ = np.polyfit(np.arange(len(series)), series, 1)
    if slope > 6:
        return "Uptrend"
    if slope < -6:
        return "Downtrend"
    return "Sideways"


def build_dashboard(limit: int, api_key: Optional[str], commodity: Optional[str] = None) -> DashboardPayload:
    frame = fetch_mandi_data(api_key=api_key, limit=limit, commodity=commodity)
    prices = frame["modal_price"].astype(float).to_numpy()

    average_price = float(np.mean(prices))
    projected = float(forecast_price(prices, steps=1)[0])
    std = float(np.std(prices))
    volatility = round(std / average_price, 4) if average_price else 0.0
    trend = _classify_trend(prices)

    anomalies = detect_anomaly(prices)
    anomaly_indices = [int(entry["index"]) for entry in anomalies]

    return DashboardPayload(
        average_price=round(average_price, 2),
        forecast_price=round(projected, 2),
        volatility=volatility,
        trend=trend,
        series=[float(v) for v in prices.tolist()],
        anomaly_indices=anomaly_indices,
    )


def build_agent_insights(payload: DashboardPayload) -> dict[str, str]:
    return {
        "farmer": farmer_view(payload.average_price, payload.forecast_price),
        "trader": trader_view(payload.volatility, len(payload.anomaly_indices)),
        "analyst": analyst_view(payload.trend, len(payload.anomaly_indices)),
    }
