# live_api/mandi_api.py

import pandas as pd
import numpy as np

def fetch_mandi_data(api_key: str, limit: int = 100):
    """
    Placeholder mandi data fetch.
    Replace this with your real API call later.
    """
    # Replace this logic with actual API call if needed
    return pd.DataFrame({
        "modal_price": np.random.randint(1000, 3000, size=limit)
    })
