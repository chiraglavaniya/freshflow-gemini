from backend.services.market_service import DashboardPayload
from gemini.gemini_client import generate_insight


def build_prompt(payload: DashboardPayload, context: str | None = None) -> str:
    prompt = (
        "You are an agriculture market analyst. "
        "Provide a concise strategy note for farmers and traders.\n"
        f"Average price: {payload.average_price}\n"
        f"Forecast price: {payload.forecast_price}\n"
        f"Volatility: {payload.volatility}\n"
        f"Trend: {payload.trend}\n"
        f"Anomaly count: {len(payload.anomaly_indices)}"
    )

    if context:
        prompt += f"\nAdditional context: {context}"

    return prompt


def generate_market_insight(payload: DashboardPayload, context: str | None = None) -> tuple[str, str]:
    prompt = build_prompt(payload, context)
    try:
        return generate_insight(prompt), "gemini"
    except Exception:
        fallback = (
            f"Trend is {payload.trend} with forecast around {payload.forecast_price}. "
            "Use staggered selling and monitor local mandi arrivals for sudden price shocks."
        )
        return fallback, "rule-based"
