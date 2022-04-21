import uvicorn

from src.core.settings import ApplicationSettings
from src.core.builder import ApplicationBuilder


def create_application():
    settings = ApplicationSettings()
    builder = ApplicationBuilder(settings=settings)
    return builder.build()

app = create_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)