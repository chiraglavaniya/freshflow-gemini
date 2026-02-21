def trader_view(volatility: float, anomaly_count: int = 0) -> str:
    if volatility >= 0.25 or anomaly_count >= 3:
        return "High-risk tape. Prefer short holding windows with strict stop-loss levels."
    if volatility >= 0.15:
        return "Moderate volatility. Use scaled entries and keep position sizes controlled."
    return "Stable range. Swing positions and inventory rotation strategies are viable."
