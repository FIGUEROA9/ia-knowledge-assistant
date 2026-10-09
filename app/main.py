from fastapi import FastAPI

from app.api.routes import health

app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.1.0",
    description="Bootstrap API - primer incremento funcional",
)

app.include_router(health.router)
