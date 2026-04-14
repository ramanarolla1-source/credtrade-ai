# CredTrade AI — Proof of Skill for Traders

> Social trading leaderboard powered by AI credibility scoring using Pacifica APIs
## 🚀 Live Demo

🎥 Demo Video: [YouTube Link]  
📄 One Pager: [Google Docs Link]  
🌐 Live App: [If available]
---

## 🚀 Overview

CredTrade AI is a social trading analytics platform that distinguishes **skilled traders from lucky ones** using AI-powered credibility scoring.

Unlike traditional leaderboards that rank traders purely based on profits, CredTrade AI evaluates **risk-adjusted performance, consistency, and trading behavior** to provide a more reliable measure of trader skill.

---
## 🏗️ Architecture

**Data Layer**
- Pacifica APIs  

↓  

**Backend Layer**
- FastAPI / Node.js  
- Data Processing (PnL, Drawdown, Metrics)  

↓  

**AI Layer**
- Credibility Scoring Engine  

↓  

**Application Layer**
- Database  
- Frontend (Next.js)  

↓  

**User Interface**
- Leaderboard  
- Trader Profiles  


## 🎯 Problem

Current social trading platforms:
- Reward short-term profits over long-term consistency  
- Promote high-risk trading behavior  
- Mislead users into following unreliable traders  

There is no standardized way to evaluate **true trading skill vs randomness**.

---

## 💡 Solution

CredTrade AI introduces an **AI-driven credibility layer** on top of Pacifica trading data.

It:
- Analyzes on-chain trading activity  
- Computes risk-aware performance metrics  
- Ranks traders based on credibility, not just PnL  

---

## 🧠 Key Features

- **AI Credibility Score**  
  Evaluates traders using Sharpe ratio, drawdowns, and consistency  

- **Risk-Adjusted Leaderboard**  
  Highlights sustainable performers instead of high-risk winners  

- **Trader Classification**  
  - 🟢 Skilled  
  - 🟡 Opportunistic  
  - 🔴 High-Risk  

- **Trader Profiles**  
  Detailed insights into performance and behavior  

- **Pacifica Integration**  
  Uses real trading data via Pacifica APIs  

---

## ⚙️ How It Works

1. Pacifica APIs provide real-time trading data  
2. Backend processes:
   - PnL
   - Drawdowns
   - Trade frequency  
3. AI scoring engine computes credibility score  
4. Traders are classified into:
   - Skilled
   - Opportunistic
   - High-Risk  
5. Frontend displays leaderboard and insights

   Proof of Work
   ## 📊 Sample Output

Example Credibility Score:

Trader A  
- Return: +120%  
- Max Drawdown: -60%  
- Score: 38/100 → High Risk  

Trader B  
- Return: +45%  
- Max Drawdown: -10%  
- Score: 82/100 → Skilled
- ## 🧠 Scoring Logic (Current Implementation)

The current MVP uses a rule-based scoring system:

- Sharpe Ratio → 40%
- Max Drawdown → 30%
- Consistency → 20%
- Volatility → 10%

This will evolve into ML-based scoring in future versions.
## 🎬 Demo Flow

1. Open leaderboard  
2. View ranked traders  
3. Select a trader  
4. View credibility breakdown  
5. Understand risk vs return behavior
   backend/
frontend/
docs/
data/
## 🔗 Why Pacifica

CredTrade AI leverages Pacifica’s trading infrastructure to:
- Access real trading data  
- Build analytics on top of perps markets  
- Enable composable DeFi intelligence tools  

----
## 📊 Example Credibility Insight

Trader A:
- High returns but large drawdowns → ⚠️ High-Risk  
- Credibility Score: 42/100  

Trader B:
- Moderate returns + consistent performance → ✅ Skilled  
- Credibility Score: 82/100  

## 📄 One Pager

📄 View One Pager: *[Add Google Docs Link]*  

---

## 🛠️ Tech Stack

- Pacifica APIs  
- Python (pandas, numpy)  
- FastAPI / Node.js  
- Next.js  
- Optional: LLM for explanation layer  

---

## ▶️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/credtrade-ai.git
cd credtrade-ai
2. Setup environment
cp .env.example .env
3. Install dependencies
# backend
cd backend
pip install -r requirements.txt

# frontend
cd ../frontend
npm install
4. Run the application
# backend
uvicorn main:app --reload

# frontend
npm run dev
📊 Credibility Scoring Logic (Simplified)

The credibility score is computed using:

Risk-adjusted return (Sharpe Ratio)
Maximum drawdown
Trade consistency
Volatility exposure

Score = Weighted combination of these metrics
🛣️ Roadmap
Q2 2026
MVP with scoring engine
Pacifica API integration
Leaderboard + profiles
Q3 2026
AI explanations
Social features (follow, watchlist)
UI/UX improvements
Q4 2026
On-chain reputation system
Copy trading
DAO governance
🌍 Impact
Enables safer trading decisions
Promotes responsible trading behavior
Builds trust in decentralized finance ecosystems
🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests.

📜 License

MIT License

🙌 Acknowledgements

Built for the Pacifica Hackathon.

----
## 🏗️ Architecture

Pacifica API → Backend (FastAPI) → AI Scoring Engine → Frontend (Next.js)
Why This Matters
## 🌍 Why This Matters

CredTrade AI reduces risk in social trading by helping users identify truly skilled traders instead of following short-term winners driven by luck.

This builds trust and transparency in decentralized finance.
Hackathon Scope Clarification
## 🧪 Hackathon Scope

This project demonstrates:
- Credibility scoring engine (core innovation)
- Leaderboard UI
- Pacifica data integration (or simulated data if applicable)

Future versions will expand into real-time execution and copy trading.


