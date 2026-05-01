from controllers import user_controller
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    openapi_prefix="",
    title="Challengers-Api",
    description="Challengers-Api",
    docs_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_controller.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
