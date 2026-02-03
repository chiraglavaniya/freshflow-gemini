def trader_view(volatility):
    if volatility > 0.25:
        return "High volatility. Short-term trading recommended."
    return "Stable market. Long positions safer."
