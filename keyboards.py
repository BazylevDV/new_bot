from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

def get_main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
        [KeyboardButton(text="Каталог оборудования🗂️"), KeyboardButton(text="Склад на сегодня💒")],
        [KeyboardButton(text="Успей купить по акции-1☎️"), KeyboardButton(text="Успей купить по акции-2☎️")],
        [KeyboardButton(text="Запросить КП🖊️"), KeyboardButton(text="Информация📝")]
    ])
    return keyboard

def back_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад👈", callback_data="back")]
    ])
    return keyboard

def reminder_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Продолжить", callback_data="continue")],
        [InlineKeyboardButton(text="Завершить сеанс", callback_data="finish")]
    ])
    return keyboard

def manager_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Дружинина  Татьяна ️", callback_data="Дружинина Татьяна")],
        [InlineKeyboardButton(text="Ковач Александр", callback_data="Ковач Александр")]
    ])
    return keyboard

def restart_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Продолжить", callback_data="continue_kp")],
        [InlineKeyboardButton(text="Начать заново", callback_data="restart_kp")]
    ])
    return keyboard

def subscribe_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на бота👌", url="https://t.me/LabDealsBot")]
    ])
    return keyboard

def admin_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Пользователи 🧑‍💻 ", callback_data="users")],
        [InlineKeyboardButton(text="Статистика 📊", callback_data="stats")],
        [InlineKeyboardButton(text="Блокировка 🔐", callback_data="block")],
        [InlineKeyboardButton(text="Разблокировка 🗝️" , callback_data="unblock")],
        [InlineKeyboardButton(text="Рассылка 📤", callback_data="broadcast")]  # Новая кнопка
    ])
    return keyboard