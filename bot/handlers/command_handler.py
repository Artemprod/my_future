import random

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.lexicon.navigation import  start_nav

# from bot.keyboards.inline_keyboards import crete_inline_keyboard_options

router = Router()


@router.message(CommandStart(), )
async def process_start_command(message: Message):
    # option_keyboard = crete_inline_keyboard_options()
    await message.answer(text=random.choice(start_nav))
