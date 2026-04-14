nano scoring.py
import numpy as np

def calculate_sharpe(returns):
    if len(returns) == 0:
        return 0
    mean = np.mean(returns)
    std = np.std(returns)
    if std == 0:
        return 0
    return mean / std


def max_drawdown(equity):
    peak = equity[0]
    max_dd = 0

    for value in equity:
        if value > peak:
            peak = value
        dd = (peak - value) / peak
        if dd > max_dd:
            max_dd = dd

    return max_dd


def credibility_score(data):
    sharpe = calculate_sharpe(data["returns"])
    drawdown = max_drawdown(data["equity_curve"])
    win_rate = data["win_rate"]

    sharpe_score = min(sharpe * 20, 40)
    drawdown_score = max(0, (1 - drawdown) * 30)
    win_score = win_rate * 30

    total = sharpe_score + drawdown_score + win_score
    return round(total, 2)


def classify_trader(score):
    if score >= 75:
        return "🟢 Skilled"
    elif score >= 50:
        return "🟡 Opportunistic"
    else:
        return "🔴 High Risk"       
 
