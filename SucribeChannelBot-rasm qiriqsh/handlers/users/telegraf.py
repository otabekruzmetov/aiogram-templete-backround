from aiogram import types
from loader import dp
from utils import photo_link
from aiogram.dispatcher.filters.builtin import Command
from utils.removeBackround import remove

@dp.message_handler(content_types="photo")
async def photo(msg: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    await msg.answer(link)

    new_photo = await remove(link)
    await msg.reply_document(document=new_photo,
                             caption="Orqa fon olindi")
