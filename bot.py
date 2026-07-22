import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ===== ВСТАВЬ СВОЙ ТОКЕН ОТ @BotFather =====
BOT_TOKEN = "8829428365:AAFooImya094bFTyDALCX9sfUa0PODPJWXY"
# ============================================

# ===== ТВОЙ TELEGRAM USERNAME =====
DEVELOPER = "@Dmitry102_0"
# ===================================

# --- ПРОМОКОДЫ (актуальные) ---
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

# --- ИНСТРУКЦИЯ ---
INSTRUCTION = (
    "📖 **Как активировать промокод в Roblox:**\n\n"
    "1️⃣ Перейди по ссылке: https://www.roblox.com/redeem\n"
    "2️⃣ Введи код в поле\n"
    "3️⃣ Нажми кнопку «Redeem»\n\n"
    "⚠️ Промокоды действуют ограниченное время!\n"
    "Вводи их как можно скорее, чтобы не упустить награду."
)

# --- КЛАВИАТУРЫ ---
def get_main_keyboard():
    buttons = [
        [InlineKeyboardButton(text="🎁 Промокоды", callback_data="show_promos")],
        [InlineKeyboardButton(text="❓ Инструкция", callback_data="show_instruction")],
        [InlineKeyboardButton(text="📩 Написать разработчику", url=f"https://t.me/{DEVELOPER.replace('@', '')}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_copy_keyboard():
    buttons = [
        [InlineKeyboardButton(text="📋 Скопировать все", callback_data="copy_all")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# --- ИНИЦИАЛИЗАЦИЯ ---
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
            f"🎁 Актуальные промокоды (Июль 2026):\n\n{promo_list}\n\n"
            "Нажми «Скопировать все», чтобы получить отдельное сообщение только с кодами.",
            reply_markup=get_copy_keyboard()
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

    else:
        await callback.answer()

# --- ЗАПУСК С УДАЛЕНИЕМ ВЕБХУКА ---
async def main():
    bot = Bot(token=BOT_TOKEN)
    
    # 👇 ЭТО ИСПРАВЛЯЕТ ОШИБКУ Conflict
    await bot.delete_webhook(drop_pending_updates=True)
    # ===================================
    
    print("✅ Бот с промокодами запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
