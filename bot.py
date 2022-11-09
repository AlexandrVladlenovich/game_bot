#Здесь создается бот и хранится его токен

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import Dispatcher


bot = Bot(token='5638213201:AAHIY8IcASm_AuuqykFB0XckiEpEbI-d_20')
# программа - слушаетель - ждет сообщения и принимает
dp = Dispatcher(bot)