import telebot
from telebot import types
import time
import cfg
import config
import os
import random


bot = telebot.TeleBot('токен')

def random_name():
	r1 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	r2 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	r3 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	r4 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	r5 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

	code = r1 + r2 + r3 + r4 + r5
	return code

def get_picture(id_picture):
	place = 'picture/' + str(id_picture) + '.jpg'
	picture_place  = open(place, 'rb')
	return picture_place

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
	item1 = types.KeyboardButton('📷Посмотреть пикчи')
	item2 = types.KeyboardButton('🔥Добавить свои пикчи')

	markup.add(item1,item2)
	gg = 'Привет, <b>' + message.from_user.first_name.title() + '</b>!\nМне на тебя абсолютно похуй но если чё это коллекция рарных пикч создателя этого бота\n\nСоздатель - Якублевич Ренат\nGithub - https://github.com/RenatYakublevich'.format(message.from_user, bot.get_me())
	bot.send_message(message.chat.id, gg ,parse_mode='html',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def crypto_price_telegram(message):
	if message.chat.type == 'private':
		if message.text == '📷Посмотреть пикчи':

			bot.send_photo(message.chat.id, get_picture(1))


			markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
			item1 = types.KeyboardButton('❌Предыдущая')
			item2 = types.KeyboardButton('Назад')
			item3 = types.KeyboardButton('✅Следующая')

			markup.add(item1,item2,item3)
			bot.send_message(message.chat.id,'Выбирай варики внизу чертила👇👇',reply_markup=markup)

		if message.text == 'Назад':
			welcome(message)
			cfg.gg = 0

		if message.text == '✅Следующая':
			cfg.gg = cfg.gg + 1
			if cfg.gg > (cfg.picture_list[-1] - 1):
				cfg.gg = 0
			bot.send_photo(message.chat.id,get_picture(cfg.picture_list[cfg.gg]))
			print(cfg.gg)
		if message.text == '❌Предыдущая':
			cfg.gg = cfg.gg - 1
			bot.send_photo(message.chat.id,get_picture(cfg.picture_list[cfg.gg]))
			print(cfg.gg)

		if message.text == '🔥Добавить свои пикчи':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
			item1 = types.KeyboardButton('Назад')

			markup.add(item1)
			bot.send_message(message.chat.id,'Привет! Отправь свою пикчу, я внесу её в коллекцию',reply_markup=markup)

@bot.message_handler(content_types=["photo"],
                     func=lambda message: cfg.get_current_state(message.chat.id) == config.States.S_SEND_PIC.value)

@bot.message_handler(content_types=['photo'])
def photo_img(message):

	try:
		file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		src='picture/moderation/' + random_name() + '.jpg';
		with open(src, 'wb') as new_file:
			new_file.write(downloaded_file)
		bot.reply_to(message,"Фото добавлено в очередь на модерацию,ожидайте!")

	except Exception as e:
		bot.reply_to(message,e )




bot.polling(none_stop=True)
