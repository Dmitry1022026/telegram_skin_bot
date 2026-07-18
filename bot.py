import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8829428365:AAFooImya094bFTyDALCX9sfUa0PODPJWXY"
DEVELOPER = "@Dmitry102_0"  # твой Telegram

PROMO_CODES = [
    "SPIDERCOLA", "TWEETROBLOX", "DIY", "GETMOVING",
    "SETTINGTHESTAGE", "STRIKEAPOSE", "VICTORYLAP",
    "WORLDALIVE", "BOARDWALK", "FXARTIST", "GLIMMER",
    "PARTICLEWIZARD", "THINGSGOBOOM", "ROSSMANNSPRING26",
    "ROBLOXATHLETES"
]

INSTRUCTION = (
    "Чтобы активировать промокод в Roblox:\n"
    "1️⃣ Перейди по ссылке: https://www.roblox.com/redeem\n"
    "2️⃣ Введи код\n"
    "3️⃣ Нажми «Redeem»\n\n"
    "⚠️ Промокоды действуют ограниченное время!"
)

def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Промокоды", callback_data="show_promos")],
        [InlineKeyboardButton(text="❓ Инструкция", callback_data="show_instruction")],
        [InlineKeyboardButton(text="📩 Написать разработчику", url=f"https://t.me/{DEVELOPER.replace('@', '')}")]
    ])

def get_copy_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Скопировать все", callback_data="copy_all")]
    ])

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот с промокодами для Roblox.\n"  # ← здесь меняй текст
        "Выбери раздел:",
        reply_markup=get_main_keyboard()
    )

@dp.callback_query()
async def handle(callback: types.CallbackQuery):
    data = callback.data
    if data == "show_promos":
        promo_list = "\n".join([f"• {code}" for code in PROMO_CODES])
        await callback.message.answer(
            f"🎁 Промокоды:\n\n{promo_list}",
            reply_markup=get_copy_keyboard()
        )
    elif data == "copy_all":
        await callback.message.answer(
            "📋 Скопируй:\n\n" + "\n".join(PROMO_CODES)
        )
    elif data == "show_instruction":
        await callback.message.answer(INSTRUCTION)
    await callback.answer()

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
