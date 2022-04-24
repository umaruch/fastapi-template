from fastapi import FastAPI, APIRouter


from src.core.settings import ApplicationSettings
from src.api import routers


class ApplicationBuilder:
    def __init__(self, settings: ApplicationSettings) -> None:
        self.app = FastAPI()
        self._settings = settings
        self.app.settings = settings

    def configure_routes(self) -> None:
        main_api_router = APIRouter()
        for url, router in routers.items():
            main_api_router.include_router(router, prefix=url)

        self.app.include_router(main_api_router, prefix=self.app.settings.API_URL)

    def configure_exception_handlers(self) -> None:
        pass

    def configure_state(self) -> None:
        pass

    def build(self) -> FastAPI:
        self.configure_routes()
        self.configure_exception_handlers()
        self.configure_state()
        return self.app