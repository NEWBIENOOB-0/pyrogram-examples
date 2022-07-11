from pyrogram import Client ,filters
from pyrogram.types import ChatPermissions
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Client(
    "my_bot",
api_id = put_your_id,
api_hash = "put_your_api_hash",
bot_token = "put_bot_token"
)

#start commmand
@bot.on_message(filters.command("start"))
def start_command(client, message):
    bot.send_message(message.chat.id,"**hi buddy i am ruuning**")
    
#help commmand
@bot.on_message(filters.command("help"))
def help_command(client, message):
    message.reply_text("`hi buddy how can i help you`")
    
#id commmand
@bot.on_message(filters.command("id"))
def id_command(client, message):
    message.reply_text(message.chat.id)

#echobot  this command disabled for other commands 
'''@bot.on_message (filters.text & filters.private)
def echobot (client, message):
    message.reply_text(message.text)'''

#welocomebot
group = "loflive"
welcome_message = "hello wellcome to chat"
left_message = "see you synora"
@bot.on_message(filters.chat(group) & filters.new_chat_members)
def welcomebot(client, message):
    message.reply_text(welcome_message)

#goodbyebot
@bot.on_message(filters.chat(group) & filters.left_chat_member)
def goodbyebot(client, message):
    message.reply_text(left_message)
 
#send image    
@bot.on_message(filters.command("image"))
def send_image (bot, message):
    bot.send_photo (message.chat.id,"https://imgur.com/gallery/wYTCtRu")
    
@bot.on_message(filters.audio & filters.private)
def get_audio(bot, message):
    message.reply(message.audio.file_id) #get file audio file id
    
#send audio through file id
@bot.on_message(filters.command("audio"))
def send_audio(bot, message):
    bot.send_audio(message.chat.id,"CQACAgIAAxkBAANHYrwhpd_A1JiUyvTKWJjyZwtPePoAAqQFAAIK93hLlKxez0I29eUeBA")

@bot.on_message(filters.document & filters.private)
def get_document(bot, message):
    message.reply(message.document.file_id) #get file document file id
    
#send documnet through file id
@bot.on_message(filters.command("doc"))
def send_document(bot, message):
    bot.send_document(message.chat.id,"BQACAgUAAxkBAANUYrwlqbV0jIJnR8OwuVTCbYHS_7MAAtYFAALMlNlVyGtBqixT5f4eBA")

 #get file video file id
@bot.on_message(filters.command("video"))
def send_video(bot, message):
    bot.send_video(message.chat.id,"BAACAgUAAxkBAANYYrwmnntFMc7Nfjp0UenP7yaw8C4AAtQGAAJW1XlVcszTktD5PRkeBA")

#get voice through file id
@bot.on_message(filters.voice & filters.private)
def get_voice(bot, message):
    message.reply(message.voice.file_id)

#send voice through file id
@bot.on_message(filters.command("voice"))
def send_voice(bot, message):
    bot.send_voice(message.chat.id,"AwACAgIAAxkBAAOYYsfWBJpD53wZnZpiTMbdzQ5oM8wAAsgKAAKsAbFJ7U6wLnr917weBA")

#get gif through file id
@bot.on_message(filters.animation & filters.private)
def get_gif(bot, message):
    message.reply(message.animation.file_id)

# send gif through file id
@bot.on_message(filters.command("gif"))
def send_gif(bot, message):
    bot.send_animation(message.chat.id,"CgACAgQAAxkBAAOiYsfXIDhsfQOGMPnM8TYdqwHbOZQAAiIDAAKhZQRT0peUDq_1IFseBA")

#get sticker through file id
@bot.on_message(filters.sticker & filters.private)
def get_sticker(bot, message):
    message.reply(message.sticker.file_id)

#send sticker file id
@bot.on_message(filters.command("sticker"))
def send_sticker(bot, message):
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAOsYsfag9qdjtwQYfHUEAFTtlS3bPsAAs4CAAM4oApOz5HCaQrLlh4E")

#leave command for left group
@bot.on_message(filters.command("leave") & filters.group)
def bot_leave(bot, message):
    bot.send_message(message.chat.id, "Bye! I am leaving this chat.") 
    bot.leave_chat(message.chat.id)
#ban chat memebr
@bot.on_message(filters.command ("ban")& filters.group)
def ban(bot, message): 
    bot.ban_chat_member(message.chat.id,message.reply_to_message.from_user.id) 
    bot.send_message(message.chat.id,f"{message.reply_to_message.from_user.mention} Banned!")

#unban chat memeber
@bot.on_message(filters.command ("unban")& filters.group)
def ban(bot, message): 
    bot.unban_chat_member(message.chat.id,message.reply_to_message.from_user.id) 
    bot.send_message(message.chat.id,f"{message.reply_to_message.from_user.mention} unBanned!")
    
#mute participants 
@bot.on_message(filters.command ("mute")& filters.group)
def mute(bot, message):
    bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
    bot.send_message(message.chat.id, f"{message.reply_to_message .from_user.mention} Muted")

#inline buttons 
START_MESSAGE = "Heya, I am a simple test bot"
START_MESSAGE_BUTTONS = [
    [InlineKeyboardButton('CHANNEL', url='https://telegram.dog/newbinoob')],
    [InlineKeyboardButton('devloper', url='https://telegram.dog/newbienoobbot')]
]
@bot.on_message(filters.command("start2"))
def start_command(client, message):
    text= START_MESSAGE
    reply_markup = InlineKeyboardMarkup (START_MESSAGE_BUTTONS)
    message.reply(
    text=text,
    reply_markup=reply_markup
    )

print("i am runnig")
bot.run()
