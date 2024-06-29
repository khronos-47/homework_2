from abc import ABC, abstractmethod


class AbstractSearch(ABC):
    @abstractmethod
    async def search() -> tuple[str, int]:
        pass
