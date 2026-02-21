from __future__ import annotations

import random

import numpy as np
import pandas as pd
import requests

MANDI_RESOURCE_URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"


def _synthetic_data(limit: int) -> pd.DataFrame:
    base = random.randint(1700, 2300)
    noise = np.random.randint(-220, 230, size=limit)
    trend = np.linspace(-80, 120, num=limit)
    series = np.maximum(200, base + noise + trend).astype(int)
    return pd.DataFrame({"modal_price": series})


def fetch_mandi_data(api_key: str | None, limit: int = 100, commodity: str | None = None) -> pd.DataFrame:
    if not api_key:
        return _synthetic_data(limit)

    params = {
        "api-key": api_key,
        "format": "json",
        "offset": 0,
        "limit": limit,
    }
    if commodity:
        params["filters[commodity]"] = commodity

    try:
        response = requests.get(MANDI_RESOURCE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json().get("records", [])

        frame = pd.DataFrame(data)
        if frame.empty or "modal_price" not in frame.columns:
            return _synthetic_data(limit)

        frame["modal_price"] = pd.to_numeric(frame["modal_price"], errors="coerce")
        frame = frame.dropna(subset=["modal_price"])
        if frame.empty:
            return _synthetic_data(limit)

        return frame[["modal_price"]].head(limit).reset_index(drop=True)
    except requests.RequestException:
        return _synthetic_data(limit)
