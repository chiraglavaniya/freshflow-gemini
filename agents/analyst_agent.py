def analyst_view(trend: str, anomaly_count: int = 0) -> str:
    signal = f"Trend looks {trend.lower()}."
    if anomaly_count:
        signal += f" Detected {anomaly_count} outlier sessions; validate mandi-level supply shocks."
    else:
        signal += " No major outlier sessions detected in the current window."
    return signal
