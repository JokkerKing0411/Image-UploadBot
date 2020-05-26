# This is bot coded by W4RR10R and used for educational purposes only
# Copyright of all images uploaded by this bot is goes to respected owners

import os
from pyrogram import Client,Filters
from telegraph import upload_file

@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"🙋Salom {message.from_user.first_name},\n🤖Bu Bot telegram dan telegra.ph 🌃Rasm Yuklab beradi.\n🎓Yaratuvchi: @JokkerKing",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(Filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="Yuklanmoqda...",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("Biroz kuting...")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Xatolik yuz berdi\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}\n\n🌃Image Upload By @Teleg2GraphBot")
    try:
        os.remove(imgdir)
    except:
        pass


