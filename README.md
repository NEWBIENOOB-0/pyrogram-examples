# Learn Pyrogram 
<p align="center">
    <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://docs.pyrogram.org/_static/pyrogram.png" alt="Pyrogram" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://pyrogram.org">
        Homepage
    </a>
    •
    <a href="https://docs.pyrogram.org">
        Documentation
    </a>
    •
    <a href="https://docs.pyrogram.org/releases">
        Releases
    </a>
    •
    <a href="https://t.me/pyrogram">
        News
    </a>
</p>

## Pyrogram
> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

### Installing

``` bash
pip3 install -U pyrogram tgcrypto
```
# Requirements
- Python And Pip Installed
- VS Code (IDE)
- Basic Knowledge About Python Programming (For Advanced Users)
- Secondary Telegram Account 
- Telegram Bot

# Let's get started 
## Setting up enviroments
- Set Your Api Id And Api Hash Bot Token And Authenticate Them: 
``` python
from pyrogram import Client, filters

bot = Client(
    "my_bot",
api_id = put_your_id,
api_hash = "put_your_creditnal",
bot_token = "put_bot_token"
)
print("i am runnig")
bot.run()
```
## Set Your First Command
``` python
@bot.on_message(filters.command("start"))
def start_command(client, message):
    bot.send_message(message.chat.id,"**hi buddy i am running**")
```
- you can set help command with same steps just replace start with help:
``` python
@bot.on_message(filters.command("help"))
```
## Send Image 
``` python
@bot.on_message(filters.command("image"))
def send_image (bot, message):
    bot.send_photo (message.chat.id,"https://imgur.com/gallery/wYTCtRu")
```
## Send Documnet
``` python 
@bot.on_message(filters.document & filters.private) 
def get_document(bot, message):
    message.reply(message.document.file_id) #get document id

#send document
@bot.on_message(filters.command("doc"))
def send_document(bot, message):
     bot.send_document(message.chat.id,"BQACAgUAAxkBAANUYrwlqbV0jIJnR8OwuVTCbYHS_7MAAtYFAALMlNlVyGtBqixT5f4eBA")
```
- You Can Send Video, Audio, Voice, Animation (Gif), Stickers With Given Document Command 
- Just Replace `Filters.Document` With `Filters.Animation`
- Example: 
``` python 
@bot.on_message(filters.animation & filters.private)
def get_gif(bot, message):
    message.reply(message.animation.file_id)

@bot.on_message(filters.command("gif"))
def send_gif(bot, message):
    bot.send_animation(message.chat.id,"CgACAgQAAxkBAAOiYsfXIDhsfQOGMPnM8TYdqwHbOZQAAiIDAAKhZQRT0peUDq_1IFseBA")
```

## Echobot 
- This simple echo bot replies to every private text same as user message:
``` python 
@bot.on_message (filters.text  & filters.private)
def echobot (client, message):
    message.reply_text(message.text)
```
***
- For More Commands And More Info, Pls View Examples.Py
- Examples.Py Includes Ban, Unban, Mute, Buttons, Id And Leave
- For more info,Check [Pyrogram Documentation](https:/https://docs.pyrogram.org/)
***
