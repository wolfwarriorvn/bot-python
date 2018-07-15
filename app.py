# -*- coding: UTF-8 -*-
from lunar_convert import LunarConvert
from fbchat import Client
from fbchat.models import *
from apscheduler.schedulers.blocking import BlockingScheduler

def fb_send(mesg):
    client = Client('vietcuong2892@gmail.com', 'adUZ4G75')

    print('Own id: {}'.format(client.uid))

    thread_id = '2246840635356131'
    thread_type = ThreadType.GROUP

    client.send(Message(text=mesg), thread_id=thread_id, thread_type=thread_type)
    client.logout()

def bot_run():
    if LunarConvert.nextday(1).day == 15 or LunarConvert.nextday(1).day == 1:
        print("Hôm nay ngày %d ăn chay nhé ahihi" % (LunarConvert.today().day))
        fb_send("Hôm nay ngày %d ăn chay nhé ahihi" % (LunarConvert.today().day))
    elif LunarConvert.nextday(2).day == 15 or LunarConvert.nextday(2).day == 1:
        print("Ngày mai ngày %d ăn chay nhé ahihi" % (LunarConvert.nextday(1).day))
        fb_send("Ngày mai ngày %d ăn chay nhé ahihi" % (LunarConvert.nextday(1).day))
    else:
        print("Free task today!!!")

def bot_test():
    fb_send("ahihi test thoi nhé")




bot_run()

# print(LunarConvert.nextday(0).day)
# while True:
#     if LunarConvert.nextday(1).day == 15 or LunarConvert.nextday(1).day == 1:
#         print("Ngày mai ăn chay nhé ahihi")
#         fb_send("Ahihi")
