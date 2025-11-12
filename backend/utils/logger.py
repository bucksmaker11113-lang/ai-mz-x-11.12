import csv, os, datetime

LOG_PATH = "reports/daily_log.csv"

def log_trade(pair, result):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    file_exists = os.path.isfile(LOG_PATH)
    with open(LOG_PATH, "a", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ts", "pair", "decision", "bias", "prediction", "structure"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "ts": datetime.datetime.now().isoformat(),
            "pair": pair,
            "decision": result["decision"],
            "bias": result["bias"],
            "prediction": result["prediction"],
            "structure": result["structure"]
        })
