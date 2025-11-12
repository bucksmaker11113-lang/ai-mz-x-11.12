def hybrid_bias(prices):
    if len(prices) < 5:
        return 0.0
    delta = (prices[-1] - prices[0]) / prices[0]
    bias = delta * 0.5
    return max(min(bias, 0.1), -0.1)
