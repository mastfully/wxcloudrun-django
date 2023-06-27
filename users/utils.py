import requests

class GetOpenId:

    jscode2session_url = 'https://api.weixin.qq.com/sns/jscode2session'

    def __init__(self,appid,appsecret):
        self.appid = appid
        self.appsecret = appsecret

    def get_session(self,code):
        url = f"{self.jscode2session_url}?appid={self.appid}&secret{self.appsecret}&js_code" \
              f"={code}&grant_type=authorization_code"

        resp = requests.get(url,verify=False)
        try:
            return resp.json()
        except Exception:
            return None
