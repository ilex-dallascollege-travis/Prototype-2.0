from dataclasses import dataclass, field


@dataclass(frozen=True)
class RiskConfig:
    max_risk_per_trade: float = 0.01       # 1% of account equity per trade
    max_daily_loss: float = 0.03           # 3% daily circuit breaker
    max_open_positions: int = 5
    default_stop_loss_pct: float = 0.02    # 2% stop loss
    default_take_profit_pct: float = 0.04  # 4% take profit


@dataclass(frozen=True)
class SignalConfig:
    min_confidence_score: float = 0.65     # Minimum score to trigger a trade
    sentiment_weight: float = 0.30
    technical_weight: float = 0.40
    insider_political_weight: float = 0.30


@dataclass(frozen=True)
class TradingConfig:
    paper_trading: bool = True
    default_timeframe: str = "1d"
    stock_watchlist: list[str] = field(
        default_factory=lambda: ["SPY", "QQQ", "AAPL", "MSFT", "NVDA"]
    )
    crypto_watchlist: list[str] = field(
        default_factory=lambda: ["BTC/USD", "ETH/USD"]
    )
    forex_watchlist: list[str] = field(
        default_factory=lambda: ["EUR_USD", "GBP_USD"]
    )
    risk: RiskConfig = field(default_factory=RiskConfig)
    signals: SignalConfig = field(default_factory=SignalConfig)


trading_config = TradingConfig()
