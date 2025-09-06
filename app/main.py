from fastapi import FastAPI, HTTPException
from app.models import Transaction, SavingsGoal, TransferRequest, APIResponse, AIInsight
from app.momo_client import MoMoClient
from app.ai_engine import AIEngine
from typing import List
import os

app = FastAPI(title="SmartSave API", description="AI-powered savings with MoMo integration")

momo_client = MoMoClient()
ai_engine = AIEngine()

@app.get("/")
async def root():
    return {"message": "Welcome to SmartSave API"}

@app.get("/transactions/{user_id}", response_model=List[Transaction])
async def get_transactions(user_id: str, start_date: str = None, end_date: str = None):
    """
    Fetch user transactions from MoMo API.
    """
    try:
        data = momo_client.fetch_transactions(user_id, start_date, end_date)
        transactions = [Transaction(**t) for t in data.get('transactions', [])]
        return transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/savings-goal", response_model=APIResponse)
async def set_savings_goal(goal: SavingsGoal):
    """
    Create a savings goal for the user.
    """
    try:
        result = momo_client.create_savings_goal(goal.user_id, goal.target_amount, goal.deadline.isoformat() if goal.deadline else None)
        return APIResponse(success=True, message="Savings goal created successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/transfer", response_model=APIResponse)
async def transfer_to_savings(request: TransferRequest):
    """
    Transfer money to the user's savings wallet.
    """
    try:
        result = momo_client.transfer_to_savings(request.user_id, request.amount)
        return APIResponse(success=True, message="Transfer initiated successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/insights/{user_id}", response_model=AIInsight)
async def get_insights(user_id: str):
    """
    Get AI-generated financial insights for the user.
    """
    try:
        # Fetch transactions
        transactions_data = momo_client.fetch_transactions(user_id)
        transactions = [Transaction(**t) for t in transactions_data.get('transactions', [])]

        # Analyze with AI
        analysis = ai_engine.analyze_transactions(transactions)
        insight = ai_engine.recommend_savings(analysis)

        return insight
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/round-up/{user_id}")
async def get_round_up_savings(user_id: str):
    """
    Calculate potential round-up savings.
    """
    try:
        transactions_data = momo_client.fetch_transactions(user_id)
        transactions = [Transaction(**t) for t in transactions_data.get('transactions', [])]
        round_up_amount = ai_engine.calculate_round_up_savings(transactions)
        return {"round_up_savings": round_up_amount}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
