from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from devtools import debug


@strawberry.type
class Missing:
    message: str


@strawberry.type
class User:
    id: str
    name: str


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def user(self, info: Info) -> User | Missing:
        headers = info.context['request'].headers
        if headers.get('user') == '1':
            return User(id="1", name="Patrick Star")
        return Missing(message="User not found")


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graphql_app, prefix="/graphql")
