nano main.py
from fastapi import FastAPI
from pydantic import BaseModel
from scoring import credibility_score, classify_trader

app = FastAPI()


class TraderData(BaseModel):
    returns: list
    equity_curve: list
    win_rate: float


@app.get("/")
def root():
    return {"message": "CredTrade AI API is running"}


@app.post("/score")
def score_trader(data: TraderData):
    trader = {
        "returns": data.returns,
        "equity_curve": data.equity_curve,
        "win_rate": data.win_rate
    }

    score = credibility_score(trader)
    category = classify_trader(score)

    return {
        "credibility_score": score,
        "classification": category
    }
python3 -m uvicorn main:app --reload
