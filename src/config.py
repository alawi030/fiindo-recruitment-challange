import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.test.fiindo.com/api/v1"
API_KEY = os.getenv("FIINDO_API_KEY")

ENDPOINTS = {
    "symbols": f"{BASE_URL}/symbols",
    "general": f"{BASE_URL}/general/{{symbol}}",
    "income_statement": f"{BASE_URL}/financials/{{symbol}}/income_statement",
    "balance_sheet": f"{BASE_URL}/financials/{{symbol}}/balance_sheet_statement",
    "cash_flow": f"{BASE_URL}/financials/{{symbol}}/cash_flow_statement",
    "eod": f"{BASE_URL}/eod/{{symbol}}",
}
