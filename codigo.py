import telebot
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

now=datetime.datetime.now()

Token="6821698862:AAGPiEmjlMsWvvaHWH_yUYVrqLO9iImuZ7c"

bot=telebot.TeleBot(Token)


#Comandos NO BOTONES
@bot.message_handler(commands=["start"])
def start(message):

   

    if message.chat.username is None:
        bot.send_message(message.chat.id, "🙏 Por favor para acceder a las funciones del bot asignese un nombre de usuario en la configuración de su perfil en Telegram.")
    else:

        markup= telebot.types.InlineKeyboardMarkup()
        button1= telebot.types.InlineKeyboardButton(text="⚙️ Recargar", callback_data="button1")
        button20= telebot.types.InlineKeyboardButton(text="👨🏻‍💻 Soporte", callback_data="button20")
        markup.add(button1,button20)

        bot.send_message(message.chat.id, f"👋 Hola @{message.from_user.username}.\n\n💰 Bienvenido a la mejor tienda de recarga para Free Fire en Cuba\n\n⚙️ Nuestro objetivo es garantizar al usuario una oportunidad comoda y automatizada para recargar y así no realentizar el proceso esperando por OTROS.\n\n⬇️ Estas en tu casa FreeWise\n\n /Creado por *Alex Gonzalez*/", reply_markup=markup)

 

@bot.message_handler(content_types=['photo'])
def handle_payment_proof(message):
        
        user_info = (f"⬇️ Datos del usuario:\n\n👤 Nombre de Usuario: @{message.from_user.username}\n\n🆔 ID del Usuario: {message.from_user.id}\n\n📆 Fecha de pago: {now.day}/{now.month}/{now.year}\n\n⬇️ VERIFICAR TRANSFERENCIA:")
        bot.send_message(chat_id='-1002038613433', text=user_info)
    # Verificar que el mensaje tenga una foto
        bot.forward_message(chat_id='-1002038613433', from_chat_id=message.chat.id, message_id=message.message_id)
        # Obtener la información del usuario

        # Enviar la información del usuario junto con la imagen

        bot.reply_to(message, f"⏳ Su captura ha sido recibida")


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):

    if call.data=="button20":
        bot.send_message(call.message.chat.id, "Escriba a @Alex_GlezRM")

    if call.data=="button1":

        markup= telebot.types.InlineKeyboardMarkup()
        button3= telebot.types.InlineKeyboardButton(text="💎 100 ", callback_data="button3")
        button4= telebot.types.InlineKeyboardButton(text="💎 310 ", callback_data="button4")
        button5= telebot.types.InlineKeyboardButton(text="💎 520 ", callback_data="button5")
        button6= telebot.types.InlineKeyboardButton(text="💎 1060 ", callback_data="button6")
        button7= telebot.types.InlineKeyboardButton(text="❇️ Membresía Semanal", callback_data="button7")
        button8= telebot.types.InlineKeyboardButton(text="❇️ Membresía Mensual", callback_data="button8")

        button14= telebot.types.InlineKeyboardButton(text="Atras", callback_data="button14")




        markup.add(button3,button4,button5,button6,button7,button8,button14)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'/⚙️ Recargar:/\n\n🪙 Aquí puede ver los tipos de recargas disponibles para Free Fire \n\n💰 Pagos en monedas circulantes en Cuba y Criptomonedas.\n\n*👉 Seleccione la opción que desee*', reply_markup=markup, parse_mode='Markdown')


    elif call.data=="button14":

        markup= telebot.types.InlineKeyboardMarkup()
        button1= telebot.types.InlineKeyboardButton(text="⚙️ Recargar", callback_data="button1")
        button20= telebot.types.InlineKeyboardButton(text="👨🏻‍💻 Soporte", callback_data="button20")
        markup.add(button1,button20)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"👋 Hola @{call.message.from_user.username}.\n\n💰 Bienvenido a la mejor tienda de recarga para Free Fire en Cuba\n\n⚙️ Nuestro objetivo es garantizar al usuario una oportunidad comoda y automatizada para recargar y así no realentizar el proceso esperando por OTROS.\n\n⬇️ Estas en tu casa FreeWise\n\n /Creado por *Alex Gonzalez*/", reply_markup=markup, parse_mode='Markdown')
 
    if call.data=="button3":
         
        markup= telebot.types.InlineKeyboardMarkup()
        button9= telebot.types.InlineKeyboardButton(text="MLC", callback_data="button9")
        button10= telebot.types.InlineKeyboardButton(text="CUP", callback_data="button10")
        button11= telebot.types.InlineKeyboardButton(text="USDT", callback_data="button11")
        button12= telebot.types.InlineKeyboardButton(text="Saldo Móvil", callback_data="button12")

        button15= telebot.types.InlineKeyboardButton(text="Atras", callback_data="button15")




        markup.add(button9,button10,button11,button12,button15)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Seleccione el método de pago con el que desea realizar su compra:*\n\nMLC\nCUP\nUSDT\nSaldo Móvil*", reply_markup=markup, parse_mode='Markdown')

    elif call.data=="button15":
        markup= telebot.types.InlineKeyboardMarkup()
        button3= telebot.types.InlineKeyboardButton(text="💎 100 ", callback_data="button3")
        button4= telebot.types.InlineKeyboardButton(text="💎 310 ", callback_data="button4")
        button5= telebot.types.InlineKeyboardButton(text="💎 520 ", callback_data="button5")
        button6= telebot.types.InlineKeyboardButton(text="💎 1060 ", callback_data="button6")
        button7= telebot.types.InlineKeyboardButton(text="❇️ Membresía Semanal", callback_data="button7")
        button8= telebot.types.InlineKeyboardButton(text="❇️ Membresía Mensual", callback_data="button8")

        button14= telebot.types.InlineKeyboardButton(text="Atras", callback_data="button14")




        markup.add(button3,button4,button5,button6,button7,button8,button14)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'/⚙️ Recargar:/\n\n🪙 Aquí puede ver los tipos de recargas disponibles para Free Fire \n\n💰 Pagos en monedas circulantes en Cuba y Criptomonedas.\n\n*👉 Seleccione la opción que desee*', reply_markup=markup, parse_mode='Markdown')

    if call.data=="button9": 

        markup= telebot.types.InlineKeyboardMarkup()
        button13= telebot.types.InlineKeyboardButton(text="Listo", callback_data="button13")
        button16= telebot.types.InlineKeyboardButton(text="Atras", callback_data="button16")




        markup.add(button13,button16)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Efectuar Compra:\n\nCompra:💎 100 Diamantes\n\nImporte------ 01.20 MLC\nComisión----- 00.00 MLC\n\nTotal--------- 1.20 MLC\n\nTransfeir a :\n\n `1234-5678-9123-4567`\n56618386\n\nLuego de realizar la transferencia envia al bot la captura de pantalla de la transferencia y acto seguido (Su ID en FREE FIRE, SOLO ACEPTAMOS ID)y luego presione LISTO y en seguida efectuaremos su pedido", reply_markup=markup, parse_mode='Markdown')








   

bot.polling()        


