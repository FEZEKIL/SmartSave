from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Transaction(BaseModel):
    id: str
    amount: float
    description: str
    date: datetime
    type: str  # 'income' or 'expense'

class UserProfile(BaseModel):
    user_id: str
    transactions: List[Transaction]

class SavingsGoal(BaseModel):
    user_id: str
    target_amount: float
    current_amount: float
    deadline: Optional[datetime] = None

class TransferRequest(BaseModel):
    user_id: str
    amount: float
    to_wallet: str

class AIInsight(BaseModel):
    insight_type: str
    message: str
    recommendation: Optional[str] = None

class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
