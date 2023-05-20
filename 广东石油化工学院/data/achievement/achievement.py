import  requests
from school.广东石油化工学院.data.login.config import headers3,data
def achievement(page):
    achievement = [
    ]
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
        resp = requests.session().post(data=data,headers=headers3,url=url)
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
