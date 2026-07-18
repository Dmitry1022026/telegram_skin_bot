import asyncio
import os
import random
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ===== ТОКЕН =====
BOT_TOKEN = os.getenv("8829428365:AAFooImya094bFTyDALCX9sfUa0PODPJWXY")
if not BOT_TOKEN:
    print("❌ Токен не найден! Добавьте BOT_TOKEN в переменные Railway.")
    sys.exit(1)
# =================

# --- ПРОМОКОДЫ ---
PROMO_CODES = [
    "SPIDERCOLA",
    "TWEETROBLOX",
    "DIY",
    "GETMOVING",
    "SETTINGTHESTAGE",
    "STRIKEAPOSE",
    "VICTORYLAP",
    "WORLDALIVE",
    "BOARDWALK",
    "FXARTIST",
    "GLIMMER",
    "PARTICLEWIZARD",
    "THINGSGOBOOM",
    "ROSSMANNSPRING26",
    "ROBLOXATHLETES"
]

INSTRUCTION = (
    "Чтобы активировать промокод в Roblox:\n"
    "1️⃣ Перейди по ссылке: https://www.roblox.com/redeem\n"
    "2️⃣ Введи код в поле\n"
    "3️⃣ Нажми кнопку «Redeem»\n\n"
    "⚠️ Промокоды действуют ограниченное время!\n"
    "Вводи их как можно скорее, чтобы не упустить награду."
)

# ТЕКСТ ДЛЯ РАЗРАБОТЧИКА (изменён)
SUPPORT_TEXT = (
    "📞 По всем вопросам пиши разработчику:\n"
    "👤 @Dmitry102_0\n\n"
    "Нажми кнопку ниже, чтобы сразу написать ему в Telegram."
)

# --- КЛАВИАТУРЫ ---
def get_main_keyboard():
    buttons = [
        [InlineKeyboardButton(text="🎁 Все промокоды", callback_data="show_promos")],
        [InlineKeyboardButton(text="🎲 Случайный код", callback_data="random_promo")],
        [InlineKeyboardButton(text="❓ Инструкция", callback_data="show_instruction")],
        [InlineKeyboardButton(text="📞 Написать разработчику", callback_data="show_support")]  # изменено
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_copy_keyboard():
    buttons = [
        [InlineKeyboardButton(text="📋 Скопировать все", callback_data="copy_all")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_support_keyboard():
    buttons = [
        [InlineKeyboardButton(text="✉️ Написать разработчику", url="https://t.me/Dmitry102_0")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот с актуальными промокодами для Roblox.\n"
        "Выбери нужный раздел:",
        reply_markup=get_main_keyboard()
    )

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    data = callback.data

    if data == "show_promos":
        promo_list = "\n".join([f"• {code}" for code in PROMO_CODES])
        await callback.message.answer(
            f"🎁 Все актуальные промокоды (Июль 2026):\n\n{promo_list}\n\n"
            "Нажми «Скопировать все», чтобы получить отдельное сообщение только с кодами.",
            reply_markup=get_copy_keyboard()
        )
        await callback.answer()

    elif data == "random_promo":
        random_code = random.choice(PROMO_CODES)
        await callback.message.answer(
            f"🎲 Случайный промокод:\n\n`{random_code}`\n\n"
            "Просто нажми на код → «Копировать».\n"
            "Активируй на https://www.roblox.com/redeem",
            parse_mode="MarkdownV2"
        )
        await callback.answer()

    elif data == "copy_all":
        codes_text = "\n".join(PROMO_CODES)
        await callback.message.answer(
            f"📋 Скопируй коды ниже:\n\n{codes_text}\n\n"
            "Просто нажми на сообщение → «Копировать»."
        )
        await callback.answer()

    elif data == "show_instruction":
        await callback.message.answer(INSTRUCTION)
        await callback.answer()

    elif data == "show_support":
        await callback.message.answer(
            SUPPORT_TEXT,
            reply_markup=get_support_keyboard()
        )
        await callback.answer()

    else:
        await callback.answer()

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
