backend/scoring.py
import numpy as np

def calculate_sharpe(returns):
    if len(returns) == 0:
        return 0
    mean_return = np.mean(returns)
    std_return = np.std(returns)
    if std_return == 0:
        return 0
    return mean_return / std_return


def max_drawdown(equity_curve):
    peak = equity_curve[0]
    max_dd = 0

    for value in equity_curve:
        if value > peak:
            peak = value
        drawdown = (peak - value) / peak
        max_dd = max(max_dd, drawdown)

    return max_dd


def credibility_score(trader_data):
    """
    trader_data = {
        "returns": list of trade returns,
        "equity_curve": list of portfolio values,
        "win_rate": float (0–1)
    }
    """

    sharpe = calculate_sharpe(trader_data["returns"])
    drawdown = max_drawdown(trader_data["equity_curve"])
    win_rate = trader_data["win_rate"]

    # Normalize values
    sharpe_score = min(sharpe * 20, 40)        # max 40
    drawdown_score = max(0, (1 - drawdown) * 30)  # max 30
    win_rate_score = win_rate * 30             # max 30

    total_score = sharpe_score + drawdown_score + win_rate_score

    return round(total_score, 2)


def classify_trader(score):
    if score >= 75:
        return "🟢 Skilled"
    elif score >= 50:
        return "🟡 Opportunistic"
    else:
        return "🔴 High Risk"
