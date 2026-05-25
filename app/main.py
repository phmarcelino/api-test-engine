from fastapi import FastAPI
from  app.core.config import settings

from app.routers import auth

from app.database import engine
from app.models import user
from app.database import Base

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    description = "Engine para realização de testes de APIs Rest e SOAP com autenticação JWT"
)

app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {
        "status": "Bem-Vindo ao API_Teste! Configurações Concluídas.",
        "app" : settings.app_name,
        "version" : settings.app_version
    }