from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import oracledb

dbconn = oracledb.init_oracle_client()

templates = Jinja2Templates(directory="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", context= {"request": request})
