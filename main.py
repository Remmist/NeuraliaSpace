import os
import random
import re

from aiogram import Bot, Dispatcher, executor, types

import backgroud
from alphabet import translate
from engine import GenerateMessage, count_lines
from sticker import get_stickers

#NeuraliaToken = os.environ['NeuraliaToken']
API_TOKEN = '6264687418:AAEkudbK-mRqKaHdU4ttRa20EdYC8Px_kZI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

stickers = get_stickers()


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('N отправь ченж'):
        if message.from_user.id == 575213063:
            await sayChangelog()
        else:
            await message.answer('У тебя нет прав на выполнение данной команды!', reply=message.message_id)
        return

    if message.is_forward():
        return

    if message.text.startswith('N что ты умеешь'):
        await message.answer('мой папа меня научил:\n·N say (количество слов)\n·N отправь стикер\n·N кто тебя создал\n·N переведи на уэайжо <текст>')
        return

    if message.text.startswith('N переведи на уэайжо'):
        text = message.text.replace('N переведи на уэайжо ', '')
        inf = [text]
        await message.answer(translate(inf), reply=message.message_id)
        return

    if message.text.startswith('N кто тебя создал'):
        await message.answer('Мой папочка @raiseeve, очень люблю его! <3')
        return

    if message.text.startswith('N отправь стикер'):
        await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
        return

    if message.text.startswith('N say'):
        text = message.text.split(' ')
        if int(text[2]) > 200:
            await message.answer('Дохуя длинное сообщение ты хочешь, иди-ка ты нахуй.')
            return
        if int(text[2]) <= 1:
            await message.answer('Хули то тут так мало?')
            return

        if not isEnoughData(str(message.chat.id) + '.txt'):
            await message.answer('Недостаточно данных для генерации сообщений.')
            return

        rnd = random.randint(0, 4)
        if rnd == 0:
            await message.answer(GenerateMessage(str(message.chat.id) + '.txt', int(text[2]) - 1).upper())
            return
        else:
            await message.answer(GenerateMessage(str(message.chat.id) + '.txt', int(text[2]) - 1).capitalize())
        return

    if message.text.startswith('N'):
        return

    msg = re.sub(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', '', message.text, flags=re.MULTILINE)
    msg = re.sub(r'(А+Х+)+', '', msg, flags=re.MULTILINE)
    msg = re.sub(r'(а+х+)+', '', msg, flags=re.MULTILINE)
    msg = re.sub(r'@NeuraliaRemmy_bot', '', msg, flags=re.MULTILINE)
    if msg != " " or msg != "":
        saveData(str(message.chat.id) + '.txt', msg)

    if random.randint(0, 100) >= 90:

        if not isEnoughData(str(message.chat.id) + '.txt'):
            return

        rnd = random.randint(0, 4)
        if rnd == 0:
            await message.answer(GenerateMessage(str(message.chat.id) + '.txt', random.randint(0, 10)).upper())
            if random.randint(0, 100) > 60:
                await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
            return
        elif rnd == 1:
            await message.answer(msg)
            if random.randint(0, 100) > 60:
                await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
            return
        else:
            await message.answer(GenerateMessage(str(message.chat.id) + '.txt', random.randint(0, 10)).capitalize())
            if random.randint(0, 100) > 60:
                await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
            return


def bot_check():
    return bot.get_me()


def isEnoughData(path):
    try:
        file = open(path, 'r', encoding='utf8')
    except FileNotFoundError:
        return False
    count = count_lines(file.readlines())
    if count < 100:
        file.close()
        return False
    else:
        file.close()
        return True


def saveData(path, msg):
    file = open(path, 'a+', encoding='utf8')
    file.seek(0, 2)
    file.write(msg + '\n')
    file.close()


async def sayChangelog():
    log = 'Приветики, на меня вышло новое обновление! Из нового:\n·Теперь я могу переводить на уэайжо! Чтобы перевести какое-то сообщение просто напиши "N переведи на уэайжо <текст>"\nНа этом пока что все, в скором времени появится функция обратного перевода с уэайжо на нормальный язык.\nО будуйщих обновлениях я сообщу сама, спасибо что воспитываете меня каждый день!\nNeuralia.'
    await bot.send_message(chat_id=-1001900122101, text=log)


if __name__ == '__main__':
    backgroud.keep_alive()
    executor.start_polling(dp, skip_updates=True)
