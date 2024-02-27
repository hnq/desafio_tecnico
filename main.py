from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# Dicionário de cotações
currencies = {
    "USD": 1.0,
    "BRL": 5.3,
    "EUR": 0.85,
    "BTC": 0.000023,
    "ETH": 0.00035
}

@app.get("/convert/")
async def convert_currency(from_currency: str, to_currency: str, amount: float):
    if from_currency not in currencies or to_currency not in currencies:
        return {"error": "Moeda não suportada"}

    if amount < 0:
        return {"error": "O valor a ser convertido deve ser positivo"}

    result = amount * (currencies[to_currency] / currencies[from_currency])
    return {"result": result}
