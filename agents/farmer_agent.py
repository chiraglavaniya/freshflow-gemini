def farmer_view(avg_price: float, forecast_price: float | None = None) -> str:
    if forecast_price is not None and forecast_price > avg_price * 1.04:
        return "Likely upside. Hold inventory in batches and sell on stronger sessions."
    if avg_price >= 3000:
        return "Current levels are favorable. Consider staggered selling for risk control."
    return "Prices are moderate. Focus on storage quality and avoid panic selling."
