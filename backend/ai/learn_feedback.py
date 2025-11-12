import sqlite3, os, datetime

DB_PATH = "data/learn.db"

def update_learning(pair, bias, risk, decision):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS learning (
        ts TEXT, pair TEXT, bias REAL, decision TEXT, risk_pct REAL, leverage INTEGER)""")
    cur.execute("INSERT INTO learning VALUES (?, ?, ?, ?, ?, ?)",
                (datetime.datetime.now().isoformat(), pair, bias, decision, risk["risk_pct"], risk["leverage"]))
    conn.commit()
    conn.close()
