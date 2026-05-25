from fastapi import FastAPI
from  app.core.config import settings


app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    description = "Engine para realização de testes de APIs Rest e SOAP com autenticação JWT"
)

@app.get("/health")
def health_check():
    return {
        "status": "Bem-Vindo ao API_Teste! Configurações Concluídas.",
        "app" : settings.app_name,
        "version" : settings.app_version
    }