from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.api.routes import router
from backend.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=settings.api_v1_prefix)

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/", include_in_schema=False)
def serve_index() -> FileResponse:
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/{path_name:path}", include_in_schema=False)
def spa_fallback(path_name: str) -> FileResponse:
    if path_name.startswith("api/"):
        raise HTTPException(status_code=404, detail="Not found")

    requested = FRONTEND_DIR / path_name
    if requested.exists() and requested.is_file():
        return FileResponse(requested)

    return FileResponse(FRONTEND_DIR / "index.html")
