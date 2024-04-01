from fastapi import APIRouter
from api.v1.endpoints import aprendiz

api_router = APIRouter()
api_router.include_router(aprendiz.router, prefix='/aprendiz', tags=["aprendizes"])