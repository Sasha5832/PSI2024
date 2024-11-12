from abc import ABC, abstractmethod
from typing import List
from domains.post import Post

class IPostRepository(ABC):
    @abstractmethod
    async def fetch_posts(self) -> List[Post]:
        pass
    @abstractmethod
    async def filter_posts(self, query: str) -> List[Post]:
        pass
