from fastapi import FastAPI
import models
from database import engine
import uvicorn


from routers.user import users

models.base.metadata.create_all(bind = engine)
app = FastAPI()

app.include_router(users.app, tags=["user"])

@app.get("/")
def read_root():
    return {"Hello" : "World"}



if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)