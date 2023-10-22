from django.http import HttpRequest
from django.http.response import HttpResponse
from strawberry.django.views import AsyncGraphQLView

from typing import TypedDict


class Context(TypedDict):
    user_id: int | None
    request: HttpRequest
    response: HttpResponse


class GraphQLView(AsyncGraphQLView[Context, None]):
    async def get_context(
        self, request: HttpRequest, response: HttpResponse
    ) -> Context:
        user_id = None

        # this is were you'd have your logic
        if request.user.is_authenticated:
            user_id = request.user.id  # type: ignore

        return {"user_id": user_id, "request": request, "response": response}
