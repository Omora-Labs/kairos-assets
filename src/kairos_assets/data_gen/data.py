import random
from typing import List

from faker import Faker

fake = Faker()


def get_currency_pairs() -> List:
    return [
        {"base_currency_id": 2, "quote_currency_id": 1},  # EUR/USD
        {"base_currency_id": 1, "quote_currency_id": 3},  # USD/JPY
        {"base_currency_id": 7, "quote_currency_id": 1},  # GBP/USD
        {"base_currency_id": 4, "quote_currency_id": 1},  # AUD/USD
        {"base_currency_id": 1, "quote_currency_id": 6},  # USD/CHF
        {"base_currency_id": 1, "quote_currency_id": 5},  # USD/CAD
    ]


def get_currencies() -> List:
    return [
        {"name": "USD"},
        {"name": "EUR"},
        {"name": "JPY"},
        {"name": "AUD"},
        {"name": "CAD"},
        {"name": "CHF"},
        {"name": "GBP"},
    ]


def get_assets() -> List:
    return [
        {"id": asset_id, "currency_id": random.choice([1, 2]), "name": fake.company()}
        for asset_id in range(1, 4)
    ]


def get_asset_values() -> List:
    return [
        {
            "asset_id": asset_id,
            "value": round(random.uniform(1000, 50000), 2),
            "date": fake.date_time_between(start_date="-1y").isoformat(),
        }
        for asset_id in range(1, 4)
        for _ in range(5)
    ]
