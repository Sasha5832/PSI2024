from typing import List
from domains.post import Post
from repositories.ipost_repository import IPostRepository
from services.ipost_service import IPostService

class PostService(IPostService):
    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository
    async def load_posts(self) -> List[Post]:
        return await self.repository.fetch_posts()
    async def search_posts(self, query: str) -> List[Post]:
        return await self.repository.filter_posts(query)
