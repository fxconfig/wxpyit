
from wxpyit import *
import logging
logging.basicConfig(level=logging.INFO)

bot = Bot(
    cache_path="peter.pkl", 
    console_qr=False, 
    qr_callback=None, 
    login_callback=None,
    logout_callback=None
)


@bot.register(Friend,except_self=False)
def just_print_friend(msg: Message):
    print(f'Friend msg({msg.create_time}): {msg}')

@bot.register(Group, except_self=False)
def just_print_group(msg:Message):
    print(f'Group  msg ({msg.create_time}): {msg}')

bot.join()