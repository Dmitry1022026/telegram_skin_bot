import asyncio
import os
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ============== ОТЛАДКА: проверяем, что видит переменную ==============
BOT_TOKEN = os.getenv("AAFooImya094bFTyDALCX9sfUa0PODPJWXY")
print(f"🔍 DEBUG: BOT_TOKEN = {BOT_TOKEN}")  # Если None — переменная не подхватилась

if not BOT_TOKEN:
    print("❌ Ошибка: токен не найден! Добавьте переменную BOT_TOKEN на Railway.")
    sys.exit(1)  # Принудительно завершаем, чтобы логи увидели ошибку
# ======================================================================

# --- ТОЛЬКО ПРОМОКОДЫ И ИНСТРУКЦИЯ ---
CATEGORIES = {
    "🎁 Промокоды": [
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
    ],
    "❓ Инструкция": [
        "Чтобы активировать промокод в Roblox:\n"
        "1️⃣ Перейди по ссылке: https://www.roblox.com/redeem\n"
        "2️⃣ Введи код в поле\n"
        "3️⃣ Нажми кнопку «Redeem»\n\n"
        "⚠️ Промокоды действуют ограниченное время!\n"
        "Вводи их как можно скорее, чтобы не упустить награду."
    ]
}

def get_keyboard():
    buttons = []
    for cat in CATEGORIES.keys():
        buttons.append([InlineKeyboardButton(text=cat, callback_data=f"cat_{cat}")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот с актуальными промокодами для Roblox.\n"
        "Выбери нужный раздел:",
        reply_markup=get_keyboard()
    )

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    data = callback.data
    if data.startswith("cat_"):
        category = data[4:]
        items = CATEGORIES.get(category, [])

        if category == "🎁 Промокоды":
            promo_list = "\n".join([f"• {code}" for code in items])
            await callback.message.answer(
                f"🎁 Актуальные промокоды (Июль 2026):\n\n{promo_list}\n\n"
                "Вводи их на странице: https://www.roblox.com/redeem"
            )
        elif category == "❓ Инструкция":
            await callback.message.answer(items[0])
        else:
            await callback.answer("Раздел временно пуст", show_alert=True)

        await callback.answer()

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
