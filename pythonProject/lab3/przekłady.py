from dataclasses import dataclass
from typing import List

@dataclass
class Post:
    id: int
    title: str
    body: str

from abc import ABC, abstractmethod
from typing import List

class IPostRepository(ABC):
    @abstractmethod
    async def fetch_posts(self) -> List[Post]:
        pass

    @abstractmethod
    async def get_posts(self) -> List[Post]:
        pass

import aiohttp
from typing import List

class PostRepository(IPostRepository):
    def __init__(self):
        self._posts: List[Post] = []

    async def fetch_posts(self) -> List[Post]:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://jsonplaceholder.typicode.com/posts") as response:
                if response.status != 200:
                    return []

                data = await response.json()
                self._posts = [Post(id=post["id"], title=post["title"], body=post["body"]) for post in data]
                return self._posts

    async def get_posts(self) -> List[Post]:
        return self._posts

from abc import ABC, abstractmethod
from typing import List

class IPostService(ABC):
    @abstractmethod
    async def filter_posts(self, keyword: str) -> List[Post]:
        pass


from typing import List

class PostService(IPostService):
    def __init__(self, repository: IPostRepository):
        self.repository = repository

    async def filter_posts(self, keyword: str) -> List[Post]:
        all_posts = await self.repository.get_posts()
        return [post for post in all_posts if keyword.lower() in post.title.lower() or keyword.lower() in post.body.lower()]


from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    repository = providers.Singleton(PostRepository)
    service = providers.Factory(PostService, repository=repository)

import asyncio
import json
from dependency_injector.wiring import inject, Provide

@inject
async def main(service: IPostService = Provide[Container.service]):
    # Fetch and save posts
    await service.repository.fetch_posts()

    # Filter posts with a specific keyword (e.g., "qui")
    filtered_posts = await service.filter_posts("qui")

    # Print filtered posts as JSON
    print(json.dumps([post.__dict__ for post in filtered_posts], indent=4))

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
