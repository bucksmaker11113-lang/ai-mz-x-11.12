import random

def risk_management(prices, decision):
    if decision == "HOLD":
        return {"leverage": 0, "risk_pct": 0}
    vol = abs(prices[-1] - prices[-2]) / prices[-2]
    risk_pct = max(0.5, min(2.0, vol * 100))
    leverage = random.choice([25, 50])
    return {"leverage": leverage, "risk_pct": round(risk_pct, 2)}
