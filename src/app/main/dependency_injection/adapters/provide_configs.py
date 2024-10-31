from typing import Self
from dishka import Provider, Scope, provide

from app.main.config import ConfigFactory
from app.main.config_loader import load_config


class ConfigProvider(Provider):
    @provide(scope=Scope.APP)
    def get_config(self: Self) -> ConfigFactory:
        return load_config()