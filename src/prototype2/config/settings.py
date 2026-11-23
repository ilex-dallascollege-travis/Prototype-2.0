"""
Prototype 2.0 - Central Configuration System

Controls application settings, supported markets, API credentials, and execution permissions.
"""

import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

# ----------------------------------------------------------------------------------------------------
# PROJECT DIRECTORY
# ----------------------------------------------------------------------------------------------------

PROJECT_ROOT + Path(__file__).resolve().parents[3]

DATA_DIR = PROJECT_ROOT / "data"
LOG_DIR = PROJECT_ROOT / "logs"

DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR =.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------------------------------
# ENVIRONMENT VARIABLES
# --------------------------------------------------------------------------------------------------

load_dotenv(PROJECT_ROOT / ".env")

def get_bool(name: str, default: bool = False) -> bool:
    """Safely convert environment variables to booleans."""

    value = os.getenv(name)

    if value is NOne:
        return default
    
    return value.strip().lower() in ("true", "1", "yes", "on")

def get_list(name: str, default: tuple) -> tuple:
    """Read comma-seperated environment variables."""

    value = os.getenv(name)

    if not value:
        return default
    
    return tuple(
        item.strip().lower()
        for item in value.split(",")
        if item.strip()
    )

    # ------------------------------------------------------------------------------------------
    # APPLICATION SETTINGS
    # --------------------------------------------------------------------------------------------

    @dataclass(frozen=True)
    class Settings:

        APP_NAME: str = "Prototype 2.0"

        VERSION: str = "2.0.0"

        ENVIRONMENT: str = os.getenv(
            "ENVIRONMENT", "development"
        )

        DEBUG: bool = get_bool("DEBUG", True)

        LOG_LEVEL: str = os.getenv(
            "LOG_LEVEL", "INFO"
        ).upper()

# ------------------------------------------------------------------------------------------
# SUPPORTED FINANCIAL MARKETS
# ------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class MarketSettings:

    SUPPORTED_MARKETS: tuple = get_list(
        "SUPPORTED_MARKETS",
        ("stocks", "forex", "commodities", "crypto")
    )

# -------------------------------------------------------------------------------------------
# INTELLIGENCE CONFIGURATION
# -----------------------------------------------------------------------------------------

@dataclass(frozen=True)
class IntelligenceSettings:

    NEWS_ENABLED: bool = True

    SENTIMENT_ANALYSIS_ENABLED: bool = True

    HISTORICAL_ANALYSIS_ENABLED: bool = True

    GEOPOLITICAL_TRACKING_ENABLED: bool = True

    INSIDER_TRACKING_ENABLED: bool = True

    CONGRESSIONAL_TRACKING_ENABLED: bool = True

    INSTITUTIONAL_TRACKING_ENABLED: bool = True


# --------------------------------------------------
# API CREDENTIALS
# --------------------------------------------------

@dataclass(frozen=True)
class APISettings:

    NEWS_API_KEY: str = os.getenv("NEWS_API_KEY", "")

    FRED_API_KEY: str = os.getenv("FRED_API_KEY", "")

    ALPACA_API_KEY: str = os.getenv(
        "ALPACA_API_KEY", ""
    )

    ALPACA_SECRET_KEY: str = os.getenv(
        "ALPACA_SECRET_KEY", ""
    )

    ALPACA_BASE_URL: str = os.getenv(
        "ALPACA_BASE_URL",
        "https://paper-api.alpaca.markets"
    )


# --------------------------------------------------
# EXECUTION CONFIGURATION
# --------------------------------------------------

@dataclass(frozen=True)
class ExecutionSettings:

    TRADING_ENABLED: bool = False

    EXECUTION_MODE: str = "research"

    PAPER_TRADING_ENABLED: bool = False

    LIVE_TRADING_ENABLED: bool = False


# --------------------------------------------------
# GLOBAL SETTINGS
# --------------------------------------------------

@dataclass(frozen=True)
class ApplicationSettings:

    APP: Settings = Settings()

    MARKETS: MarketSettings = MarketSettings()

    INTELLIGENCE: IntelligenceSettings = (
        IntelligenceSettings()
    )

    API: APISettings = APISettings()

    EXECUTION: ExecutionSettings = ExecutionSettings()


# --------------------------------------------------
# INITIALIZE CONFIGURATION
# --------------------------------------------------

settings = ApplicationSettings()


# --------------------------------------------------
# CONFIGURATION VALIDATION
# --------------------------------------------------

def validate_settings() -> bool:

    valid_markets = {
        "stocks",
        "forex",
        "commodities",
        "crypto"
    }

    selected_markets = set(
        settings.MARKETS.SUPPORTED_MARKETS
    )

    if not selected_markets:
        raise ValueError(
            "At least one market must be configured."
        )

    invalid_markets = selected_markets - valid_markets

    if invalid_markets:
        raise ValueError(
            f"Unsupported markets: {invalid_markets}"
        )

    if settings.EXECUTION.TRADING_ENABLED:
        raise ValueError(
            "Automated trading is disabled during development."
        )

    return True


if __name__ == "__main__":

    validate_settings()

    print("=" * 45)
    print("PROTOTYPE 2.0 CONFIGURATION")
    print("=" * 45)

    print(f"Application: {settings.APP.APP_NAME}")
    print(f"Version: {settings.APP.VERSION}")

    print(
        f"Environment: {settings.APP.ENVIRONMENT}"
    )

    print(
        f"Supported Markets: "
        f"{settings.MARKETS.SUPPORTED_MARKETS}"
    )

    print(
        f"Execution Mode: "
        f"{settings.EXECUTION.EXECUTION_MODE}"
    )

    print(
        f"Automated Trading: "
        f"{settings.EXECUTION.TRADING_ENABLED}"
    )

    print("=" * 45)
    print("CONFIGURATION VALIDATED SUCCESSFULLY")
    
