# kairos-assets

Synthetic financial data generator with analytics built on DuckDB and dbt.

## Overview

Kairos Assets generates synthetic financial data including assets, valuations, currencies, and exchange rates. Includes dbt models for portfolio analytics with multi-currency reporting.

## Features

- **Synthetic data generation** - Creates realistic financial data using Faker
- **Multi-currency support** - Generates assets in different currencies with exchange rates
- **Time-series data** - Historical asset valuations and exchange rates
- **dbt Analytics** - Pre-built models for portfolio reporting and currency conversion
- **Local & Cloud** - Works with local DuckDB or MotherDuck cloud storage
- **Transaction safety** - Automatic rollback on data generation failures

## Database Schema

### Raw Tables (staging)

- `currencies` - Currency definitions (USD, EUR, JPY, etc.)
- `assets` - Asset records with currency references
- `asset_values` - Time-series asset valuations
- `currency_pairs` - Available currency conversion pairs
- `exchange_rates` - Historical exchange rates

### dbt Models (marts)

- `monthly_asset_values` - Latest asset values per month
- `monthly_asset_totals` - Aggregated totals by currency
- `monthly_exchange_rates` - Latest exchange rates per month
- `monthly_asset_values_all_currencies` - Asset values in all reporting currencies
- `monthly_asset_totals_all_currencies` - Totals converted to all currencies
- `portfolio_total_all_currencies` - Complete portfolio value by currency

## Setup

### Prerequisites

- Python 3.13+
- uv package manager

### Installation

```bash
uv sync
```

### Configuration

For local development, no configuration needed. Database will be created as `assets.duckdb`.

### Generate Data and Reports

```bash
uv run src/kairos_assets/main.py
```

This will:
1. Create local DuckDB database
2. Set up all tables with proper relationships
3. Generate synthetic financial data
4. Run dbt models to create analytics views
5. Display portfolio reports

## Project Structure

```
kairos-assets/
├── src/kairos_assets/        # Python data generation
│   ├── data_gen/              # Synthetic data generators
│   ├── db/                    # Database setup and insert
│   └── main.py               # Main orchestration
├── kairos_assets_analytics/   # dbt project
│   ├── models/
│   │   ├── staging/          # Clean raw data
│   │   └── marts/            # Business logic
│   └── profiles.yml          # dbt connection config
└── assets.duckdb             # Local database file
```

## License

[MIT](https://opensource.org/licenses/MIT)
