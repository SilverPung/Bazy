from fastapi import FastAPI
from controller import get_requests, update_requests, delete_requests, post_requests
import web_page
from fastapi.staticfiles import StaticFiles

app = FastAPI(description="""
## Welcome to an API Connecing to the firebird database with following tables:\n
-Agent\n
-Agreement\n
-Client\n
-Manager\n
-ManagerAgent\n
-Meeting\n
-Payment\n
-Property\n
-Rents\n
-Repairs\n
-Review\n
-Sales\n
-Tel_number\n
-User\n
""",)

app.include_router(get_requests.router)
app.include_router(post_requests.router, tags=["POST"])
app.include_router(update_requests.router, tags=["UPDATE"])
app.include_router(delete_requests.router, tags=["DELETE"])
app.include_router(web_page.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

