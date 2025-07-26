# Conversational AI Backend

## Setup Instructions

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Setup PostgreSQL and update `.env` with your DB credentials.
4. Run the app:
```bash
uvicorn app.main:app --reload
```
