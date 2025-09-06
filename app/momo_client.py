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
        """
        url = f"{self.base_url}/users/{user_id}/transactions"
        params = {}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def create_savings_goal(self, user_id: str, amount: float, deadline: str = None):
        """
        Create a savings goal for the user.
        """
        url = f"{self.base_url}/users/{user_id}/savings-goals"
        payload = {
            "amount": amount
        }
        if deadline:
            payload["deadline"] = deadline
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def transfer_to_savings(self, user_id: str, amount: float):
        """
        Transfer money to the user's savings wallet.
        """
        url = f"{self.base_url}/users/{user_id}/transfer"
        payload = {
            "amount": amount
        }
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()
