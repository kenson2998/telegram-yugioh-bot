#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from telegram.ext.updater import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext.commandhandler import CommandHandler
import telegram
from time import sleep
import random
from bs4 import BeautifulSoup
import requests

html_sample = [
                       u'https://asia.xpg.cards/pack/復刻包/174/LB-青眼白龍',#0
                       u'https://asia.xpg.cards/pack/復刻包/233/RB-暗黑魔龍復活',
                       u'https://asia.xpg.cards/pack/復刻包/195/ME-鋼鐵襲擊者',
                       u'https://asia.xpg.cards/pack/復刻包/211/PG-幻影的召喚神',
                       u'https://asia.xpg.cards/pack/復刻包/123/EE3-復刻高手包系列1',
                       u'https://asia.xpg.cards/pack/復刻包/123/EE3-復刻高手包系列2',
                       u'https://asia.xpg.cards/pack/復刻包/123/EE3-復刻高手包系列3',
                       u'https://asia.xpg.cards/pack/復刻包/123/EE3-復刻高手包系列4',
                       u'https://asia.xpg.cards/pack/復刻包/72/DL5-決鬥者遺產1',
                       u'https://asia.xpg.cards/pack/復刻包/72/DL5-決鬥者遺產2',
                       u'https://asia.xpg.cards/pack/復刻包/72/DL5-決鬥者遺產3',
                       u'https://asia.xpg.cards/pack/復刻包/72/DL5-決鬥者遺產4',
                       u'https://asia.xpg.cards/pack/復刻包/72/DL5-決鬥者遺產5',#12
                       u'https://asia.xpg.cards/pack/套牌/357/YU-遊戲篇',#13
                       u'https://asia.xpg.cards/pack/套牌/304/SY2-遊戲篇2',
                       u'https://asia.xpg.cards/pack/套牌/275/SDMY-武藤遊戯',
                       u'https://asia.xpg.cards/pack/套牌/273/SDKS-海馬瀨人',#16
                       u'https://asia.xpg.cards/pack/套牌/281/SK2-海馬2',
                       u'https://asia.xpg.cards/pack/套牌/171/KA-海馬篇',
                       u'https://asia.xpg.cards/pack/套牌/210/PE-貝卡斯',#19
                       u'https://asia.xpg.cards/pack/套牌/170/JY-城之內篇VOL1',#20
                       u'https://asia.xpg.cards/pack/套牌/279/SJ2-城之內2',
                       u'https://asia.xpg.cards/pack/套牌/274/SDM-馬力克',#22
                       ]
def bsoup(ranhtml,update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.from_user.first_name + duelcard,
                     parse_mode=telegram.ParseMode.HTML)
    req = requests.get(html_sample[ranhtml])
    sa = []
    sa1 = {'卡名': '', '攻擊力': '', '守備力': '', '種族': '', '屬性': '', '卡片描述': '', '種類': ''}
    sa2 = ''
    sa3 = ''
    soup = BeautifulSoup(req.text)

    for link in soup.select('img'):
        sa.append(link.get('src'))

    raa = random.randint(1, len(sa) - 1)
    print(raa, ',', len(sa) - 1)
    for link in soup.select('#app > div > div.container > div.pack-page > div > a:nth-of-type(' + str(raa) + ')'):
        sa2 = (link.get('href'))
    req1 = requests.get(u'https://asia.xpg.cards' + sa2)
    print(u'https://asia.xpg.cards' + sa2)
    soup1 = BeautifulSoup(req1.text)
    taa = 1
    sss = soup1.select('#app > div > div.container > div.card > div > div.info > img')
    for link in sss:
        sa2 = link.get('src')
    sss = soup1.select('#app > div > div.container > div.card > div > div.detail > ul > div.box > div > div.effect')
    for link in sss:
        sa1['卡片描述'] = (link.text).replace(u'卡片描述', '')

    while taa < 8:
        sss = soup1.select(
            '#app > div > div.container > div.card > div > div.detail > ul > div.box > div > table > tbody > tr > td:nth-of-type(' + str(
                taa) + ')')

        for link in sss:

            if (link.text).find(u'種類') > 0:
                sa1['種類'] = (link.text).replace(u'種類', '')
                sa3 = sa3 + u'\n種類:' + sa1['種類']
            if (link.text).find(u'屬性') > 0:
                sa1['屬性'] = (link.text).replace(u'屬性', '')
                sa3 = sa3 + u'\n屬性:' + sa1['屬性']
            if (link.text).find(u'種族') > 0:
                sa1['種族'] = (link.text).replace(u'種族', '')
                sa3 = sa3 + u'\n種族:' + sa1['種族']
            if (link.text).find(u'攻擊力') > 0:
                sa1['攻擊力'] = (link.text).replace(u'攻擊力', '')
                sa3 = sa3 + u'\n攻擊力:' + sa1['攻擊力']
            if (link.text).find(u'守備力') > 0:
                sa1['守備力'] = (link.text).replace(u'守備力', '')
                sa3 = sa3 + u'\n守備力:' + sa1['守備力']
            if (link.text).find(u'屬性') > 0:
                sa1['屬性'] = ((link.text))
                sa3 = sa3 + u'\n屬性:' + sa1['屬性']

        taa = taa + 1
    sa3 = u'卡名:' + soup1.title.text.replace(u'- AsiaCards(亞洲卡片王)', '') + sa3 + u'\n卡片描述:' + sa1['卡片描述'] + '\n' + sa2
    sleep(1)

    print (update.message.from_user.first_name)
    bot.send_message(chat_id=update.message.chat_id, text=sa3)

updater = Updater('00000000:XXXXXXXX')
dispatcher = updater.dispatcher
bot = telegram.Bot(token='00000000:XXXXXXXX')
starttext = u'<b>:「闇の扉が…開かれた」「黑暗之門…打開了」</b>'
duelcard = u'<b>:「我的回合抽牌!! 」</b>'

def start(bot, update):

    custom_keyboard = [[u'隨機抽牌'], ["抽遊戲牌組", "抽海馬牌組"], ["抽馬力克牌組",'抽貝卡斯牌組','抽城之內牌組'], ['取消遊戲']]

    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat_id, text=u'「' + update.message.from_user.first_name + u"開啟了黑暗遊戲。」",
                     reply_markup=reply_markup)
    bot.send_message(chat_id=update.message.chat_id, text=update.message.from_user.first_name +starttext,parse_mode = telegram.ParseMode.HTML)


def canceel(bot, update):
    reply_markup3 = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=update.message.chat_id, text=u'「' + update.message.from_user.first_name + u"關閉了黑暗遊戲。」", reply_markup=reply_markup3)


def echo(bot, update):
    print(update.message.text)
    print(update.message.from_user.first_name)

    if update.message.text == u'抽遊戲牌組':
       ranhtml=random.randint(13, 15)
       bsoup(ranhtml,update)
    elif update.message.text == u'抽海馬牌組':
       ranhtml=random.randint(16, 18)
       bsoup(ranhtml,update)
    elif update.message.text == u'抽馬力克牌組':
       ranhtml=22
       bsoup(ranhtml,update)
    elif update.message.text == u'抽城之內牌組':
       ranhtml=random.randint(20, 21)
       bsoup(ranhtml,update)
    elif update.message.text == u'抽貝卡斯牌組':
        ranhtml = 19
        bsoup(ranhtml, update)
    elif update.message.text == u'隨機抽牌' or update.message.text == '/draw@YuGiOhAtem_bot':

       ranhtml=random.randint(0, len(html_sample) - 1)
       bsoup(ranhtml,update)
        # bot.send_photo(chat_id=update.message.chat_id, photo=sa2)
    elif update.message.text == u'取消遊戲':
        canceel(bot, update)
    else :
         print (update.message.from_user.first_name)
         # text = '<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.'
         # custom_keyboard = [['top-left', 'top-right'],['bottom-left', 'bottom-right']]

         reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
         bot.send_message(chat_id=update.message.chat_id, text=u'「' + update.message.from_user.first_name + u"開啟了黑暗遊戲。」",
                          reply_markup=reply_markup)

         # bot.send_message(chat_id=update.message.chat_id, text=duelcard,parse_mode = telegram.ParseMode.HTML)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('cancel', canceel))
dispatcher.add_handler(CommandHandler('draw', echo))
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()