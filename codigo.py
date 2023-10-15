import telebot
import datetime

# Crear instancia del bot con el token proporcionado por BotFather
bot = telebot.TeleBot("6494400228:AAHHLW6Mes860FRtgcV9RAOvB5kqHt6BXfQ")
now = datetime.datetime.now()
# Manejar el comando /start
@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.username is None:
        bot.send_message(message.chat.id, "🙏 Por favor para acceder a las funciones del bot asignese un nombre de usuario en la configuracion de su perfil en Telegran.")
    else:
        bot.send_message(message.chat.id, f"👋 Bienvenido @{message.from_user.username}.\n\n🤖 Soy el controlador de pagos de Kerter+.\n\n⚙️ Mi función es verificar tu suscripción.\n\n1️⃣ Primeramente tiene que estar registrado en www.kerter.cu/kerter-plus.\n\n2️⃣ Despues de haberse registrado presione /pago y siga los pasos para que su verificación sea válida.")

# Manejar el comando /pago
@bot.message_handler(commands=['pago'])
def send_payment_request(message):
    if message.chat.username is None:
        bot.send_message(message.chat.id, "🙏 Por favor para acceder a las funciones del bot asignese un nombre de usuario en la configuracion de su perfil en Telegran.")
    else:
        bot.send_message(message.chat.id, "📲 Por favor, envíeme una captura de pantalla de la transferencia para que sea revisada por un administrador que le avisará rapidamente cuando su suscripción este activa\n\nTiene que enviarme una imagen obligatoriamente, sino su transferencia será invalidada, dele prioridad a que se vea la fecha y el número de transacción")

# Manejar las imágenes enviadas por el usuario
@bot.message_handler(content_types=['photo'])
def handle_payment_proof(message):
    # Verificar que el mensaje tenga una foto
        user_info = (f"👤 Nombre de Usuario: @{message.from_user.username}\n\n🆔 ID del Usuario: {message.from_user.id}\n\n📆 Fecha de pago:{now.day}/{now.month}/{now.year}\n\n⬇️ Aquí esta la captura de la transferencia jefe:")
        bot.send_message(chat_id='-1001655572791', text=user_info)

        bot.forward_message(chat_id='-1001655572791', from_chat_id=message.chat.id, message_id=message.message_id)
        # Obtener la información del usuario
        
        # Enviar la información del usuario junto con la imagen
        
        bot.reply_to(message, "⏳ Su transferencia esta siendo revisada, pronto recibirá un mensaje de nuestro soporte\n🙏 Si hay algun contratiempo le avisaremos")


# Iniciar el bot
if __name__=='__main__':
   print('iniciado')
   bot.infinity_polling()

