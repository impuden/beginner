import pyowm
import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('your_token', parse_mode='html')

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('your_token')
mgr = owm.weather_manager()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        sti = open('C:\puthon\stickers\sakorona.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        name = message.from_user.first_name
        bot.send_message(message.chat.id, "Приветствую, " + name +'\n Я - testbot, подопытный бот.' '\n Могу сказать какая погода в твоем городе, просто напиши название)')
	
@bot.message_handler(func=lambda m: True, content_types=['text'])
def echo_all(message):
        observation = mgr.weather_at_place( message.text )
	w = observation.weather
	
	temp = int(w.temperature('celsius')["temp"])
	lol = str(w.detailed_status)
	
	answer = "В городе " + message.text + " сейчас " + str(lol) + '\n'
	answer += "Температура около " + str(temp) +  "\n\n"
	
	if temp < -5:
		answer += "Только зимняя одежда"
	elif temp < 10:
		answer += "Холодно, оденься теплее"
	elif temp < 20:
		answer += "Не забудь куртку"
	else:
		answer += "Получай удовольствие от прогулок"
		
	bot.send_message(message.chat.id, answer)
	
bot.infinity_polling()
