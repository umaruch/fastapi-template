from fastapi import FastAPI


from src.core.settings import ApplicationSettings

class ApplicationBuilder:
    def __init__(self, settings: ApplicationSettings) -> None:
        self.app = FastAPI()
        self._settings = settings
        self.app.settings = settings

    def configure_routes(self) -> None:
        pass

    def configure_exception_handlers(self) -> None:
        pass

    def configure_state(self) -> None:
        pass

    def build(self) -> FastAPI:
        return self.app