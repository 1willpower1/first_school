import requests
from school.广东石油化工学院.data.login.login import login
#登录的网址
#具体数据的网址
#zc = 填现在的周次 xnxqdm:年级数+第几学期 第一学期:01
def curriculum(xnxqdm,zc,username,password,flag):
    cookie = login(username,password,flag)
    headers = {
        "Accept": "application/json,text/javascript,*/*; q=0.01",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Cookie":f"TWFID=8328cd0fa9b6ca13; browserID=1952807128;{cookie[0]}",
        "Host": "jwxt.gdupt.edu.cn",
        "Referer": "https://jwxt.gdupt.edu.cn/xsgrkbcx!xskbList.action?xnxqdm=202202&zc=13",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    pn = 1
    params = {"xnxqdm":xnxqdm,"zc": zc}
    curriculum = []
    while 1:
        url = f"https://jwxt.gdupt.edu.cn/xsgrkbcx!getKbRq.action?xnxqdm=202202&zc={pn}"
        try:
            resp = requests.session().get(params=params,url=url,headers=headers)
            if resp.json()[0]:
                for i in range(len(resp.json()[0])):
                    jcdms = resp.json()[0][i].get("jcdm")
                    jxcdmcs = resp.json()[0][i].get("jxcdmc")
                    kcmcs = resp.json()[0][i].get("kcmc")
                    teaxms = resp.json()[0][i].get("teaxms")
                    xqs = resp.json()[0][i].get("xq")
                    zcs = resp.json()[0][i].get("zc")
                    course = {
                        "jcdm":jcdms,
                        "jxcdmc":jxcdmcs,
                        "kcmc":kcmcs,
                        "teaxm":teaxms,
                        "xq":xqs,
                        "zc":zcs
                    }
                    curriculum.append(course)
                print(curriculum)
                curriculum = []
            else:
                print(f"第{pn}开始没课")
                break
        except Exception as e:
            print(e)
        pn+=1
