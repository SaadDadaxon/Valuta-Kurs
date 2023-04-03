from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Valuta Kurslar"),
            KeyboardButton(text="📌Manzil", request_location=True),
            KeyboardButton(text="Bot Yaratuvchisi"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
