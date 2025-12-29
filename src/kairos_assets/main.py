import subprocess

import duckdb
import polars as pl
from tabulate import tabulate

from kairos_assets.db.main import setup_db


def format_value(value):
    if value is None:
        return None
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    elif value >= 1_000:
        return f"{value / 1_000:.2f}K"
    else:
        return f"{value:.2f}"


def generate_porftolio_value(conn) -> None:
    print("\n=== Portfolio Totals ===")
    df = pl.read_database(
        "SELECT * FROM main.portfolio_total_all_currencies WHERE porfolio_total IS NOT NULL",
        connection=conn
    )

    df = df.with_columns(
        pl.col("porfolio_total")
        .map_elements(format_value, return_dtype=pl.Utf8)
        .alias("formatted_total")
    ).select(["month", "reporting_currency", "formatted_total"])

    print(tabulate(df.rows(), headers=df.columns, tablefmt="grid"))


def generate_monthly_assets(conn) -> None:
    print("\n=== Monthly Asset Values ===")
    df = pl.read_database(
        "SELECT * FROM main.monthly_asset_values_all_currencies WHERE value IS NOT NULL LIMIT 10",
        connection=conn
    )

    df = df.with_columns(
        pl.col("value")
        .map_elements(format_value, return_dtype=pl.Utf8)
        .alias("formatted_value")
    ).select(["month", "asset_name", "original_currency", "reporting_currency", "formatted_value"])

    print(tabulate(df.rows(), headers=df.columns, tablefmt="grid"))


def generate_assets_and_reports() -> None:
    try:
        print("Kairos Assets, a Omora Labs project")
        db = setup_db()  # set up assets and db
        db.conn.close()  # Close connection before dbt runs

        print("Preparing reports using DBT technology")
        subprocess.run(  # run dbt processes for reports preparation
            ["uv", "run", "dbt", "run"], cwd="kairos_assets_analytics", check=True
        )

        conn = duckdb.connect("assets.duckdb", read_only=True)

        generate_porftolio_value(conn)
        generate_monthly_assets(conn)

        conn.close()
    except Exception as e:
        print(f"Failure running process: {e}")


if __name__ == "__main__":
    generate_assets_and_reports()
