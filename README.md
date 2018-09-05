###用telegram-bot 來做一個抽卡的機器人

首先要創立一個機器人，這部分請找BotFather申請，不多加敘述<br>

創好以後拿到機器人token就可以直接使用啦~ <br>

這邊/的指令設定我是只有用/start 、 /cancel 、 /draw ，主要開啟用start，關閉用cancel ，draw 是早期直接抽牌互動用的<br>

後來發現echo 好像比較多使用性就用echo了<br>

網路上找了一個遊戲王的卡片網:https://asia.xpg.cards <br>

爬蟲是很常變動的，所以 html_sample 裡面擺放的網址是有可能因為網址更動而失效的。<br>

使用爬蟲看一下xpath的規則就可以來抓取圖片連結和卡片資料<br>

1.先找到頁面所有HTML標籤為"img"的元素 網址，並存到sa陣列裡面，這個套卡有幾張牌的意思。<br>

```python
for link in soup.select('img'):
    sa.append(link.get('src'))
```
2.隨機抽卡會用到random工具，產生隨機一個數字，一個不大於sa的數字。<br>

這個是卡片的xpath:'#app > div > div.container > div.pack-page > div > a:nth-of-type(' + str(raa) + ')'<br>
將href網址丟入sa2。<br>

```python
raa = random.randint(1, len(sa) - 1)
    print(raa, ',', len(sa) - 1)
    for link in soup.select('#app > div > div.container > div.pack-page > div > a:nth-of-type(' + str(raa) + ')'):
        sa2 = (link.get('href'))
```

sa1 是用來放卡片資訊的字典，裡面的key 可宣告可不宣告，這邊宣告是顯示訊息的時候比較整齊，不宣告的話key的位置不會照順序排列。<br>
sa1 = {'卡名': '', '攻擊力': '', '守備力': '', '種族': '', '屬性': '', '卡片描述': '', '種類': ''}<br>
<br>


3.用ReplyKeyboardMarkup 來創建一組按鈕，就可以不用打字傳送指令了，這也是我用來和MessageHandler配合使用的方法。<br>
以下是開啟和關閉按鈕面板的function。<br>

```python
def start(bot, update):

    custom_keyboard = [[u'隨機抽牌'], ["抽遊戲牌組", "抽海馬牌組"], ["抽馬力克牌組",'抽貝卡斯牌組','抽城之內牌組'], ['取消遊戲']]

    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat_id, text=u'「' + update.message.from_user.first_name + u"開啟了黑暗遊戲。」",
                     reply_markup=reply_markup)
    
def canceel(bot, update):
    reply_markup3 = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=update.message.chat_id, text=u'「' + update.message.from_user.first_name + u"關閉了黑暗遊戲。」", reply_markup=reply_markup3)
```
4. 下面是監聽的部分，而echo_handler = MessageHandler()是用來處理訊息用的，CommandHandler是處理/指令的，<br>
所以我大部份都是用MessageHandler做事，內鍵的/start是第一次訪問bot時預設的指令，我也不浪費當作開啟抽牌遊戲的指令。<br>
<img src='https://raw.githubusercontent.com/kenson2998/telegram-yugioh-bot/master/1.jpg'></img>

```python
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('cancel', canceel))
dispatcher.add_handler(CommandHandler('draw', echo))
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
```
<img src='https://raw.githubusercontent.com/kenson2998/telegram-yugioh-bot/master/2.jpg'></img>