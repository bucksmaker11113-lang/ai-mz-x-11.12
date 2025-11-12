def smc_structure(prices):
    if len(prices) < 4:
        return "neutral"
    if prices[-1] > prices[-2] > prices[-3]:
        return "HH-HL"
    if prices[-1] < prices[-2] < prices[-3]:
        return "LL-LH"
    return "range"
