from fastapi import FastAPI


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware()
