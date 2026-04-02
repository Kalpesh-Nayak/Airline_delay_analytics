import pandas as pd

def transform(df):
    df = df.dropna()

    df = df.rename(columns={
        "AIRLINE": "airline",
        "ORIGIN_AIRPORT": "origin",
        "DESTINATION_AIRPORT": "destination",
        "DEPARTURE_DELAY": "departure_delay",
        "ARRIVAL_DELAY": "arrival_delay"
    })

    return df