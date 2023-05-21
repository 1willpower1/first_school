from school.广东石油化工学院.data.login.login import login
from school.广东石油化工学院.data.data.data import data
#输入对应的用户名和密码,执行logi_NCnUWREP即可登录
def login_NCUWREP(username,password):
    login(username,password)
# xnxqdm:年级数+第几学期 列入 202202 表示2022级第2学期
# zc:填入周次如何数字都
# page:填入一共有多少页成绩数据
def getData_NCUWREP(xnxqdm,zc,page,username,password):
    data(xnxqdm,zc,page,username,password)
