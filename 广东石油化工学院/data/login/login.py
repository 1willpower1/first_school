import requests
from school.广东石油化工学院.data.login.config import  headers
def login(username,password):
    import  base64
    #登录的网址
    url = "https://jwxt.gdupt.edu.cn/login!doLogin.action"
    # 登录使用的登录数据
    password = password.encode("utf-8")
    rel_password = base64.b64encode(password)
    data = {
        "account": f"{username}",
        "pwd": f"{rel_password.decode('utf-8')}",
        "verifycode": "",
    }
    #具体数据的网址
    try:
        resp1 = requests.session().post(data=data,headers=headers,url=url)
        if resp1.text == '{"msg":"/login!welcome.action","status":"y"}':
            print("登录成功")
        else:
            print("登录失败")
    except Exception as e:
        print(e)

