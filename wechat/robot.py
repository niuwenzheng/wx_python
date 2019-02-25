
from werobot import WeRoBot
import json
# Create your views here.
myrobot = WeRoBot(enable_session=False,token='niuniu',app_id='wx93f9e0c4b7c341be',app_secret='4ae277740b39a26205d86106fc5b6f4c')
client = myrobot.client

@myrobot.handler
def hello(message):
    return '欢迎关注测试账号'
@myrobot.text
def backA(message):
    if message.content =='A':
        userinfor = client.get_user_info(message.source,lang='zh_CN')
        return ('A'+userinfor['nickname'])
    else:
        return '不要乱回复'

@myrobot.key_click("music")
def music(message):
    return '你点击了“使用说明”按钮'


client.create_menu({
    "button":[{
         "type": "click",
         "name": "使用说明",
         "key": "music",
    },{
     "type": "view",
         "name": "sousou",
         "url":"http://www.soso.com/",
    },{
        "type": "view",
         "name": "个人数据",
         "url":"https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx93f9e0c4b7c341be&redirect_uri=https%3a%2f%2fwww.wegoto.xyz%2ftheweb%2f&response_type=code&scope=snsapi_base&state=123#wechat_redirect/"    
    }]
})