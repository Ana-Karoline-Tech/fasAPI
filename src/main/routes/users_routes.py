from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["Usuários"])

@users_routes.post("/users")
async def crear_usuario():

        return JSONResponse(
                content={"Ola": "Mundo"}, 
                status_code=200
                )