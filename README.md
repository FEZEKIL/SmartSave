# SmartSave

SmartSave aims to solve the problem of inconsistent saving habits by leveraging AI and the MoMo API. The system securely analyzes a user's transaction history to create a financial profile. A machine learning model predicts disposable income and recommends optimal savings amounts. The app uses MoMo's disbursement API to automatically transfer these amounts into a savings wallet at regular intervals.

## Features

- Fetch user transactions via MoMo API
- AI-powered analysis of transaction history
- Predict disposable income using ML models
- Recommend savings amounts (e.g., 5% of income, round-ups)
- Automatic transfers to savings wallet via MoMo API
- Actionable financial insights

## Technologies

- **Backend**: Python with FastAPI
- **AI/ML**: Scikit-learn, TensorFlow for time-series forecasting
- **API Integration**: MoMo API

## Project Structure

```
momo-smartsave-hackathon/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application instance & routes
│   ├── momo_client.py   # Functions to call the MoMo API
│   ├── ai_engine.py     # Core logic for savings rules & AI analysis
│   └── models.py        # Pydantic models for request/response validation
├── tests/               # Unit tests
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API keys)
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env`
4. Run the application: `uvicorn app.main:app --reload`

## API Endpoints

- `GET /transactions` - Fetch user transactions
- `POST /savings-goal` - Set savings goal
- `POST /transfer` - Initiate transfer to savings wallet
- `GET /insights` - Get AI-generated financial insights

## Usage

1. Authenticate with MoMo API
2. Fetch transaction history
3. Analyze data with AI engine
4. Set savings goals and automate transfers

## Contributing

This is a MTN MoMo Hackathon project. Feel free to contribute improvements!

## License

MIT License
