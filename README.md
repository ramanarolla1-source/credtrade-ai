# CredTrade AI — Proof of Skill for Traders

> Social trading leaderboard powered by AI credibility scoring using Pacifica APIs

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

1. Fetch trading data from Pacifica APIs  
2. Process key metrics (PnL, volatility, drawdowns)  
3. Apply scoring algorithm to compute credibility score  
4. Rank traders dynamically  
5. Display results via web dashboard
   Pacifica API → Backend → AI Scoring Engine → Frontend Dashboard
   
- **Backend**: FastAPI / Node.js  
- **AI Engine**: Python (pandas + statistical scoring)  
- **Frontend**: Next.js  

---

## 🧪 Demo

🎥 Demo Video: *[Add YouTube Link]*  
🌐 Live App: *[Optional]*  

---

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

---

# 🔥 What makes this strong

- Clear **problem → solution → demo flow**
- Uses **judge-friendly language**
- Shows **technical depth without overcomplicating**
- Aligns perfectly with your one-pager

---

# ⚠️ What you MUST update

Before submission, replace:

- `YOUR_USERNAME`
- YouTube link
- Google Docs one-pager link
- (Optional) Live demo link

---

# 👉 Next Step (high priority)

Now we move to:

👉 **“Starter code + folder structure”**  
or  
👉 **“AI scoring logic implementation”**

This is where your project becomes *real*.
   

---

## 🏗️ Architecture
