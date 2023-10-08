import telebot
# Crear el bot con el token de acceso
TOKEN='6636288744:AAFhyH1hnrilP2fBGutv4F_WxSy8OV2XtCc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def send_welcome(message):
 # Enviar mensaje de bienvenida con botones
    bot.reply_to(message, f"👋 Hola @{message.from_user.username}!\n\n❗️ Este bot solo funciona cuando hay sorteos en @fifacuba, mantente al tanto\n\n👮 Creado por @Alex_GlezRM")
 #Manejar el comando /archivo1

if __name__=='__main__':
    print('iniciando')
    bot.infinity_polling()
