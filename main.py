import os
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv

# .env faylni yuklaymiz
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Start komandasi
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(
        "👋 Salom! Bu Soft mahsulotlari savdo botiga xush kelibsiz!\n\n"
        "📦 Mahsulot nomi: Soft Men Spray\n"
        "💧 Hajmi: 20 ml\n"
        "💰 Narxi: 119 000 so‘m\n\n"
        "📸 Rasm quyida 👇"
    )
    await message.answer_photo(
        photo='https://i.imgur.com/yV7bJ1B.jpeg',
        caption="🧴 Soft Men Spray — 20ml | 119 000 so‘m\n\n📞 Buyurtma uchun bog‘laning!"
    )

# Xatoliklardan himoya
@dp.errors_handler()
async def errors_handler(update, exception):
    print(f"Xatolik: {exception}")
    return True

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
