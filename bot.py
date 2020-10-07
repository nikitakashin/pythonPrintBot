from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions, ContentType

import json
import time

from config import TOKEN, GREETING, ADMIN
import keyboards as kb
from db import add_user_to_db






bot = Bot(token = TOKEN)
dp = Dispatcher(bot)





def makeDownloadLink(message, TOKEN):
    fileinfo = json.loads(str(message))
    LINK = "https://api.telegram.org/file/" + TOKEN + "/" + fileinfo["document"]["file_id"]
    return LINK

def getSize(message):
    fileinfo = json.loads(str(message))
    size = int(fileinfo["document"]["file_size"])
    return size




@dp.message_handler(commands=['start'])
async def process_start_comand(message: types.Message):
    await message.reply(GREETING, reply_markup=kb.greet_kb)
    add_user_to_db(message)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/print', '/copy', '/scan', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.greet_kb)

@dp.message_handler(commands=['print'])
async def process_print_comand(message: types.Message):
    await message.reply('Просто отправьте мне документ который надо распечатать')

@dp.message_handler(commands=['copy'])
async def process_copy_comand(message: types.Message):
    await message.reply('Для того чтобы сделать копию свяжитесь с оператором: ' + ADMIN)

@dp.message_handler(commands=['scan'])
async def process_scan_comand(message: types.Message):
    await message.reply('Для того чтобы сделать скан свяжитесь с оператором: ' + ADMIN)

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def process_recive_comand(message: types.Message):
    if (getSize(message) < 20971520):
        await message.reply('Принято в работу. За подробностями: ' + ADMIN)
        await bot.send_message("@" + ADMIN, makeDownloadLink(message, TOKEN))
    else:
        await message.reply('Файл должен быть меньше 20 МБ, сожмите свой файл, либо залейте в облако и пришлите ссылку на него ☺')

@dp.message_handler(content_types=ContentType.PHOTO)
async def process_recive2_comand(message: types.Message):
    await message.reply('Принято в работу. За подробностями: ' + ADMIN)

@dp.message_handler(regexp='http')
async def process_recive3_comand(message: types.Message):
    await message.reply('Принято в работу. За подробностями: ' + ADMIN)

@dp.message_handler(regexp='привет')
async def process_recive4_comand(message: types.Message):
    await message.reply('ну привет')
   
@dp.message_handler(regexp='иди нахуй')
async def process_recive5_comand(message: types.Message):
    await message.reply('сам иди нахуй')
    time.sleep(2)
    await message.reply('чмо ебаное')
    time.sleep(1)
    await message.reply('в багажнике поедешь')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Мне некогда болтать...')


if __name__ == '__main__':
    executor.start_polling(dp)