# Prototype 2.0

Event-driven quantitative trading research bot benchmarked against `SPY` buy-and-hold and Prototype 1.0's EMA 5/15 crossover logic.

## Stage 1 Setup (Windows PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
pre-commit install
