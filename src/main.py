from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "dev")
APP_NAME = os.getenv("APP_NAME", "fastapi-demo")
FEATURE_FLAG = os.getenv("FEATURE_FLAG", "false")

API_KEY = os.getenv("API_KEY", "defaultkey")

@app.get("/")
def root():
    return {"message": f"{APP_NAME} running in {APP_ENV} v2"}

@app.get("/config")
def config():
    return {
        "env": APP_ENV,
        "feature_enabled": FEATURE_FLAG
    }

@app.get("/secure")
def secure(key: str):
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "Access granted"}