from fastapi import APIRouter

router = APIRouter(prefix='/api',
                   tags=['API'])


@router.get('/')
def home(name: str, message: str):
    return f'Hello {name}! {message}!'
