from io import BytesIO
import os
import aiohttp
from pyrogram import Client, filters

# command handle 
@Client.on_message(filters.command("gen"))
async def imagine(client, message):
    prompt = message.text.split(" ", 1)
    if len(prompt) == 1:
        await message.reply("**Please provide your prompt for generating an image**")
        return        
    prompt = prompt[1]
    m = await message.reply("**Please wait for a few seconds..**")    
    url = f"https://horridapi2-0.onrender.com/imagine?prompt={prompt}&api_key=horridapi_OPmNaSRCp6mjamT0WDguLA_free_key"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image_data = await response.read()
    with BytesIO(image_data) as out_file:
        out_file.name = "image.jpg"
        await message.reply_photo(photo=out_file, caption=f"**🎉 Image generated by @movies_mnbot \n👨‍💻 Join @mnbots for more awesome content! 💥\nPrompt: {prompt}**")
    await m.delete()
