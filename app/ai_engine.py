import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from app.models import Transaction, AIInsight

class AIEngine:
    def __init__(self):
        self.model = LinearRegression()

    def analyze_transactions(self, transactions: list[Transaction]) -> dict:
        """
        Analyze transaction history to extract insights.
        """
        df = pd.DataFrame([t.dict() for t in transactions])
        df['date'] = pd.to_datetime(df['date'])

        # Calculate basic stats
        total_income = df[df['type'] == 'income']['amount'].sum()
        total_expenses = df[df['type'] == 'expense']['amount'].sum()
        disposable_income = total_income - total_expenses

        # Predict future disposable income
        prediction = self.predict_disposable_income(df)

        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "disposable_income": disposable_income,
            "predicted_disposable_income": prediction
        }

    def predict_disposable_income(self, df: pd.DataFrame) -> float:
        """
        Simple linear regression to predict disposable income.
        """
        # Prepare data
        df['month'] = df['date'].dt.month
        monthly_data = df.groupby('month').agg({
            'amount': lambda x: x[df['type'] == 'income'].sum() - x[df['type'] == 'expense'].sum()
        }).reset_index()

        if len(monthly_data) < 2:
            return df['amount'].sum()  # Fallback

        X = monthly_data[['month']]
        y = monthly_data['amount']

        self.model.fit(X, y)
        next_month = np.array([[df['month'].max() + 1]])
        return self.model.predict(next_month)[0]

    def recommend_savings(self, analysis: dict) -> AIInsight:
        """
        Generate savings recommendations based on analysis.
        """
        disposable = analysis['disposable_income']
        if disposable > 0:
            savings_amount = disposable * 0.05  # 5% rule
            return AIInsight(
                insight_type="savings_recommendation",
                message=f"Based on your disposable income of ${disposable:.2f}, we recommend saving ${savings_amount:.2f} per month.",
                recommendation=f"Save ${savings_amount:.2f} automatically each month."
            )
        else:
            return AIInsight(
                insight_type="budget_alert",
                message="Your expenses exceed your income. Consider reducing discretionary spending.",
                recommendation="Review your expenses and cut non-essential costs."
            )

    def calculate_round_up_savings(self, transactions: list[Transaction]) -> float:
        """
        Calculate potential savings from rounding up transactions.
        """
        total_round_up = 0
        for t in transactions:
            if t.type == 'expense':
                round_up = np.ceil(t.amount) - t.amount
                total_round_up += round_up
        return total_round_up
