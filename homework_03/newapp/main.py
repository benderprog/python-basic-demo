import uvicorn
from fastapi import FastAPI
from items_views import router as items_router
from users.views import router as users_router

app = FastAPI(
    redoc_url=None,
)
app.include_router(
    items_router,
    prefix="/items",
)
app.include_router(
    users_router,
    prefix="/users",
)


@app.get("/")
def index():
    return {
        "message": "index",
    }


@app.get("/hello/")
def hello(name: str = "World!"):
    return {
        "message": f"Hello, {name}!"
    }

@app.get(
    path="/ping/",
)
def ping():
    return {
        "message": "pong"
    }



def main():
    uvicorn.run(
        "main:app",
        reload=True,
    )

if __name__ == '__main__':
    main()