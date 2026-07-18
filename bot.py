import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8829428365:AAFooImya094bFTyDALCX9sfUa0PODPJWXY"
DEVELOPER = "@Dmitry102_0"

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
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎁 Промокоды")],
            [KeyboardButton(text="❓ Инструкция")],
            [KeyboardButton(text="📩 Написать разработчику")]
        ],
        resize_keyboard=True,
        is_persistent=True
    )

def get_copy_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Скопировать все", callback_data="copy_all")]
    ])

dp = Dispatcher()

# ========== КОМАНДЫ ==========
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот с промокодами для Roblox.",
        reply_markup=get_main_keyboard()
    )

@dp.message(Command("promos"))
async def promos_command(message: types.Message):
    promo_list = "\n".join([f"• {code}" for code in PROMO_CODES])
    await message.answer(
        f"🎁 Промокоды:\n\n{promo_list}",
        reply_markup=get_copy_keyboard()
    )

@dp.message(Command("instruction"))
async def instruction_command(message: types.Message):
    await message.answer(INSTRUCTION)

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "📋 Доступные команды:\n"
        "/start — главное меню\n"
        "/promos — промокоды\n"
        "/instruction — инструкция\n"
        "/help — это сообщение\n\n"
        "Или просто пользуйся кнопками внизу 👇"
    )

# ========== КНОПКИ ==========
@dp.message(lambda message: message.text == "🎁 Промокоды")
async def show_promos(message: types.Message):
    promo_list = "\n".join([f"• {code}" for code in PROMO_CODES])
    await message.answer(
        f"🎁 Промокоды:\n\n{promo_list}",
        reply_markup=get_copy_keyboard()
    )

@dp.message(lambda message: message.text == "❓ Инструкция")
async def show_instruction(message: types.Message):
    await message.answer(INSTRUCTION)

@dp.message(lambda message: message.text == "📩 Написать разработчику")
async def contact_developer(message: types.Message):
    await message.answer(f"👨‍💻 Свяжись с разработчиком: {DEVELOPER}")

# ========== INLINE ==========
@dp.callback_query()
async def handle_copy(callback: types.CallbackQuery):
    if callback.data == "copy_all":
        await callback.message.answer(
            "📋 Скопируй:\n\n" + "\n".join(PROMO_CODES)
        )
        await callback.answer()

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
