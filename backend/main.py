from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai.core_engine import analyze_market, generate_signal
from utils.logger import log_trade
import os, datetime, sqlite3, csv

app = FastAPI(title="MZ/X 4.3 Self-Learning AI Engine")

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "data/learn.db"
REPORT_PATH = "reports/daily_log.csv"

# --- Health check ---
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "version": "4.3",
        "time": datetime.datetime.now().isoformat(),
        "mode": os.getenv("AI_MODE", "self_learning"),
    }

# --- Elemzés végrehajtása ---
@app.get("/api/analyze/{pair}")
async def analyze(pair: str):
    result = analyze_market(pair)
    log_trade(pair, result)
    return result

# --- Jelzés generálása ---
@app.get("/api/signal/{pair}")
async def signal(pair: str):
    return generate_signal(pair)

# --- Jelentés lekérése ---
@app.get("/api/report")
async def report():
    try:
        with open(REPORT_PATH, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)[-10:]
    except FileNotFoundError:
        return {"error": "Nincs még jelentés generálva."}

@app.get("/")
def home():
    return {"message": "MZ/X Backend fut", "AI": "aktív"}
