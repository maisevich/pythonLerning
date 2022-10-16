import random

import telebot

bot = telebot.TeleBot('5783962027:AAHNTNOavWT6BCMr-l8jGTiATWHuo3RShUU')

from telebot import types

first = ["Сегодня — идеальный день для темного лагера"]
second = ["Но помните, что даже в этом случае нужно не забывать про светлный эль"]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно."]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет":

        bot.send_message(message.from_user.id, "*Привет, дорогой любитель пенного!* "
                                               "Этот чат-бот поможет тебе "
                                               "провести сегодняшний день в компании пива Афанасий!")

        keyboard = types.InlineKeyboardMarkup()
        key_maroch = types.InlineKeyboardButton(text='"Марочное" светлое', callback_data='marochnoe_white')
        keyboard.add(key_maroch)
        key_maroch_black = types.InlineKeyboardButton(text='"Марочное" темное', callback_data='marochnoe_black')
        keyboard.add(key_maroch_black)
        key_remeslennoe_white = types.InlineKeyboardButton(text='"Ремесленное" светлое', callback_data='remeslennoe_white')
        keyboard.add(key_remeslennoe_white)
        key_remeslennoe_black = types.InlineKeyboardButton(text='"Ремесленное" темное', callback_data='remeslennoe_black')
        keyboard.add(key_remeslennoe_black)
        key_kraft = types.InlineKeyboardButton(text='"Крафтовое"', callback_data='kraft')
        keyboard.add(key_kraft)
        key_zigul = types.InlineKeyboardButton(text='"Жигулевское"', callback_data='zigul')
        keyboard.add(key_zigul)
        key_dobroe_white = types.InlineKeyboardButton(text='"Афанасий Доброе светлое"', callback_data='dobroe_white')
        keyboard.add(key_dobroe_white)
        key_dobroe_strong = types.InlineKeyboardButton(text='"Афанасий Доброе крепкое"', callback_data='dobroe_strong')
        keyboard.add(key_dobroe_strong)
        key_exper = types.InlineKeyboardButton(text='"Экспериментальное"', callback_data='exper')
        keyboard.add(key_exper)
        key_ecobeer = types.InlineKeyboardButton(text='"ЭкоBeer"', callback_data='ecobeer')
        keyboard.add(key_ecobeer)
        key_nippelale = types.InlineKeyboardButton(text='"NIPPEL STRONG"', callback_data='nippelale')
        keyboard.add(key_nippelale)
        key_nippellager = types.InlineKeyboardButton(text='"NIPPEL LAGER"', callback_data='nippellager')
        keyboard.add(key_nippellager)
        key_tverskoe_small = types.InlineKeyboardButton(text='"Тверское" 0,5 л', callback_data='tverskoe_small')
        keyboard.add(key_tverskoe_small)
        key_tverskoe_big = types.InlineKeyboardButton(text='"Тверское" 1,9 л', callback_data='tverskoe_big')
        keyboard.add(key_tverskoe_big)

        bot.send_message(message.from_user.id, text='Выбери свое пиво', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет'")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "marochnoe_white":

        msg = '*Марочное светлое*\nПиво светлое пастеризованное. Бугель-бутылка 0,5 л, стекло. Состав: питьевая вода, солод пивоваренный ' \
              'ячменный светлый, хмель. Экстрактивность начального сусла: 11 %. ' \
              'Алкоголь: 4,5 % об.'
        bot.send_message(call.message.chat.id, msg)
    if call.data == "marochnoe_black":
        msg =  '*Марочное темное*\nПиво тёмное пастеризованное. Бугель-бутылка 0,5 л., стекло. ' \
               'Состав: питьевая вода, солод пивоваренный ячменный светлый, хмель. ' \
               'Экстрактивность начального сусла: 11 %. Алкоголь: 4,5 % об. '
        bot.send_message(call.message.chat.id, msg)
    if call.data == "remeslennoe_white":
        msg = '*Ремесленное* светлое\nПиво светлое нефильтрованное неосветленное непастеризованное. Бугель-бутылка 1 л., стекло. ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый, хмель. ' \
              'Экстрактивность начального сусла 11%. Алкоголь: 4,5 % об.'

        bot.send_photo(call.message.chat.id, 'http://ремесленноепиво.рф/img/range.png?v=2')
        bot.send_message(call.message.chat.id, msg)
    if call.data == "remeslennoe_black":
        msg = '*Ремесленное* темное\nПиво темное нефильтрованное неосветленное непастеризованное. Бугель-бутылка 1 л., стекло. ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый и жженый, хмель. ' \
              'Экстрактивность начального сусла 11%. Алкоголь: 4,5 % об'

        bot.send_photo(call.message.chat.id, 'http://ремесленноепиво.рф/img/dark.png?v=2')
        bot.send_message(call.message.chat.id, msg)
    if call.data == "kraft":
        msg = '*Крафтовое*\nПиво светлое пастеризованное. Бугель-бутылка 0,75 л., стекло. ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый, хмель, хмелепродукты. ' \
              'Экстрактивность начального сусла: 11 % ' \
              'Алкоголь: 4,5 % об.'
        bot.send_message(call.message.chat.id, msg)
    if call.data == "zigul":
        msg = '*Жигулевское*\nПиво светлое пастеризованное. ПЭТ бутылка 1,5 л. Состав: питьевая вода, солод пивоваренный ячменный светлый, ' \
              'ячмень, хмель. Экстрактивность начального сусла: 11% Алкоголь: 4,5 %. '
        bot.send_message(call.message.chat.id, msg)
    if call.data == "dobroe_white":
        msg = '*Афанасий Доброе Светлое*\nЛегкое пиво с чистым солодовым вкусом и приятной хмельной горчинкой. ' \
              'Пиво светлое пастеризованное. ПЭТ бутылка 1,5 л. ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый, ячмень, хмель. ' \
              'Экстрактивность начального сусла: 11%. Алкоголь: 4,5 % '
        bot.send_message(call.message.chat.id, msg)
    if call.data == "dobroe_strong":
        msg = '*Афанасий Доброе Крепкое*\nПиво светлое пастеризованное. ПЭТ бутылка 1,5 л. Состав: питьевая вода, солод пивоваренный ячменный ' \
              'светлый, хмель. Экстрактивность начального сусла: 16%. Алкоголь: 6,9 %. '
        bot.send_message(call.message.chat.id, msg)
    if call.data == "exper":
        msg = '*Экспериментальное*\nЛегкое пиво высокой плотности, темно-каштанового цвета, ' \
              'который достигается сочетанием нескольких специальных видов жженого солода, ' \
              'с приятной горчинкой, требующей следующего глотка. ' \
              'Пиво тёмное лёгкое пастеризованное. ПЭТ бутылка 1 л. ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый и жжёный, хмель. ' \
              'Экстрактивность начального сусла: 11 % ' \
              'Алкоголь: 4,5 % об.'
        bot.send_message(call.message.chat.id, msg)
    if call.data == "ecobeer":
        msg = '*ЭкоBeer*\nПиво светлое пастеризованное. ПЭТ Бутылка 0,5 л. ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый, ячмень, хмель.' \
              'Экстрактивность начального сусла: 10 % ' \
              'Алкоголь: 4,5 % об. '
        bot.send_message(call.message.chat.id, msg)
    if call.data == "nippelale":
        msg = '*NIPPEL STRONG*\nПивной напиток светлый нефильтрованный неосветленный ' \
              'непастеризованный с возможностью дображивания в бутылке. Упаковка: бутылка 1,4 л, ПЭТ ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый, ячмень, хмель, ' \
              'пищевая добавка - кислота молочная, пивные дрожжи. Алкоголь: не более 0,5% об. '
        bot.send_message(call.message.chat.id, msg)
    if call.data == "nippellager":
        msg = '*NIPPEL LAGER*\nПивной напиток светлый нефильтрованный неосветленный непастеризованный с возможностью ' \
              'дображивания в бутылке. Бутылка 1,4 л, ПЭТ. Состав: питьевая вода, солод ' \
              'пивоваренный ячменный светлый, ячмень, хмель, пищевая добавка - кислота молочная, ' \
              'пивные дрожжи. Алкоголь: не более 0,5 % об. '
        bot.send_message(call.message.chat.id, msg)
    if call.data == "tverskoe_small":
        msg = '*Тверское* 0,5 л.\nПиво светлое фильтрованное пастеризованное. Бутылка 0,5 л, стекло ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый, ячмень, хмель. ' \
              'Экстрактивность начального сусла: 10 % ' \
              'Алкоголь: 4,1 % об. Срок годности – 180 суток '
        bot.send_message(call.message.chat.id, msg)
    if call.data == "tverskoe_big":
        msg = '*Тверское* 1,9 л.\nПиво светлое фильтрованное пастеризованное. Бутылка 1,9 л, ПЭТ ' \
              'Состав: питьевая вода, солод пивоваренный ячменный светлый, ячмень, хмель. ' \
              'Экстрактивность начального сусла: 10 % ' \
              'Алкоголь: 4,1 % об. Срок годности – 180 суток '
        bot.send_message(call.message.chat.id, msg)
bot.polling(none_stop=True, interval=0)