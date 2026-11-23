from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Project paths (resolves up to Prototype-2.0/)
BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
HISTORICAL_DATA_DIR = DATA_DIR / "historical"
LOGS_DIR = BASE_DIR / "logs"


class Settings(BaseSettings):
    # App settings
    app_env: str = "development"  # development | paper | live
    log_level: str = "INFO"

    # Stage 2: News, Sentiment & Political/Insider Data APIs
    news_api_key: str = ""
    finnhub_api_key: str = ""
    quiver_api_key: str = ""

    # Stage 5: Broker & Exchange Credentials
    alpaca_api_key: str = ""
    alpaca_secret_key: str = ""
    alpaca_base_url: str = "https://paper-api.alpaca.markets"

    oanda_api_key: str = ""
    oanda_account_id: str = ""

    crypto_api_key: str = ""
    crypto_secret_key: str = ""

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def is_live(self) -> bool:
        return self.app_env.lower() == "live"


settings = Settings()
