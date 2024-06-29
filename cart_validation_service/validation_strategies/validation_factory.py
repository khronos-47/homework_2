from abc import ABC, abstractmethod


class Validate(ABC):
    @abstractmethod
    async def validate() -> dict:
        pass
