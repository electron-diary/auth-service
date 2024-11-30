from fastapi import APIRouter

metrics: APIRouter = APIRouter(prefix="/metrics", tags=["metrics"])
