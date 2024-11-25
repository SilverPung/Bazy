from fastapi import FastAPI
from controller import get_requests

app = FastAPI()

app.include_router(get_requests.router)