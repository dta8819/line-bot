#載入flask模Flaskequest,abort
from flask import Flask, request, abort

#載入linebot模組中的LineBotApi(Lieokebookaer(Lie
from linebot import (
    LineBotApi, WebhookHandler
)
#載入1inebot.exceptions組的Ivliiger錯偵錯用的
from linebot.exceptions import (
    InvalidSignatureError
)
#載入1inebot.models模中的MessageEventTextMessageTextSendMessage
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
#載入json模组(格式化輸出結果
import json
#載入os組(此於讀取環境)
import os

#建立 application物件
app = Flask(__name__)
#放入自己的LINEBOT-ChanelAccessToken
line_bot_api = LineBotApi("os.getenv('CHANNEL_ACCESS_TOKEN"))
#放入自己的LINEBOTChannelSecret
handler = WebhookHandler("os.getenv('CHANNEL_SECRET"))
    
#Webhook 入口
@app. route("/callback",  methods=[ 'PosT'])
def callback():
    # Get X-Line-Signature header value
    signature = request. headers ['X-Line-Signature' ]
    #將接收到的請求轉换為文字
    body = request.get_data(as_text=True)
    #將接收到的資訊轉為JSON格
    json_data = json. loads(body)
    #”格式化 json_dat讓輸储結果增加可請性
    json_str = json.dumps(json_data,indent=4)
    #印出來檢视一下
    print(json_str)
    # Handle Webhook body
    try:
        #如果ChannelAccessToken或ChanelSecret發生錯誤
        #會進入到exceptInvalidSignatureError:區塊・
        handler.handle(body,signature)
    except  InvalidSignatureError:
        #如果有錯誤代表ChannelAcceokenecet
        #可能輪入錯誤或無效
        #處理錯誤,abort400-
        abort(400)
    #返回OKLINEDeveloper收到代表book執行沒
    return 'OK'

#linebot訊息接收處
@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    #將接收到的資訊轉為JSON格式
    json_data = json.loads(str(event))
    #格式化 json_dat讓結可性
    json_str = json.dumps(json_data, indent=4)
    #印出來檢視一下
    print(json_str)
    #獲得使用者傳來的訊息
    msg = event.message.text
    #回應訊息 傳送msg
    line_bot_api.reply_message(event.reply_token, TextSendMessage(msg))


if __name__=="__main__":
    app.run(port=3000)
