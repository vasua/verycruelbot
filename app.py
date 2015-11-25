"""
import sys
import time
import random
import datetime
"""
import telepot
from telepot.delegate import per_chat_id, create_open


class VeryCruel(telepot.helper.ChatHandler):

    def __init__(self, seed_tuple, timeout):
        super(VeryCruel, self).__init__(seed_tuple,timeout)

    def reply_to_serjant(self,m):
        self.sender.sendMessage('Сообщение получено от %s c id %s' % (m.from_, m.from_.id))

    def on_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance2(msg)
        m = telepot.namedtuple(msg, 'Message')

        if chat_id < 0:
            # public chat
            self.reply_to_serjant(m)
        else:
            # private conversation
            if content_type == 'text':
                if 'хуй' in m.text:
                    self.sender.sendMessage('НЕ МАТЕРИСЬ, ПИДАРАС!', reply_to_message_id=m.message_id)

TOKEN = '148865285:AAHvwDHJGVrSzEGJ_ToGUxk1RWclvX2L_W4'

bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(VeryCruel, timeout=15)),
])
bot.notifyOnMessage(run_forever=True)
