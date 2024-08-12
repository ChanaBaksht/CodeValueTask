import logging
import uvicorn
from fastapi import FastAPI
from solution.api_server.router import router

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="stores")
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9991)
