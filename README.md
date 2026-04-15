🎥 Demo Video: [YouTube Link]  
📄 One Pager: [Google Docs Link]  
🌐 Live App: [If available]
---
# 🚀 CredTrade AI Agent

### AI-Powered Social Trading Credibility Engine

CredTrade AI Agent is an AI-driven system that evaluates trader performance and ranks them based on **true skill vs luck**, using risk-adjusted metrics and behavioral consistency.

---

## 🧠 What This Agent Does

CredTrade AI Agent analyzes trader performance using:

- 📊 Risk-adjusted returns (Sharpe-like scoring)
- 📉 Maximum drawdown (risk exposure)
- 🎯 Win-rate consistency

It classifies traders into:

- 🟢 Skilled Traders  
- 🟡 Opportunistic Traders  
- 🔴 High-Risk / Lucky Traders  

---

## 🚨 Problem

Social trading platforms today reward **short-term gains**, not real skill.

This leads to:
- Misleading leaderboards
- Copy trading losses
- Inability to distinguish skilled vs lucky traders

---

## ✅ Solution

CredTrade AI Agent introduces a **Credibility Score** that evaluates traders based on:

- Consistency over time  
- Risk management  
- Sustainable performance  

---

## ⚙️ How It Works

1. Collect trader data (returns, equity curve, win rate)
2. Compute:
   - Sharpe-like score
   - Drawdown penalty
   - Consistency score
3. Generate a final **Credibility Score**
4. Classify trader into category

---

## 🏗️ Architecture

Pacifica APIs  
↓  
Backend Processing Layer  
↓  
AI Credibility Scoring Engine  
↓  
Database / Storage  
↓  
Leaderboard + Trader Profiles  

---
📈 Future Scope
🔗 Integration with Pacifica APIs
⛓️ On-chain trader data analysis
🤖 Autonomous trading agents
📊 Real-time leaderboard updates
🛣️ Roadmap
Q2 2026
MVP AI Credibility Engine
Basic leaderboard system
Q3 2026
Pacifica API integration
Real-time trader analytics
Advanced scoring models
🧩 Tech Stack
Python
FastAPI
NumPy
(Future: Pacifica APIs, Web3 data)

## 🎬 Demo

This project demonstrates how an AI agent evaluates trader credibility.

### Example:

| Trader | Score | Classification |
|-------|------|---------------|
| Trader A | 82 | 🟢 Skilled |
| Trader B | 54 | 🟡 Opportunistic |
| Trader C | 31 | 🔴 High Risk |

---

## 🧪 Sample Input

```json
{
  "returns": [0.05, 0.04, 0.06],
  "equity_curve": [100, 105, 110],
  "win_rate": 0.75
}

