from abc import ABC, abstractmethod

class Search(ABC):
	@abstractmethod
	async def search()-> tuple[str, int]:
		pass