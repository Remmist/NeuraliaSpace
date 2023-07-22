import os
import random
import re

from aiogram import Bot, Dispatcher, executor, types

import backgroud
from alphabet import translate, retranslate, getAlphabet
from engine import GenerateMessage, isEnoughData, saveData
from smart import GenerateAnswer
from sticker import get_stickers

NeuraliaToken = os.environ['NeuraliaToken']
bot = Bot(token=NeuraliaToken)
dp = Dispatcher(bot)

stickers = get_stickers()


@dp.message_handler()
async def echo(message: types.Message):
    # IF THIS MESSAGE WAS FORWARD FROM ANOTHER CHAT, THEN IGNORE THIS MESSAGE
    if message.is_forward():
        return

    # START MESSAGE FOR NEW USERS
    if message.text == '/start' or message.text == '/help' or message.text == 'help' or message.text == 'start':
        hello = open('hello.txt', 'r', encoding='utf8').read()
        await message.reply(hello)
        return

    if message.text.startswith('@NeuraliaRemmy_bot'):
        # LIST OF COMMANDS
        if message.text.startswith('@NeuraliaRemmy_bot что ты умеешь'):
            await message.reply(
                'Я умею следующее:\n·say <количество слов или large (l), small (s), medium (m)>\n·отправь стикер\n·кто тебя создал\n·переведи на уэайжо <текст>\n·переведи c уэайжо <текст>\n·покажи алфавит')
            return

        # SEND УЭАЙЖО ALPHABET
        if message.text.startswith('@NeuraliaRemmy_bot покажи алфавит'):
            text = getAlphabet()
            await message.reply(text)
            return

        # TRANSLATE TEXT TO УЭАЙЖО LANGUAGE
        if message.text.startswith('@NeuraliaRemmy_bot переведи на уэайжо'):
            text = message.text.replace('@NeuraliaRemmy_bot переведи на уэайжо ', '')
            inf = [text]
            await message.reply(translate(inf))
            return

        # TRANSLATE TEXT FROM УЭАЙЖО LANGUAGE
        if message.text.startswith('@NeuraliaRemmy_bot переведи с уэайжо'):
            text = message.text.replace('@NeuraliaRemmy_bot переведи с уэайжо ', '')
            await message.reply(retranslate(text))
            return

        # CREATOR INFO
        if message.text.startswith('@NeuraliaRemmy_bot кто тебя создал'):
            await message.reply(
                'Я была создана руками @raiseeve, если вдруг со мной что-то не так, то сообщите ему!')
            return

        # SEND STICKER
        if message.text.startswith('@NeuraliaRemmy_bot отправь стикер'):
            await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
            return

        # GENERATING REQUESTED MESSAGE
        if message.text.startswith('@NeuraliaRemmy_bot say'):
            text = message.text.split(' ')
            length = 0

            if text[2].lower() == 'l' or text[2].lower() == 'm' or text[2].lower() == 's' or text[
                2].lower() == 'large' or \
                    text[2].lower() == 'medium' or text[2].lower() == 'small':
                if text[2].lower() == 's' or text[2].lower() == 'small':
                    length = random.randint(5, 15)
                if text[2].lower() == 'm' or text[2].lower() == 'medium':
                    length = random.randint(20, 30)
                if text[2].lower() == 'l' or text[2].lower() == 'large':
                    length = random.randint(35, 50)
            else:
                if int(text[2]) > 200:
                    await message.reply('Слишком большое сообщение для генерации. Пожалуйста введите число меньше')
                    return
                if int(text[2]) <= 1:
                    await message.reply(
                        'Слишком маленькое сообщение для генерации. Пожалуйста введите число больше')
                    return
                length = int(text[2])

            if not isEnoughData(str(message.chat.id) + '.txt'):
                await message.reply('Недостаточно данных для генерации сообщения.')
                return

            rnd = random.randint(0, 4)
            if rnd == 0:
                await message.reply(GenerateMessage(str(message.chat.id) + '.txt', length - 1).upper())
                return
            else:
                await message.reply(GenerateMessage(str(message.chat.id) + '.txt', length - 1).capitalize())
            return

        # IF MESSAGE CONTAINS COMMAND, THAT DOESNT EXISTS, THEN JUXT IGNORE THIS MESSAGE
        if message.text.startswith('N') or message.text.startswith('n'):
            return

        # SEND SMART ANSWER
        text = message.text.replace('@NeuraliaRemmy_bot', '')
        answ = GenerateAnswer(text)
        await message.reply(answ)
        return

    # SEND CHANGELOG COMMAND
    if message.text.startswith('N отправь ченж'):
        if message.from_user.id == 575213063:  # CREATOR ID
            await sayChangelog()
        else:
            await message.reply('У тебя нет прав на выполнение данной команды!')
        return

    # REGEX CLEAR URL FROM MESSAGE
    msg = re.sub(
        r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})',
        '', message.text, flags=re.MULTILINE)
    msg = re.sub(r'(А+Х+)+', '', msg, flags=re.MULTILINE)
    msg = re.sub(r'(а+х+)+', '', msg, flags=re.MULTILINE)
    msg = re.sub(r'(Х+А+)+', '', msg, flags=re.MULTILINE)
    msg = re.sub(r'(х+а+)+', '', msg, flags=re.MULTILINE)
    msg = re.sub(r'@NeuraliaRemmy_bot', '', msg, flags=re.MULTILINE)

    # SAVING MESSAGE
    if msg != ' ' or msg != '' or msg.__len__() != 1 or msg.__len__() != 0:
        saveData(str(message.chat.id) + '.txt', msg)

    # GENERATING NEW MESSAGE TO CHAT
    if random.randint(0, 100) >= 80:

        # OLD METHOD TO GENERATE MESSAGES

        # if not isEnoughData(str(message.chat.id) + '.txt'):
        #     return

        # rnd = random.randint(0, 4)
        # if rnd == 0:
        #     await message.answer(GenerateMessage(str(message.chat.id) + '.txt', random.randint(0, 10)).upper())
        #     if random.randint(0, 100) > 60:
        #         await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
        #     return
        # elif rnd == 1:
        #     await message.answer(msg)
        #     if random.randint(0, 100) > 60:
        #         await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
        #     return
        # else:
        #     await message.answer(GenerateMessage(str(message.chat.id) + '.txt', random.randint(0, 10)).capitalize())
        #     if random.randint(0, 100) > 60:
        #         await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
        #     return

        rnd = random.randint(0, 4)
        if rnd == 0:
            await message.answer(GenerateAnswer(message.text).upper())
            if random.randint(0, 100) > 60:
                await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
            return
        elif rnd == 1:
            await message.answer(msg)
            if random.randint(0, 100) > 60:
                await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
            return
        else:
            await message.answer(GenerateAnswer(message.text))
            if random.randint(0, 100) > 60:
                await bot.send_sticker(chat_id=message.chat.id, sticker=random.choice(stickers))
            return


# METHOD TO CHECK BOT STATUS FOR FLASK SERVER
def bot_check():
    return bot.get_me()


# METHOD TO SEND CHANGELOG IN CHAT
async def sayChangelog():
    log = open('changelog.txt', 'r', encoding='utf8').read()
    project_directory = os.getcwd()
    chats_directory = os.path.join(project_directory, 'chats')
    file_list = os.listdir(chats_directory)
    txt_files = [file for file in file_list if file.endswith('.txt')]
    for chat in txt_files:
        await bot.send_message(chat_id=str(chat), text=log)


if __name__ == '__main__':
    backgroud.keep_alive()
    executor.start_polling(dp, skip_updates=True)
