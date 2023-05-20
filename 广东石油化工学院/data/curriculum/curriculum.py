import requests
from school.广东石油化工学院.data.login.config import headers2,params1
#登录的网址
#具体数据的网址
#zc = 填现在的周次 xnxqdm:年级数+第几学期 第一学期:01
def curriculum(xnxqdm,zc):
    pn = 1
    params = {"xnxqdm": xnxqdm, "zc": zc}
    curriculum = []
    while 1:
        url = f"https://jwxt.gdupt.edu.cn/xsgrkbcx!getKbRq.action?xnxqdm=202202&zc={pn}"
        try:
            resp = requests.session().get(params=params,url=url,headers=headers2)
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
