from datetime import datetime

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime


class MarketPoint(BaseModel):
    index: int
    modal_price: float


class AgentInsights(BaseModel):
    farmer: str
    trader: str
    analyst: str


class DashboardResponse(BaseModel):
    average_price: float
    forecast_price: float
    volatility: float
    trend: str
    anomaly_count: int
    series: list[MarketPoint]
    anomalies: list[MarketPoint]
    agents: AgentInsights


class InsightRequest(BaseModel):
    limit: int = Field(default=120, ge=20, le=500)
    commodity: str | None = None
    context: str | None = None


class InsightResponse(BaseModel):
    insight: str
    source: str
