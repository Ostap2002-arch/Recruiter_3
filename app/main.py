import sys
from os.path import dirname, abspath

from fastapi import FastAPI

sys.path.insert(0, dirname(abspath(__file__)))
from pages.router import router as router_pages
from api.router import router as router_api

app = FastAPI()
app.include_router(router_api)
app.include_router(router_pages)
