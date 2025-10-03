from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request):
    return  templates.TemplateResponse(name="index.html", request=request)