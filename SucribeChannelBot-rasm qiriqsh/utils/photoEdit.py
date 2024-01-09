from io import BytesIO
import aiohttp
from aiogram import types
from loader import bot

async def photo_link(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=file,
        )

        async with bot.session.post("https://telegra.ph/upload", data=form) as response:
            img_scr = await response.json()
            print(img_scr)
    link = "http://telegra.ph/" + img_scr[0]["src"]
    return link