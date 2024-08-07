import httpx

from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
client = httpx.AsyncClient()

app.mount("/img", StaticFiles(directory="public/img"), name="img")
app.mount("/js", StaticFiles(directory="public/js"), name="js")

templates = Jinja2Templates(directory="public/templates")


@app.get("/", response_class=HTMLResponse)
async def debug_challenge_page(
        request: Request,
        username: str = Query(..., title="username"),
        command: str = Query(..., title="command"),
        uid: str = Query(..., title="uid"),
        gt: str = Query(..., title="gt"),
        challenge: str = Query(..., title="challenge"),
):
    user = {"username": username, "uid": uid, "command": command}
    geetest = {
        "gt": gt,
        "challenge": challenge,
    }
    return templates.TemplateResponse(
        "example.html", {"request": request, "user": user, "geetest": geetest}
    )


@app.get("/webapp", response_class=HTMLResponse)
async def debug_challenge_page(
        request: Request,
        username: str = Query(..., title="username"),
        command: str = Query(..., title="command"),
        uid: str = Query(..., title="uid"),
        gt: str = Query(..., title="gt"),
        challenge: str = Query(..., title="challenge"),
        user_id: str = Query("", title="user_id"),
):
    user = {"username": username, "uid": uid, "command": command, "user_id": user_id}
    geetest = {
        "gt": gt,
        "challenge": challenge,
    }
    return templates.TemplateResponse(
        "webapp.html", {"request": request, "user": user, "geetest": geetest}
    )


@app.get("/tasks1", response_class=HTMLResponse)
async def debug_tasks1_page(
    request: Request,
    command: str = Query(..., title="command"),
    bot_data: str = Query(..., title="bot_data"),
):
    user = {"command": command, "bot_data": bot_data}
    return templates.TemplateResponse(
        "tasks1.html", {"request": request, "user": user}
    )


@app.get("/tasks2", response_class=HTMLResponse)
async def debug_tasks2_page(
    request: Request,
    command: str = Query(..., title="command"),
    bot_data: str = Query(..., title="bot_data"),
):
    user = {"command": command, "bot_data": bot_data}
    return templates.TemplateResponse(
        "tasks2.html", {"request": request, "user": user}
    )


@app.get("/tasks3", response_class=HTMLResponse)
async def debug_tasks3_page(
    request: Request,
    command: str = Query(..., title="command"),
    bot_data: str = Query(..., title="bot_data"),
):
    user = {"command": command, "bot_data": bot_data}
    return templates.TemplateResponse(
        "tasks3.html", {"request": request, "user": user}
    )


@app.get("/tasks4", response_class=HTMLResponse)
async def debug_tasks4_page(
    request: Request,
    command: str = Query(..., title="command"),
    bot_data: str = Query(..., title="bot_data"),
):
    user = {"command": command, "bot_data": bot_data}
    return templates.TemplateResponse(
        "tasks4.html", {"request": request, "user": user}
    )


@app.get("/relic_property", response_class=HTMLResponse)
async def relic_property_page(
    request: Request,
    command: str = Query(..., title="command"),
    name: str = Query(..., title="name"),
    cid: str = Query(..., title="cid"),
    recommend: str = Query(..., title="recommend"),
    custom: str = Query(..., title="custom"),
):
    user = {"command": command, "recommend": recommend, "custom": custom, "name": name, "cid": cid}
    return templates.TemplateResponse(
        "relic_property.html", {"request": request, "user": user}
    )


@app.get("/telegram-web-app.js", response_class=PlainTextResponse)
async def get_telegram_web_js():
    return (await client.get("https://telegram.org/js/telegram-web-app.js")).text
