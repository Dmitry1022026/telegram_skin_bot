import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ===== ВСТАВЬ СВОЙ НОВЫЙ ТОКЕН =====
BOT_TOKEN = "8829428365:AAFooImya094bFTyDALCX9sfUa0PODPJWXY"
# ====================================

# --- БАЗА ССЫЛОК (замени на свои) ---
SKINS = {
    "Одежда": [
        "https://www.roblox.com/catalog/123456789/Футболка-пример",
        "https://www.roblox.com/catalog/987654321/Штаны-пример"
    ],
    "Аксессуары": [
        "https://www.roblox.com/catalog/111111111/Шляпа-пример"
    ],
    "Эмоции": [
        "https://www.roblox.com/catalog/333333333/Эмоция-пример"
    ]
}

ALL_SKINS = [link for sub in SKINS.values() for link in sub]

def get_keyboard():
    buttons = []
    for cat in SKINS.keys():
        buttons.append([InlineKeyboardButton(text=cat, callback_data=f"cat_{cat}")])
    buttons.append([InlineKeyboardButton(text="🎲 Случайный скин", callback_data="random")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот для бесплатных скинов в Roblox.\n"
        "Выбери категорию или нажми «Случайный скин»:",
        reply_markup=get_keyboard()
    )

@dp.message(Command("get_skin"))
async def get_skin(message: types.Message):
    if not ALL_SKINS:
        await message.answer("Список пуст, добавь ссылки.")
        return
    link = random.choice(ALL_SKINS)
    await message.answer(f"🎁 Вот ссылка:\n{link}")

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    data = callback.data
    if data.startswith("cat_"):
        category = data[4:]
        links = SKINS.get(category, [])
        if not links:
            await callback.answer("В этой категории нет ссылок", show_alert=True)
            return
        link = random.choice(links)
        await callback.message.answer(f"🎁 Скин из категории «{category}»:\n{link}")
        await callback.answer()
    elif data == "random":
        if not ALL_SKINS:
            await callback.answer("Список пуст", show_alert=True)
            return
        link = random.choice(ALL_SKINS)
        await callback.message.answer(f"🎲 Случайный скин:\n{link}")
        await callback.answer()

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
