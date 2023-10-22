import strawberry
from strawberry.types import Info

from .views import Context


@strawberry.type
class Query:
    @strawberry.field
    def hello(self, info: Info[Context, None]) -> str:
        print(info.context["user_id"])

        return "Hello, world!"


schema = strawberry.Schema(query=Query)
