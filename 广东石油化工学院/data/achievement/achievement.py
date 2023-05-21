import  requests
from school.广东石油化工学院.data.login.login import login
def achievement(page,username,password,flag):
    cookie = login(username,password,flag)
    achievement = [
    ]
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "60",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": f"TWFID=8328cd0fa9b6ca13; browserID=1952807128;{cookie[0]}",
        "Host": "jwxt.gdupt.edu.cn",
        "Origin": "https://jwxt.gdupt.edu.cn",
        "Referer": "https://jwxt.gdupt.edu.cn/xskccjxx!xskccjList.action?firstquery=1",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    #需要根据一共页数来爬取
    for i in range(page):
        data = {
            "xnxqdm":"",
            "page":f"{i}",
            "rows":"20",
            "sort":"xnxqdm,kcbh,ksxzdm",
            "order":"asc"
        }
        # 成绩的地址
        url = "https://jwxt.gdupt.edu.cn/xskccjxx!getDataList.action"
        kind = {}
        # data = {
        #     "account": 22014260526,
        #     "pwd": "MTM5MjgzMzc4NTVh",
        #     "verifycode": "",
        # }
        resp = requests.session().post(data=data,headers=headers,url=url)
        if resp.json().get("rows"):
            for i in range(len(resp.json().get("rows"))):
                kind["kcmc"] = resp.json().get("rows")[i].get("kcmc")
                kind["xf"] = resp.json().get("rows")[i].get("xf")
                kind["jd"] = resp.json().get("rows")[i].get("cjjd")
                kind["cjfsmc"] = resp.json().get("rows")[i].get("cjfsmc")
                kind["kcbh"] = resp.json().get("rows")[i].get("kcbh")
                kind["kcdlmc"] = resp.json().get("rows")[i].get("kcdlmc")
                kind["ksxzmc"] = resp.json().get("rows")[i].get("ksxzmc")
                achievement.append(kind)
                kind = {}
            print(achievement)
        else:
            print('爬取失败')
