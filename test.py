from dataclasses import dataclass
from fastapi import FastAPI, APIRouter, Depends

from app.infrastructure.mediator.mediator import ConcreteMediator
from app.application.base.base_query import BaseQuery
from app.application.base.query_handler import QueryHandler

@dataclass(frozen=True)
class GetUserQuery(BaseQuery):
    user_id: int


class GetUserHandler(QueryHandler[GetUserQuery, int]):
    def __init__(self) -> None:
        pass

    async def __call__(self, query: GetUserQuery) -> int:
        return query.user_id
    

def setup_handlers(mediator: ConcreteMediator) -> None:
    mediator.register_query_handler(GetUserQuery, GetUserHandler())

mediator = ConcreteMediator()

def get_mediator() -> ConcreteMediator:
    return mediator

router = APIRouter()

@router.get('/user{user_id}')
async def get_user(user_id: int, mediator: ConcreteMediator = Depends(get_mediator)) -> int:
    print(mediator.query_handlers)
    return await mediator.process_query(GetUserQuery(user_id=user_id))

def setup_routes(app: FastAPI) -> None:
    app.include_router(router)

def setup_app() -> None:
    setup_handlers(mediator)
    print(mediator.query_handlers)
    app = FastAPI()
    setup_routes(app)
    return app
    