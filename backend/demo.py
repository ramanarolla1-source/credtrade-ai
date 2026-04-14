Create:
backend/demo.py
from scoring import credibility_score, classify_trader

trader_a = {
    "returns": [0.1, -0.2, 0.3, -0.4, 0.5],
    "equity_curve": [100, 110, 90, 120, 80, 130],
    "win_rate": 0.5
}

trader_b = {
    "returns": [0.05, 0.04, 0.06, 0.05, 0.04],
    "equity_curve": [100, 105, 109, 115, 120, 125],
    "win_rate": 0.9
}

for name, trader in [("Trader A", trader_a), ("Trader B", trader_b)]:
    score = credibility_score(trader)
    category = classify_trader(score)

    print(f"{name}: Score = {score}, Category = {category}")
  ▶️ Run it
cd backend
python demo.py
