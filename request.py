from fastapi import FastAPI
from controller import get_requests, update_requests, delete_requests, insert_requests

app = FastAPI()

app.include_router(get_requests.router)
app.include_router(update_requests.router)
app.include_router(delete_requests.router)
app.include_router(insert_requests.router)
