import uvicorn
from fastapi import FastAPI
from src.routes import contacts, auth

app = FastAPI()

app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')


@app.get("/")
def read_root():
    return {'messege': 'Contact api'}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
