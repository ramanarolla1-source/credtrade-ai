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

----

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
