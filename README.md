# FreshFlow - Production-Ready Market Intelligence Website

FreshFlow is now structured as a full-stack web application with a FastAPI backend and a responsive frontend dashboard.

## What is included

- Backend API (`FastAPI`) with versioned routes
- Frontend website (`HTML/CSS/JS`) served by backend
- Market analytics (forecasting, volatility, anomaly detection)
- Multi-agent recommendations (farmer, trader, analyst)
- Optional Gemini AI commentary endpoint
- Docker support and test scaffolding

## API Endpoints

- `GET /api/v1/health`
- `GET /api/v1/dashboard?limit=120&commodity=Potato`
- `POST /api/v1/insight`

## Local Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure environment:

```bash
cp .env.example .env
```

3. Start the app:

```bash
uvicorn backend.main:app --reload
```

4. Open:

- Website: `http://127.0.0.1:8000/`
- API docs: `http://127.0.0.1:8000/docs`

## Docker Run

```bash
docker build -t freshflow .
docker run --rm -p 8000:8000 --env-file .env freshflow
```

## Tests

```bash
pytest -q
```
