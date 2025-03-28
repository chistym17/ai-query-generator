from fastapi import FastAPI
from Routes.query import router as query_router
from Routes.validation import router as validation_router

app = FastAPI()

app.include_router(query_router)
app.include_router(validation_router)


@app.get("/")
def root():
    return {"message": "SQL Query Generator API is running!"}
