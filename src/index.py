import os
import json
import docker
import telepot
from telepot.loop import MessageLoop

tg_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
tg_admin_id = os.environ['TELEGRAM_ADMIN_ID']


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(tg_admin_id, msg['text'])


bot = telepot.Bot(tg_bot_token)
MessageLoop(bot, handle).run_as_thread()
client = docker.from_env()
events = client.events()
for event in events:
    print(event)
    parsed_event = json.loads(event)
    msg = "*" + parsed_event['Type'] + "*"
    bot.sendMessage(tg_admin_id, msg, parse_mode='Markdown')
