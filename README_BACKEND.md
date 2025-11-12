# MZ/X 4.3 Backend – Railway Deploy
Önállóan tanuló mesterséges intelligencia rendszer (FastAPI + SQLite)

## Funkciók
- Monte Carlo + Hybrid Bias + SMC struktúra azonosítás
- OrderBlock alapú döntés (verzió 4.3)
- Saját tanulási adatbázis (SQLite)
- CSV naplózás
- Railway deploy támogatás

## Telepítés
1. Railway → New Project → Deploy from GitHub
2. Build command: pip install -r requirements.txt
3. Start command: python main.py
4. Environment:
   - AI_MODE=self_learning
   - TZ=Europe/Budapest
