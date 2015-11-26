"""
import sys
import time
import random
import datetime
"""
import telepot
# import os
# from bottle import run
from telepot.delegate import per_chat_id, create_open


class VeryCruel(telepot.helper.ChatHandler):

    def __init__(self, seed_tuple, timeout):
        super(VeryCruel, self).__init__(seed_tuple,timeout)

    def reply_to_kek(self, content_type, m):
        if content_type == 'text' and 'кек' in m.text:
            self.sender.sendMessage('ИДИ ФПИЗДУ ПИДАРАС', reply_to_message_id=m.message_id)
            return True
        else:
            return False

    def reply_to_badgay(self, content_type, m):
        if content_type == 'text' and 'хуй' in m.text:
            self.sender.sendMessage('НЕ МАТЕРИСЬ, ПИДАРАС!', reply_to_message_id=m.message_id)

    def on_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance2(msg)
        m = telepot.namedtuple(msg, 'Message')

        if chat_id < 0:
            # public chat
            if not self.reply_to_serjant(content_type, m):
                self.reply_to_badgay(content_type, m)
        else:
            # private conversation
            self.reply_to_badgay(content_type, m)

    """
    def on_close(self, exception):
        if isinstance(exception, telepot.helper.WaitTooLong):
            bot.notifyOnMessage(run_forever=True)
    """

TOKEN = '148865285:AAHvwDHJGVrSzEGJ_ToGUxk1RWclvX2L_W4'

bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(VeryCruel, timeout=1)),
])
bot.notifyOnMessage(run_forever=True)
