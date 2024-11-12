from abc import ABC, abstractmethod
from typing import List
from domains.post import Post

class IPostService(ABC):
    @abstractmethod
    async def load_posts(self) -> List[Post]:
        pass
    @abstractmethod
    async def search_posts(self, query: str) -> List[Post]:
        pass
