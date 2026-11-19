# Prototype-2.0
The second ai trading robot built by Ilex Travis.

# 🤖 Prototype 2.0: Event-Driven & Copy-Trading AI Bot

**Prototype 2.0** is an autonomous, sentiment driven algorithmic trading bot engineered to rival **Prototype 1.0**. While traditional bots rely purely on technical indicators and price action, Prototype 2.0 trades on real-world catalysts combining macroeconomic news, geopolitical events, and "smart money" disclosures from top-performing traders and politicians.

---

## 🧠 Core Architecture

Prototype 2.0 operates on three main data pipelines that feed into a centralized decision engine:

1. **Macro & Political NLP Engine:** Scrapes breaking economic reports and geopolitical news to gauge market sentiment and identify impacted sectors.
2. **Smart Money & Congressional Tracker:** Monitors public financial disclosures (Form 4, Form 13F, and STOCK Act filings) to mirror high-conviction moves by top investors and politicians.
3. **Execution & Risk Engine:** Weighs conflicting signals, accounts for reporting lag, enforces stop-loss limits, and executes orders via broker APIs.

---

## 📡 Data Sources & Intel

* **Congressional & Insider Trades:** Capitol Trades, Quiver Quantitative API, SEC EDGAR (Forms 4 & 13F), WhaleWisdom.
* **Economic & Geopolitical News:** NewsAPI, Benzinga API, FRED (Federal Reserve Economic Data), GDELT Project.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Data & Scraping:** `pandas`, `requests`, `BeautifulSoup4`, `Playwright`
* **AI & Sentiment Analysis:** Hugging Face `FinBERT` (financial sentiment scoring) & LLM APIs (for structured impact analysis)
* **Brokerage Integration:** Alpaca API (Paper & Live execution)

---

## 🛡️ Built-In Safeguards

* **Reporting Lag Filter:** Verifies that the current asset price hasn't already priced in delayed disclosures (e.g., the 45-day congressional reporting window) before entering a position.
* **Multi-Source Verification:** Cross-references breaking political headlines across multiple reputable outlets to filter out market noise and rumors.
* **Dynamic Signal Weighting:** Resolves conflicts between bearish macro news and bullish insider activity using a weighted confidence score.

---

## 🚀 Roadmap

- [x] Define system architecture and data sources
- [ ] Build SEC & congressional trade scraper
- [ ] Integrate FinBERT sentiment pipeline for live news feeds
- [ ] Develop signal-weighting and risk management engine
- [ ] Deploy in paper-trading mode to benchmark against **Prototype 1.0**

---

## ⚠️ Disclaimer
*This project is for educational and research purposes only. Algorithmic trading 
