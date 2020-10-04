from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

print_button = KeyboardButton('/print')
copy_button = KeyboardButton('/copy')
scan_button = KeyboardButton('/scan')
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(print_button)
greet_kb.add(copy_button)
greet_kb.add(scan_button)