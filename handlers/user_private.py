from aiogram import types, Router,F
from aiogram.filters import CommandStart, Command, or_f

user_private_router = Router()
from kbds import reply

@user_private_router.message(CommandStart()) # старт
async def start_cmd(message: types.Message):
    await message.answer('Привет! Давай начнём работу!',reply_markup=reply.start_kb)

@user_private_router.message(or_f(Command('menu'),(F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer('Давай приступим!!!',reply_markup=reply.menu_kb)

@user_private_router.message(or_f(Command('help'),(F.text.lower() == "справка")))
async def help(message: types.Message):
    await message.answer('А мне бы кто помог :(')
   
@user_private_router.message(or_f(Command('donate'),(F.text.contains('Донат'))))
async def donate(message: types.Message):
    await message.answer('Спасибо, что хотите поддержать, но пока что данная функция не работает')

@user_private_router.message(or_f(Command('MidJourney'), (F.text.lower() == "создание фото")))
async def MifJourney(message: types.Message):
    await message.answer('1. DALL·E 3 (OpenAI)')
    await message.answer(
        'DALL·E 3 — мощная нейросеть от OpenAI, которая генерирует изображения по текстовым описаниям. Она известна своей способностью создавать креативные и реалистичные изображения.'
    )
    await message.answer('Ссылка: https://openai.com/dall-e')

    await message.answer('2. Stable Diffusion')
    await message.answer(
        'Stable Diffusion — нейросеть с открытым исходным кодом, которая позволяет генерировать изображения на основе текстовых запросов. Она популярна благодаря своей гибкости и возможности локальной установки.'
    )
    await message.answer('Ссылка: https://stability.ai/stable-diffusion')

    await message.answer('3. MidJourney')
    await message.answer(
        'MidJourney — одна из самых популярных нейросетей для генерации изображений. Она создаёт высококачественные и художественные изображения по текстовым запросам.'
    )
    await message.answer('Ссылка: https://www.midjourney.com')
