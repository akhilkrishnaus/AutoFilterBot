from pyrogram import Client, filters
from Mangandi import ImageUploader
import requests 

api_key = "horridapi_vWPjevmyVpTUSkx0OsmpIg_free_key"

num = 8

@Client.on_message(filters.command(["upscale", "improve"]))
async def upscale(bot, m):
    if not m.reply_to_message.photo:
        await m.reply_text("<b>Rᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ!</b>")
        return
 
    if m.reply_to_message.photo:
        s = await m.reply_text("<b>Dᴏᴡɴʟᴏᴅɪɴɢ...</b>")
        download = await m.reply_to_message.download()
        await s.edit("<b>Uᴘʟᴏᴀᴅɪɴɢ...</b>")
        media = ImageUploader(download)
        photo = media.upload()       
        response = requests.get(f"https://horridapi2-0.onrender.com/upscale?api_key={api_key}&url={photo}&scale={num}")
        data = response.json()
        
        if not data["STATUS"] == "OK":
            await s.edit(f"<b>Aɴ Oᴄᴄᴜʀᴇᴅ Eʀʀᴏʀ: <code>{data['error']}</code></b>")

        if data["STATUS"] == "OK":
            await bot.send_document(chat_id=m.chat.id, document=data["data"][0]["URL"], caption="<b>Sᴜᴄᴄᴇꜱꜱғᴜʟʟʏ Uᴘꜱᴄᴀʟᴇᴅ</b>")
