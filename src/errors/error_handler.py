from fastapi import HTTPException
from src.errors.types.http_bad_request_error import HttpBadRequestError

def error_handler(exception: Exception) -> HTTPException:
    if isinstance(exception, HttpBadRequestError):
        # alertar um sistema de mensagens
        # Log para quando ocorrer esse erro...
        # Vários processamentos
        raise HTTPException(
            status_code=exception.status_code,
            detail=exception.message
        )
    
    raise HTTPException(
        status_code=500,
        detail="Erro insperado ao processar!!"
    )