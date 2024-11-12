from dependency_injector.wiring import Provide
import asyncio
import json

from container import Container
from services.ipost_service import IPostService

async def main(service: IPostService = Provide[Container.service]) -> None:
    await service.load_posts()
    print("All posts have been loaded.")
    query = input("Enter a search query: ")
    filtered_posts = await service.search_posts(query)
    result = [post.__dict__ for post in filtered_posts]
    print("Filtered posts (in JSON format):")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    asyncio.run(main())
