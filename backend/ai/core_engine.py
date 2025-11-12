import random, math, datetime
from ai.montecarlo import montecarlo_simulation
from ai.hybrid_bias import hybrid_bias
from ai.smc_logic import smc_structure
from ai.dynamic_risk import risk_management
from ai.learn_feedback import update_learning

def analyze_market(pair: str):
    prices = [random.uniform(20000, 60000) if "BTC" in pair.upper() else random.uniform(1000, 4000) for _ in range(30)]
    bias = hybrid_bias(prices)
    mc_result = montecarlo_simulation(prices[-1], bias)
    structure = smc_structure(prices)
    decision = "HOLD"
    if mc_result > prices[-1] * 1.01 and structure == "HH-HL":
        decision = "LONG"
    elif mc_result < prices[-1] * 0.99 and structure == "LL-LH":
        decision = "SHORT"
    risk = risk_management(prices, decision)
    update_learning(pair, bias, risk, decision)
    return {
        "pair": pair.upper(),
        "bias": round(bias, 4),
        "prediction": round(mc_result, 2),
        "structure": structure,
        "decision": decision,
        "risk": risk,
        "time": datetime.datetime.now().isoformat()
    }

def generate_signal(pair: str):
    result = analyze_market(pair)
    if result["decision"] == "LONG":
        return {"signal": "Vétel", "strength": result["bias"]}
    elif result["decision"] == "SHORT":
        return {"signal": "Eladás", "strength": result["bias"]}
    return {"signal": "Nincs egyértelmű irány", "strength": 0}
