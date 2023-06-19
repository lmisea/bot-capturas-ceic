# Autor: Luis Miguel Isea
# Carnet: 19-10175

# Este bot de telegram tiene la intención de facilitar el control y registro de los pagos, reenviando los comprobantes de pago al grupo de Tesorería.
# En un futuro se le podrían añadir más funcionalidades, como por ejemplo, registrar los pagos en un drive, o en el mismo Excel de control de ventas.

# Para el bot uso la librería python-telegram-bot, en la versión 20.3. Hay que estar pendiente porque en internet sale mucha información de versiones anteriores, que no son compatibles.
# Para instalar la librería: 'pip install -r requirements.txt'.

# Los archivos de log se guardan en el directorio $HOME/.bot-capturas-log/, con el nombre del archivo en el formato: 'DD-MM-YYYY_HH:MM:SS.log'.
# Así, se crea un archivo de log por cada ejecución del bot.

import logging
import os
from datetime import datetime

from telegram import Update, constants
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)

# Configura el token de acceso del bot dado por BotFather
BOT_TOKEN = 'Acá va el token del bot'

# Configura el ID del grupo a donde se reenviarán los comprobantes
FORWARD_GROUP_ID = 'Acá va el ID del grupo'

# Obtener el path del directorio donde se van a guardar los logs
HOME = os.path.expanduser('~')
LOG_DIR = os.path.join(HOME, '.bot-capturas-log')

# Verifica que exista el directorio donde se van a guardar los logs
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configura el nombre del archivo de logs
DATE = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
LOG_FILE = os.path.join(LOG_DIR, DATE + '.log')

# Configura el nivel de registro de logs
logging.basicConfig(filename=LOG_FILE, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mensaje de bienvenida a penas se ejecuta /start."""
    user = update.message.from_user
    await update.message.reply_text(f"Hola, {user.first_name} 😊 ¡Envía la foto del comprobante del pago a nuestro bot y se le reenviará al equipo de Tesorería, facilitando el control y registro de los pagos! 😎\n\nPor favor, envía la foto del comprobante del pago <b>como una foto</b>, no como archivo.", parse_mode=constants.ParseMode.HTML)

# Reenviar comprobantes de pago
async def reenviar_pago(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Esta función se encarga de reenviar los comprobantes de los pagos al grupo de Tesorería."""
    user = update.effective_user

    # Reenvía la imagen al grupo de Tesorería
    await update.message.forward(chat_id=FORWARD_GROUP_ID)

    # Verifica si el usuario tiene last_name y username
    last_name = '' if user.last_name is None else f' {user.last_name}'
    username = 'No tiene username' if user.username is None else f'@{user.username}'

    # Envía un mensaje al grupo de Tesorería indicando quién envió el comprobante
    await context.bot.send_message(chat_id=FORWARD_GROUP_ID, text=f"Enviado por: {user.first_name}{last_name} ({username})")

    # Envía un mensaje al remitente confirmando el envío del comprobante
    await update.message.reply_text("¡El comprobante del pago ha sido enviado con éxito al CEIC! Gracias 🫶")

# Maneja cualquier otro tipo de mensaje que no sea una foto
async def handle_any_other_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Función que maneja cualquier otro tipo de mensaje que no sea una foto."""
    await update.message.reply_text("Lo siento, no puedo procesar ese tipo de mensaje.\n\nPor favor, envía el comprobante del pago <b>como una foto</b>.", parse_mode=constants.ParseMode.HTML)

# Función principal que inicia el bot
def iniciar_bot():
    # Se crea la app y se le pasa el token del Bot
    application = Application.builder().token(BOT_TOKEN).build()

    # Configura los handlers de comandos
    start_handler = CommandHandler('start', start)
    photo_handler = MessageHandler(filters.PHOTO, reenviar_pago)
    any_other_message_handler = MessageHandler(filters.ALL, handle_any_other_message)

    # Agrega los handlers a la app
    application.add_handler(start_handler)
    application.add_handler(photo_handler)
    application.add_handler(any_other_message_handler)

    # Inicia el hosting del bot hasta que se presione Ctrl+C
    application.run_polling()
