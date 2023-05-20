#登录时使用的表头
headers = {
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
"Connection": "keep-alive",
"Content-Length":"52",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Cookie": "TWFID=8328cd0fa9b6ca13; JSESSIONID=A8C308D39F091A3086D237BB6BE27106; browserID=1952807128",
"Host": "jwxt.gdupt.edu.cn",
"Origin": "https://jwxt.gdupt.edu.cn",
"Referer": "https://jwxt.gdupt.edu.cn/",
"sec-ch-ua": 'Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}
# 课表时需要传递的数据
params1 = {"xnxqdm":202202,"zc":12}
# 课表时的请求表头
headers2 = {
"Accept":"application/json,text/javascript,*/*; q=0.01",
"Accept-Encoding":"gzip,deflate,br",
"Accept-Language":"zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
"Connection":"keep-alive",
"Cookie":"TWFID=8328cd0fa9b6ca13; browserID=1952807128; JSESSIONID=A21D2693EB04D6916A349C6BA6B2D59B",
"Host": "jwxt.gdupt.edu.cn",
'Referer': 'https://jwxt.gdupt.edu.cn/xsgrkbcx!xskbList.action?xnxqdm=202202&zc=12',
"sec-ch-ua":'"Google Chrome";v="111","Not(A:Brand";v="8", "Chromium";v="111"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform":'"Windows"',
"Sec-Fetch-Dest":"empty",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Site":"same-origin",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
"X-Requested-With":"XMLHttpRequest"
}
# 成绩时的请求表头
headers3 = {
"Accept":"application/json,text/javascript,*/*;q=0.01",
"Accept-Encoding":"gzip,deflate,br",
"Accept-Language":"zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
"Connection":"keep-alive",
"Content-Length":"60",
"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
"Cookie":"TWFID=8328cd0fa9b6ca13; browserID=1952807128; JSESSIONID=A21D2693EB04D6916A349C6BA6B2D59B",
"Host":"jwxt.gdupt.edu.cn",
"Origin":"https://jwxt.gdupt.edu.cn",
"Referer":"https://jwxt.gdupt.edu.cn/xskccjxx!xskccjList.action?firstquery=1",
"sec-ch-ua":'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform":'"Windows"',
"Sec-Fetch-Dest":"empty",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Site":"same-origin",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
"X-Requested-With":"XMLHttpRequest"
}
data = {
    "xnxqdm":"",
    "page":"1",
    "rows":"20",
    "sort":"xnxqdm,kcbh,ksxzdm",
    "order":"asc"
}
