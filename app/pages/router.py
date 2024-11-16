import sys
from os.path import dirname, abspath

from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates



sys.path.insert(0, dirname(abspath(__file__)))
from app.api.router import home

router = APIRouter(
    prefix='/greetings',
    tags=['Фронтенд']
)

templates = Jinja2Templates(directory='app/templates')


@router.get('/')
def get_pages(request: Request,
              message=Depends(home)):
    return templates.TemplateResponse(name='base_templates.html', context={'request': request, 'message': message})
