import aiohttp
from typing import List
from domains.post import Post
from repositories.ipost_repository import IPostRepository
from utils import consts

class PostRepository(IPostRepository):
    def __init__(self):
        self.posts: List[Post] = []
    async def fetch_posts(self) -> List[Post]:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_POSTS_URL) as response:
                if response.status == 200:
                    data = await response.json()
                    self.posts = [Post(**item) for item in data]
        return self.posts
    async def filter_posts(self, query: str) -> List[Post]:
        return [
            post for post in self.posts
            if query.lower() in post.title.lower() or query.lower() in post.body.lower()
        ]

