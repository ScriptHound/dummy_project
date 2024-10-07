import logging

from fastapi import FastAPI

app = FastAPI()

uvicorn_error = logging.getLogger("uvicorn.error")
uvicorn_error.disabled = True
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
