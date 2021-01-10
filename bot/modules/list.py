from telegram.ext import CommandHandler, run_async
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot import LOGGER, dispatcher
from bot.helper.telegram_helper.message_utils import sendMessage, sendMarkup, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
 
@run_async
def list_drive(update,context):
    try:
        search = update.message.text.split(' ',maxsplit=1)[1]
        LOGGER.info(f"𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴: {search}")
        reply = sendMessage('𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴....𝗛𝗼𝗹𝗱 𝗢𝗻!', context.bot, update)
        gdrive = GoogleDriveHelper(None)
        msg, button = gdrive.drive_list(search)
 
        if button:
            editMessage(msg, reply, button)
        else:
            editMessage('𝗡𝗼 𝗿𝗲𝘀𝘂𝗹𝘁 𝗳𝗼𝘂𝗻𝗱', reply, button)
 
    except IndexError:
        sendMessage('𝘀𝗲𝗻𝗱 𝗮 𝘀𝗲𝗮𝗿𝗰𝗵 𝗸𝗲𝘆 𝗮𝗹𝗼𝗻𝗴 𝘄𝗶𝘁𝗵 𝗰𝗼𝗺𝗺𝗮𝗻𝗱', context.bot, update)
 
 
list_handler = CommandHandler(BotCommands.ListCommand, list_drive,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(list_handler)
