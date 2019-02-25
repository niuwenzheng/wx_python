import json
import urllib3

http = urllib3.PoolManager()
def getToken():
    url = 'https://api.weixin.qq.com/cgi-bin/token'#grant_type为固定值
    data = {'grant_type':'client_credential',
            'appid':'wx93f9e0c4b7c341be',
            'secret':'4ae277740b39a26205d86106fc5b6f4c'}
    r=http.request(
        'GET',
        url,
        fields=data
    )
    return json.loads(r.data.decode('utf-8'))
