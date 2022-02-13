# -*- coding:utf-8 -*-
"""摸鱼日历： 发送 摸鱼日历 即可"""
from botoy import GroupMsg, FriendMsg, Picture, Text, Picture
from botoy.decorators import ignore_botself, startswith

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import time
import datetime
import random
import os

from .CalendarConvert import *

arr1 = [
    "早上好,摸鱼人!\n\n$1是摸鱼时间，该摸鱼的时候\n摸鱼,别让自己忙碌起来，老板\n不会关心你，只有我会关心你!",
    "早上好,摸鱼人\n\n又到$1了,摸鱼人的$1只想\n安安静静的摸鱼,工作什么的能\n推到下周就推到下周!\n毕竟身体是自己的,别累坏了自\n己,反而得不偿失!",
    "早上好,摸鱼人\n\n又是元气满满的一天哦!\n千万要记得,工作时候一定要摸\n鱼,只要还工作!钱自然不会少\n你的!",
    "早上好，摸鱼人!\n\n即使工作有压,也要好好摸鱼\n活下去,因为其它都是浮云!身\n体才是自己的,注意工作摸鱼两\n不误哟!",
    "早安，摸鱼人!\n\n虽然摸鱼很爽,但是也别贪多!\n注意提防老板和监控哟!\n下午的时候来杯咖啡提提神，时\n间很快就过去啦!",
    "早安,摸鱼人!\n\n工作再疲惫,划水要学会,\n工作再紧张,摸鱼不能忘。\n工作再疲惫、再紧张,也一定不\n要忘记摸鱼哦!"
]

arr2 = [
    "    偶尔摸鱼有害健康,常常\n摸鱼收获满满。",
    "    人生就是浑水,你不去趟\n，怎么能摸鱼呢?",
    "    “鱼”是我养的宠物,再忙都\n要花点时间摸摸才行!",
    "    感觉有什么东西在扒拉我\n,以为是爱情的魔爪,没想到是\n你的鱼钩!",
    "    做个优秀的摸鱼人,要摸\n遍有所企业和岗位,摸过所有\n不曾摸过的,才不虚此班!",
    "    相比于上班划水摸鱼,按\n时下班才会让人更快乐!",
    "    摸鱼人加班的信念是什么\n?是责任么?不,TM是贫穷!",
    "    现在时间告诉我,认真工作\n的时间已经过了,到了该摸鱼\n的时候了。",
    "    钱能治愈一切自卑,摸鱼\n能治愈一切忙碌。"
]


def get_date():
    random.seed(random_z())
    t_l = random.randint(1, 9)  # 九种背景

    # 设置所使用的字体/颜色
    colour_dict = {
        1: (7, 51, 113),
        2: (131, 56, 54),
        3: (47, 54, 120),
        4: (39, 88, 80),
        5: (15, 85, 103),
        6: (226, 86, 81),
        7: (131, 56, 54),
        8: (8, 53, 113),
        9: (17, 84, 105),
    }
    colour = colour_dict[t_l]
    date_font = ImageFont.truetype("./plugins/bot_moyu/font/方正粗圆宋简体.TTF", 19)  # 日期字体：方正粗圆宋简体，19
    date_font2 = ImageFont.truetype("./plugins/bot_moyu/font/sourceserif4subhead-bold.ttf",
                                    60)  # 日期字体：Source Serif 4 Subhead Bold，60
    date_font3 = ImageFont.truetype("./plugins/bot_moyu/font/方正大黑简体.ttf", 16)  # 日期字体：方正大黑简体，19
    date_font4 = ImageFont.truetype("./plugins/bot_moyu/font/方正大黑简体.ttf", 25)  # 日期字体：方正大黑简体，25

    # 打开图片
    imageFile = "./plugins/bot_moyu/images/" + str(t_l) + ".png"
    im1 = Image.open(imageFile)

    # 画图
    draw = ImageDraw.Draw(im1)
    # 设置日期文字位置/内容
    draw.text((50, 70), time.strftime("%y"), colour, font=date_font)  # 年
    draw.text((88, 70), time.strftime("%m"), colour, font=date_font)  # 月
    draw.text((45, 80), time.strftime("%d"), colour, font=date_font2)  # 日
    draw.text((32, 150), get_nongli_date(datetime.datetime.now()), colour, font=date_font3)  # 农历
    draw.text((162, 140), get_week_day(datetime.datetime.now()), colour, font=date_font4)  # 星期

    if (t_l == 6):
        date_font5 = ImageFont.truetype("D:/zm/bot_moyu/font/方正大黑简体.ttf", 20)  # 日期字体：方正大黑简体，20
        draw.text((85, 380), get_week_day(datetime.datetime.now()), colour, font=date_font5)  # 星期
        draw.text((195, 430), get_week_day(datetime.datetime.now()), colour, font=date_font5)  # 星期

    # 工作假期倒计时
    vacation_text = get_vacation_text(time.strftime("%m%d", time.localtime()))  # 倒计时文案
    draw.text((279, 233), random.choice(arr1).replace("$1", "周" + get_week_day(datetime.datetime.now())), colour,
              font=date_font3)  # 宣言
    draw.text((279, vacation_text.count('\n') * 117), vacation_text, colour, font=date_font3)  # 倒计时

    # 名言名句
    y_text = random.choice(arr2)
    if (y_text.count('\n') > 1):
        date_font5 = ImageFont.truetype("./plugins/bot_moyu/font/江西拙楷2.0.ttf", 18)  # 日期字体：江西拙楷2.0,20
    date_font5 = ImageFont.truetype("./plugins/bot_moyu/font/江西拙楷2.0.ttf", 20)  # 日期字体：江西拙楷2.0,20
    draw.text((38, 675), y_text, colour, font=date_font5)  # 宣言

    draw = ImageDraw.Draw(im1)  # Just draw it!

    # 另存图片
    today = time.strftime("%d", time.localtime())
    im1.save(r'./plugins/bot_moyu/images/output/output' + today + '.png')


def checkUser():  # 判断是否今天获取过
    today = time.strftime("%d", time.localtime())
    cacheFileName = './plugins/bot_moyu/images/output/output' + today + '.png'
    if not os.path.isfile(cacheFileName):
        execute()
        return True
    return False


def execute():  # 删除旧记录
    filePath = '/root/opqbot/client/botoy/plugins/bot_moyu/images/output/'
    name = os.listdir(filePath)
    for i in name:
        path = '/root/opqbot/client/botoy/plugins/bot_moyu/images/output/{}'.format(i)
        print(path)
        if 'output' in i:
            os.remove(path)


def random_z():
    t = time.time()
    time_s = str(round(t * 1000000))
    return int(time_s[::-1][1:6])


@ignore_botself  # 忽略机器人自身的消息
def receive_group_msg(ctx: GroupMsg):
    if (ctx.Content == "摸鱼日历"):
        today = time.strftime("%d", time.localtime())
        if ctx.FromUserId == 1340219674:
            execute()
            get_date()
        elif checkUser():
            get_date()
        cacheFileName = './plugins/bot_moyu/images/output/output' + today + '.png'
        Picture(pic_path=cacheFileName)


@ignore_botself  # 忽略机器人自身的消息
def receive_friend_msg(ctx: FriendMsg):
    if (ctx.Content == "摸鱼日历"):
        today = time.strftime("%d", time.localtime())
        if FromUin == 1340219674:
            execute()
            get_date()
        elif checkUser():
            get_date()
        cacheFileName = './plugins/bot_moyu/images/output/output' + today + '.png'
        Picture(pic_path=cacheFileName)
