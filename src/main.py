from fastapi import Depends, FastAPI, HTTPException
from auth import AuthHandler
from schema import AuthDetails


app = FastAPI()

auth_handler = AuthHandler()
users = []

@app.post("/register", status_code=201)
def register(auth_details=AuthDetails):
    if any(user["username"] == auth_details.username for user in users):
        raise HTTPException(status_code=400, detail="Username is taken")

@app.post("/login")
def login(auth_details=AuthDetails):
    user = None
    for user in users:
        if user["username"] == auth_details.username:
            u = user
            break

    if not user: 
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    token = auth_handler.encode_token(
        user["username"]
    )
    return {"token": token}

@app.get("/protected")
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {"name": username}

@app.get("/unprotected")
def unprotected():
    return {"message": "unprotected"}