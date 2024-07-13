from fastapi import FastAPI
from app.logger import get_logger

app = FastAPI()

# Configure logging
logger = get_logger(__name__)


@app.get("/")
def read_root():
    logger.info("Root endpoint was called")
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(host="0.0.0.0", port=8000, reload=True)
