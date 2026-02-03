# live_api/mandi_api.py

def fetch_mandi_data(api_key, limit=100):
    import pandas as pd
    import numpy as np

    return pd.DataFrame({
        "modal_price": np.random.randint(1000, 3000, size=limit)
    })
