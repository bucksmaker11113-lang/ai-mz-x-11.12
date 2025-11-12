import random

def montecarlo_simulation(price, bias, trials=500):
    outcomes = []
    for _ in range(trials):
        drift = random.uniform(-0.03, 0.03) + bias
        outcomes.append(price * (1 + drift))
    return sum(outcomes) / len(outcomes)
