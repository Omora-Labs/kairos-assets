import json
from typing import Dict

import polars as pl

from kairos_assets.data_gen.data import (
    get_asset_values,
    get_assets,
    get_currencies,
    get_currency_pairs,
)
from kairos_assets.ex_rates.main import get_exchange_rates


def get_data() -> Dict:
    asset_values = get_asset_values()
    currencies = get_currencies()
    currency_pairs = get_currency_pairs()
    assets = get_assets()
    exchange_rates = get_exchange_rates(asset_values, currency_pairs, currencies)

    return {
        "currencies": currencies,
        "currency_pairs": currency_pairs,
        "assets": assets,
        "asset_values": asset_values,
        "exchange_rates": exchange_rates,
    }


def data_to_dfs(data):
    df_currencies = pl.DataFrame(data["currencies"])
    df_currency_pairs = pl.DataFrame(data["currency_pairs"])
    df_assets = pl.DataFrame(data["assets"])
    df_asset_values = pl.DataFrame(data["asset_values"])
    df_exchange_rates = pl.DataFrame(data["exchange_rates"])

    return [
        df_currencies,
        df_currency_pairs,
        df_assets,
        df_asset_values,
        df_exchange_rates,
    ]


def generate_json(data: Dict) -> None:
    with open("src/kairos_assets/data_gen/data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("JSON generated")


def generate_data():
    data = get_data()
    generate_json(data)
    data_dfs = data_to_dfs(data)
    return data_dfs


if __name__ == "__main__":
    generate_data()
