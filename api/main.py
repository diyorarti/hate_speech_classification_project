from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.config import settings
from api.routers import home, predict

def App() -> FastAPI:
    app = FastAPI(title=settings.API_NAME, version=settings.API_VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(home.router)
    app.include_router(predict.router)

    return app

app = App()
