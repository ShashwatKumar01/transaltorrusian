
import asyncio

from pyrogram import Client, filters, enums
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
import logging
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import errors
from quart import Quart
from googletrans import Translator


api_id = '26566076'
api_hash = '40ce27837b95819c42cac67b46a2dc2b'
bot_token='7132391493:AAEYNvmCqcjtKy-3CwenJBTiIysXp0El0jo'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

bot = Quart(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

translator = Translator()

@bot.route('/')
async def hello():
    return 'Hello, world!'


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("Send me Russian Lang")

# Pyrogram text translation handler
@app.on_message(filters.text)
async def translate_text_message(client, message):
    translated_text = translator.translate(message.text, src='ru', dest='en').text
    await message.reply(text=translated_text)

async def translate_caption(caption):
    if caption:
        return translator.translate(caption, src='ru', dest='en').text
    return None

@app.on_message(filters.media)
async def translate_media_message(client, message):
    translated_caption = await translate_caption(message.caption)

    if message.photo:
        await message.reply_photo(
            photo=message.photo.file_id,
            caption=translated_caption
        )
    elif message.video:
        await message.reply_video(
            video=message.video.file_id,
            caption=translated_caption
        )
    elif message.document:
        await message.reply_document(
            document=message.document.file_id,
            caption=translated_caption
        )
    elif message.audio:
        await message.reply_audio(
            audio=message.audio.file_id,
            caption=translated_caption
        )
    elif message.voice:
        await message.reply_voice(
            voice=message.voice.file_id,
            caption=translated_caption
        )
    else:
        logger.warning(f"Unsupported media type: {message.media}")


@bot.before_serving
async def before_serving():
    await app.start()


@bot.after_serving
async def after_serving():
    await app.stop()


# if __name__ == '__main__':

# bot.run(port=8000)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(bot.run_task(host='0.0.0.0', port=8080))
    loop.run_forever()

