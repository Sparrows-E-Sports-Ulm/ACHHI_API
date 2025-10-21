from dataclasses import dataclass
from .config import Config

@dataclass
class APIServices:

    config: Config

    @staticmethod
    async def create(config_path: str):
        return APIServices(
            config = Config(config_path),
        )