"""
Egyszerű liquidity grab detektálás:
- Wick alapú kiszúrás: ha az utolsó gyertya felső/alsó kanóca nagyobb, mint a teljes range X%-a,
  és kitör az előző N gyertya high/low tartományából, majd visszazár – gyakori „liquidity sweep” jel.
"""

from typing import List, Literal

def detect_liquidity_grab(
    highs: List[float],
    lows: List[float],
    closes: List[float],
    wick_ratio: float = 0.6,
    lookback: int = 10
) -> Literal["buy_sweep","sell_sweep","none"]:
    if len(highs) < max(lookback, 3):
        return "none"

    # utolsó gyertya
    h, l, c = highs[-1], lows[-1], closes[-1]
    prev_high = max(highs[-(lookback+1):-1])
    prev_low  = min(lows[-(lookback+1):-1])

    rng = h - l if h > l else 1e-9
    # ha a zárás visszatér a range-be és nagy wick látszik, sweep-gyanú
    upper_wick = h - max(c, (h + l) / 2)
    lower_wick = min(c, (h + l) / 2) - l

    # sell side liquidity grab (felső likviditás kiszedése)
    if h > prev_high and c < prev_high and upper_wick / rng >= wick_ratio:
        return "sell_sweep"

    # buy side liquidity grab (alsó likviditás kiszedése)
    if l < prev_low and c > prev_low and lower_wick / rng >= wick_ratio:
        return "buy_sweep"

    return "none"
