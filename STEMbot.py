# from aiogram import Bot, Dispatcher, types
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# import asyncio
# import logging
#
# TOKEN = "8070637274:AAHT-UZ_xNSiXd5UMAWHXVo220X67--ZE_Q"
# ADMIN_ID = 191282752
# GROUP_ID = -1002469789522
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# menu_buttons = [
#     [KeyboardButton(text="Учебные программы 🗒️")],
#     [KeyboardButton(text="Предложения и пожелания ✍️")],
#     [KeyboardButton(text="Характеристика ребёнка 📈")]
# ]
# main_menu = ReplyKeyboardMarkup(keyboard=menu_buttons, resize_keyboard=True)
#
#
# class Form(StatesGroup):
#     waiting_for_message = State()
#
#
# @dp.message(Command('start'))
# async def start_handler(message: Message):
#     welcome_text = ("👋 Добро пожаловать в STEM-бот! 🏫\n"
#                     "📚 Этот бот помогает родителям и ученикам.\n\n"
#                     "✨ *Как пользоваться:*\n"
#                     "- 🗒️ *Учебные программы*: Скачайте учебные планы.\n"
#                     "- ✍️ *Предложения* и 📈 *Характеристика*: Отправьте сообщения админу и группе.")
#     await message.answer(welcome_text, reply_markup=main_menu, parse_mode="Markdown")
#
#
# @dp.message(lambda msg: msg.text == "Учебные программы 🗒️")
# async def choose_subject(message: Message):
#     markup = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="📘 STEM", callback_data="subject_STEM")],
#         [InlineKeyboardButton(text="📗 PSHE", callback_data="subject_PSHE")]
#     ])
#     await message.answer("📚 Выберите предмет:", reply_markup=markup)
#
#
# @dp.callback_query(lambda c: c.data.startswith("subject_"))
# async def show_classes(callback: types.CallbackQuery):
#     subject = callback.data.split("_")[1]
#     if subject == "STEM":
#         classes = [f"{i} класс STEM" for i in range(0, 10)]
#     else:
#         classes = [f"{i} класс PSHE" for i in range(5, 10)]
#
#     buttons = [InlineKeyboardButton(text=cls, callback_data=f"class_{cls}") for cls in classes]
#     markup = InlineKeyboardMarkup(inline_keyboard=[[btn] for btn in buttons])
#     await callback.message.edit_text("📚 Выберите класс:", reply_markup=markup)
#
#
# @dp.callback_query(lambda c: c.data.startswith("class_"))
# async def send_class_link(callback: types.CallbackQuery):
#     class_name = callback.data.split("_")[1]
#     links = {
#         '0 класс STEM': 'https://drive.google.com/file/d/10AysxxzZsap6DDtdcFX-Ejk5VqtjohdQ/view?usp=sharing',
#         '1 класс STEM': 'https://drive.google.com/file/d/1y8d_0nrbZ6lB7QjJk88W0ADORDj4UlHY/view?usp=sharing',
#         '2 класс STEM': 'https://drive.google.com/file/d/1zB_i5RojmmcXgoNMVRoXlN7nyCZZn_Mn/view?usp=sharing',
#         '3 класс STEM': 'https://drive.google.com/file/d/1AS-ptHIb0nVVV_TXtzG8G4WDnGc-quii/view?usp=sharing',
#         '4 класс STEM': 'https://drive.google.com/file/d/19uL5T08Wa2iBO7OiqAmcuPnzBLTrGLwS/view?usp=sharing',
#         '5 класс STEM': 'https://drive.google.com/file/d/1Nn6VBVTD39KHO0fmGxsdOFYujprBTPjz/view?usp=sharing',
#         '6 класс STEM': 'https://drive.google.com/file/d/1Ql7kjgRhCWpCcwVHNmPNKvffi3kcxMq1/view?usp=sharing',
#         '7 класс STEM': 'https://drive.google.com/file/d/1hFNrXaqZQwjOYfudTuaJnVnTVUCDeJzq/view?usp=sharing',
#         '8 класс STEM': 'https://drive.google.com/file/d/18rO275lgM0x9qrjIBDk1XiBt48-0Sfx4/view?usp=sharing',
#         '9 класс STEM': 'https://drive.google.com/file/d/1tVF4eQLomy85sorfGHsLuCfLToRiVClI/view?usp=sharing',
#         '5 класс PSHE': 'https://drive.google.com/file/d/1BVKMhqEbgaytH1He7xE63t84kahVV_gm/view?usp=sharing',
#         '6 класс PSHE': 'https://drive.google.com/file/d/1BNI4OJUdyhSNw9AVG4qrlRr0usQixGO9/view?usp=sharing',
#         '7 класс PSHE': 'https://drive.google.com/file/d/1FX04ezKVxZDplSRoN0IGhOtM3et0c8-M/view?usp=drive_link',
#         '8 класс PSHE': 'https://drive.google.com/file/d/174OHI_zwc30bvABnVcPROu-HEhXx7Q4X/view?usp=drive_link',
#         '9 класс PSHE': 'https://drive.google.com/file/d/1U20ERIIS8dbYJoA0gjDuyPNsTT7Pm2Vt/view?usp=sharing'
#     }
#     link = links.get(class_name, "Ссылка не найдена.")
#     await callback.message.answer(f"📥 {class_name}: {link}")
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# import asyncio
# import logging

# TOKEN = "8070637274:AAHT-UZ_xNSiXd5UMAWHXVo220X67--ZE_Q"
# ADMIN_ID = 191282752
# GROUP_ID = -1002469789522
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# menu_buttons = [
#     [KeyboardButton(text="Учебные программы 🗒️")],
#     [KeyboardButton(text="Предложения и пожелания ✍️")],
#     [KeyboardButton(text="Характеристика ребёнка 📈")]
# ]
# main_menu = ReplyKeyboardMarkup(keyboard=menu_buttons, resize_keyboard=True)
#
#
# class Form(StatesGroup):
#     waiting_for_message = State()
#
#
# @dp.message(Command('start'))
# async def start_handler(message: Message):
#     welcome_text = ("👋 Добро пожаловать в STEM-бот! 🏫\n"
#                     "📚 Этот бот помогает родителям и ученикам.\n\n"
#                     "✨ *Как пользоваться:*\n"
#                     "- 🗒️ *Учебные программы*: Скачайте учебные планы.\n"
#                     "- ✍️ *Предложения* и 📈 *Характеристика*: Отправьте сообщения админу и группе.")
#     await message.answer(welcome_text, reply_markup=main_menu, parse_mode="Markdown")
#
#
# @dp.message(lambda msg: msg.text == "Учебные программы 🗒️")
# async def choose_subject(message: Message):
#     markup = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="📘 STEM", callback_data="subject_STEM")],
#         [InlineKeyboardButton(text="📗 PSHE", callback_data="subject_PSHE")]
#     ])
#     await message.answer("📚 Выберите предмет:", reply_markup=markup)
#
#
# @dp.message(lambda msg: msg.text == "Предложения и пожелания ✍️" or msg.text == "Характеристика ребёнка 📈")
# async def forward_message(message: Message):
#     try:
#         forward_text = f"📩 Новое сообщение от {message.from_user.full_name} (@{message.from_user.username}):\n\n{message.text}"
#         await bot.send_message(GROUP_ID, forward_text)
#         await message.answer("✅ Ваше сообщение отправлено в группу.")
#     except Exception as e:
#         logger.error(f"Ошибка отправки сообщения: {e}")
#         await message.answer("❌ Ошибка при отправке сообщения.")
#
#
# @dp.callback_query(lambda c: c.data.startswith("subject_"))
# async def show_classes(callback: types.CallbackQuery):
#     subject = callback.data.split("_")[1]
#     if subject == "STEM":
#         classes = [f"{i} класс STEM" for i in range(0, 10)]
#     else:
#         classes = [f"{i} класс PSHE" for i in range(5, 10)]
#
#     buttons = [InlineKeyboardButton(text=cls, callback_data=f"class_{cls}") for cls in classes]
#     markup = InlineKeyboardMarkup(inline_keyboard=[[btn] for btn in buttons])
#     await callback.message.edit_text("📚 Выберите класс:", reply_markup=markup)
#
#
# @dp.callback_query(lambda c: c.data.startswith("class_"))
# async def send_class_link(callback: types.CallbackQuery):
#     class_name = callback.data.split("_")[1]
#     links = {
#         '0 класс STEM': 'https://drive.google.com/file/d/10AysxxzZsap6DDtdcFX-Ejk5VqtjohdQ/view?usp=sharing',
#         '1 класс STEM': 'https://drive.google.com/file/d/1y8d_0nrbZ6lB7QjJk88W0ADORDj4UlHY/view?usp=sharing',
#         '2 класс STEM': 'https://drive.google.com/file/d/1zB_i5RojmmcXgoNMVRoXlN7nyCZZn_Mn/view?usp=sharing',
#         '3 класс STEM': 'https://drive.google.com/file/d/1AS-ptHIb0nVVV_TXtzG8G4WDnGc-quii/view?usp=sharing',
#         '4 класс STEM': 'https://drive.google.com/file/d/19uL5T08Wa2iBO7OiqAmcuPnzBLTrGLwS/view?usp=sharing',
#         '5 класс STEM': 'https://drive.google.com/file/d/1Nn6VBVTD39KHO0fmGxsdOFYujprBTPjz/view?usp=sharing',
#         '6 класс STEM': 'https://drive.google.com/file/d/1Ql7kjgRhCWpCcwVHNmPNKvffi3kcxMq1/view?usp=sharing',
#         '7 класс STEM': 'https://drive.google.com/file/d/1hFNrXaqZQwjOYfudTuaJnVnTVUCDeJzq/view?usp=sharing',
#         '8 класс STEM': 'https://drive.google.com/file/d/18rO275lgM0x9qrjIBDk1XiBt48-0Sfx4/view?usp=sharing',
#         '9 класс STEM': 'https://drive.google.com/file/d/1tVF4eQLomy85sorfGHsLuCfLToRiVClI/view?usp=sharing',
#         '5 класс PSHE': 'https://drive.google.com/file/d/1BVKMhqEbgaytH1He7xE63t84kahVV_gm/view?usp=sharing',
#         '6 класс PSHE': 'https://drive.google.com/file/d/1BNI4OJUdyhSNw9AVG4qrlRr0usQixGO9/view?usp=sharing',
#         '7 класс PSHE': 'https://drive.google.com/file/d/1FX04ezKVxZDplSRoN0IGhOtM3et0c8-M/view?usp=drive_link',
#         '8 класс PSHE': 'https://drive.google.com/file/d/174OHI_zwc30bvABnVcPROu-HEhXx7Q4X/view?usp=drive_link',
#         '9 класс PSHE': 'https://drive.google.com/file/d/1U20ERIIS8dbYJoA0gjDuyPNsTT7Pm2Vt/view?usp=sharing'
#     }
#     link = links.get(class_name, "Ссылка не найдена.")
#     await callback.message.answer(f"📥 {class_name}: {link}")
#
#
# async def main():
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import asyncio
import logging

TOKEN = "8070637274:AAHT-UZ_xNSiXd5UMAWHXVo220X67--ZE_Q"
ADMIN_ID = 191282752
GROUP_ID = -1002469789522

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu_buttons = [
    [KeyboardButton(text="Учебные программы 🗒️")],
    [KeyboardButton(text="Предложения и пожелания ✍️")],
    [KeyboardButton(text="Характеристика ребёнка 📈")]
]
main_menu = ReplyKeyboardMarkup(keyboard=menu_buttons, resize_keyboard=True)


class Form(StatesGroup):
    waiting_for_message = State()


@dp.message(Command('start'))
async def start_handler(message: Message):
    welcome_text = ("👋 Добро пожаловать в STEM-бот! 🏫\n"
                    "📚 Этот бот помогает родителям и ученикам.\n\n"
                    "✨ *Как пользоваться:*\n"
                    "- 🗒️ *Учебные программы*: Скачайте учебные планы.\n"
                    "- ✍️ *Предложения* и 📈 *Характеристика*: Отправьте сообщения админу и группе.")
    await message.answer(welcome_text, reply_markup=main_menu, parse_mode="Markdown")


@dp.message(lambda msg: msg.text == "Учебные программы 🗒️")
async def choose_subject(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📘 STEM", callback_data="subject_STEM")],
        [InlineKeyboardButton(text="📗 PSHE", callback_data="subject_PSHE")]
    ])
    await message.answer("📚 Выберите предмет:", reply_markup=markup)


@dp.message(lambda msg: msg.text in ["Предложения и пожелания ✍️", "Характеристика ребёнка 📈"])
async def request_message(message: Message, state: FSMContext):
    await state.set_state(Form.waiting_for_message)
    await message.answer("📝 Пожалуйста, введите ваше сообщение, и оно будет отправлено в группу.")


@dp.message(Form.waiting_for_message)
async def forward_user_message(message: Message, state: FSMContext):
    try:
        await bot.send_message(GROUP_ID,
                               f"📩 Сообщение от {message.from_user.full_name} (@{message.from_user.username}):\n\n{message.text}")
        await message.answer("✅ Ваше сообщение отправлено в группу.")
    except Exception as e:
        logger.error(f"Ошибка отправки сообщения: {e}")
        await message.answer("❌ Ошибка при отправке сообщения.")
    finally:
        await state.clear()


@dp.callback_query(lambda c: c.data.startswith("subject_"))
async def show_classes(callback: types.CallbackQuery):
    subject = callback.data.split("_")[1]
    if subject == "STEM":
        classes = [f"{i} класс STEM " for i in range(0, 10)]
    else:
        classes = [f"{i} класс PSHE" for i in range(5, 10)]

    buttons = [InlineKeyboardButton(text=cls, callback_data=f"class_{cls}") for cls in classes]
    markup = InlineKeyboardMarkup(inline_keyboard=[[btn] for btn in buttons])
    await callback.message.edit_text("📚 Выберите класс:", reply_markup=markup)


@dp.callback_query(lambda c: c.data.startswith("class_"))
async def send_class_link(callback: types.CallbackQuery):
    class_name = callback.data.split("_")[1]
    links = {
            '0 класс STEM': 'https://drive.google.com/file/d/10AysxxzZsap6DDtdcFX-Ejk5VqtjohdQ/view?usp=sharing',
            '1 класс STEM': 'https://drive.google.com/file/d/1y8d_0nrbZ6lB7QjJk88W0ADORDj4UlHY/view?usp=sharing',
            '2 класс STEM': 'https://drive.google.com/file/d/1zB_i5RojmmcXgoNMVRoXlN7nyCZZn_Mn/view?usp=sharing',
            '3 класс STEM': 'https://drive.google.com/file/d/1AS-ptHIb0nVVV_TXtzG8G4WDnGc-quii/view?usp=sharing',
            '4 класс STEM': 'https://drive.google.com/file/d/19uL5T08Wa2iBO7OiqAmcuPnzBLTrGLwS/view?usp=sharing',
            '5 класс STEM': 'https://drive.google.com/file/d/1Nn6VBVTD39KHO0fmGxsdOFYujprBTPjz/view?usp=sharing',
            '6 класс STEM': 'https://drive.google.com/file/d/1Ql7kjgRhCWpCcwVHNmPNKvffi3kcxMq1/view?usp=sharing',
            '7 класс STEM': 'https://drive.google.com/file/d/1hFNrXaqZQwjOYfudTuaJnVnTVUCDeJzq/view?usp=sharing',
            '8 класс STEM': 'https://drive.google.com/file/d/18rO275lgM0x9qrjIBDk1XiBt48-0Sfx4/view?usp=sharing',
            '9 класс STEM': 'https://drive.google.com/file/d/1tVF4eQLomy85sorfGHsLuCfLToRiVClI/view?usp=sharing',
            '5 класс PSHE': 'https://drive.google.com/file/d/1BVKMhqEbgaytH1He7xE63t84kahVV_gm/view?usp=sharing',
            '6 класс PSHE': 'https://drive.google.com/file/d/1BNI4OJUdyhSNw9AVG4qrlRr0usQixGO9/view?usp=sharing',
            '7 класс PSHE': 'https://drive.google.com/file/d/1FX04ezKVxZDplSRoN0IGhOtM3et0c8-M/view?usp=drive_link',
            '8 класс PSHE': 'https://drive.google.com/file/d/174OHI_zwc30bvABnVcPROu-HEhXx7Q4X/view?usp=drive_link',
            '9 класс PSHE': 'https://drive.google.com/file/d/1U20ERIIS8dbYJoA0gjDuyPNsTT7Pm2Vt/view?usp=sharing'
        }
    link = links.get(class_name, "Ссылка не найдена.")
    await callback.message.answer(f"📥 {class_name}: {link}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())