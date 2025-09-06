import os
import requests
from dotenv import load_dotenv

load_dotenv()

MOMO_API_KEY = os.getenv("MOMO_API_KEY")
MOMO_API_SECRET = os.getenv("MOMO_API_SECRET")
MOMO_BASE_URL = os.getenv("MOMO_BASE_URL", "https://sandbox.momodeveloper.mtn.com")

class MoMoClient:
    def __init__(self):
        self.api_key = MOMO_API_KEY
        self.api_secret = MOMO_API_SECRET
        self.base_url = MOMO_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

    def fetch_transactions(self, user_id: str, start_date: str = None, end_date: str = None):
        """
        Fetch user transactions from MoMo API.
        For demo purposes, return mock data.
        """
        # Mock transaction data
        mock_data = {
            "transactions": [
                {
                    "id": "txn_001",
                    "amount": 50.0,
                    "description": "Coffee purchase",
                    "date": "2023-10-01T10:00:00Z",
                    "type": "expense"
                },
                {
                    "id": "txn_002",
                    "amount": 200.0,
                    "description": "Salary",
                    "date": "2023-10-01T09:00:00Z",
                    "type": "income"
                },
                {
                    "id": "txn_003",
                    "amount": 25.0,
                    "description": "Bus fare",
                    "date": "2023-09-30T08:00:00Z",
                    "type": "expense"
                },
                {
                    "id": "txn_004",
                    "amount": 100.0,
                    "description": "Freelance payment",
                    "date": "2023-09-29T15:00:00Z",
                    "type": "income"
                }
            ]
        }
        return mock_data

    def create_savings_goal(self, user_id: str, amount: float, deadline: str = None):
        """
        Create a savings goal for the user.
        For demo purposes, return mock response.
        """
        # Mock response
        mock_response = {
            "goal_id": "goal_001",
            "user_id": user_id,
            "target_amount": amount,
            "deadline": deadline,
            "status": "created"
        }
        return mock_response

    def transfer_to_savings(self, user_id: str, amount: float):
        """
        Transfer money to the user's savings wallet.
        For demo purposes, return mock response.
        """
        # Mock response
        mock_response = {
            "transfer_id": "transfer_001",
            "user_id": user_id,
            "amount": amount,
            "status": "completed"
        }
        return mock_response
