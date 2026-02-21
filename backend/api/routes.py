from datetime import datetime, timezone

from fastapi import APIRouter, Query

from backend.config import get_settings
from backend.schemas import (
    AgentInsights,
    DashboardResponse,
    HealthResponse,
    InsightRequest,
    InsightResponse,
    MarketPoint,
)
from backend.services.insight_service import generate_market_insight
from backend.services.market_service import build_agent_insights, build_dashboard

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", timestamp=datetime.now(timezone.utc))


@router.get("/dashboard", response_model=DashboardResponse)
def get_dashboard(
    limit: int = Query(default=120, ge=20, le=500),
    commodity: str | None = Query(default=None),
) -> DashboardResponse:
    settings = get_settings()
    payload = build_dashboard(limit=limit, api_key=settings.data_gov_api_key, commodity=commodity)
    agent_payload = build_agent_insights(payload)

    points = [MarketPoint(index=i + 1, modal_price=value) for i, value in enumerate(payload.series)]
    anomaly_points = [points[i] for i in payload.anomaly_indices if 0 <= i < len(points)]

    return DashboardResponse(
        average_price=payload.average_price,
        forecast_price=payload.forecast_price,
        volatility=payload.volatility,
        trend=payload.trend,
        anomaly_count=len(anomaly_points),
        series=points,
        anomalies=anomaly_points,
        agents=AgentInsights(**agent_payload),
    )


@router.post("/insight", response_model=InsightResponse)
def get_insight(payload: InsightRequest) -> InsightResponse:
    settings = get_settings()
    dashboard = build_dashboard(
        limit=payload.limit,
        api_key=settings.data_gov_api_key,
        commodity=payload.commodity,
    )
    insight, source = generate_market_insight(dashboard, payload.context)
    return InsightResponse(insight=insight, source=source)
