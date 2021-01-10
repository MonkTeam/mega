from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.telegram_helper.message_utils import *
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.bot_utils import new_thread
from bot import dispatcher
 
 
@new_thread
def cloneNode(update,context):
    args = update.message.text.split(" ",maxsplit=1)
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"𝗖𝗹𝗼𝗻𝗶𝗻𝗴..𝗪𝗮𝗶𝘁 𝗽𝗹𝘀.🤓\n\n 𝗟𝗶𝗻𝗸: <code>{link}</code>",context.bot,update)
        gd = GoogleDriveHelper()
        result, button = gd.clone(link)
        deleteMessage(context.bot,msg)
        if button == "":
            sendMessage(result,context.bot,update)
        else:
            sendMarkup(result,context.bot,update,button)
    else:
        sendMessage("𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗚-𝗗𝗿𝗶𝘃𝗲 𝗦𝗵𝗮𝗿𝗲𝗮𝗯𝗹𝗲 𝗟𝗶𝗻𝗸 𝘁𝗼 𝗖𝗹𝗼𝗻𝗲😐.",context.bot,update)
 
clone_handler = CommandHandler(BotCommands.CloneCommand,cloneNode,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(clone_handler)
