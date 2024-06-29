from logging import getLogger

from fastapi import FastAPI
from uvicorn import run

from .endpoints import list_of_routes


logger = getLogger(__name__)


def bind_routes(application: FastAPI) -> None:
    """
    Bind all routes to application.
    """
    for route in list_of_routes:
        application.include_router(route)


def get_app() -> FastAPI:

    application = FastAPI()
    bind_routes(application)
    return application


app = get_app()


if __name__ == "__main__":  # pragma: no cover

    run(
        "cart_validation_service.app:app",
        host="0.0.0.0",
        port=7432,
        reload=True,
        reload_dirs="cart_validation_service",
        log_level="debug",
    )
# rlkgldgrnjdjdf
