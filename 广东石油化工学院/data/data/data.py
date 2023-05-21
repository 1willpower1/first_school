from school.广东石油化工学院.data.achievement.achievement import  achievement
from school.广东石油化工学院.data.curriculum.curriculum import curriculum
def data(xnxqdm,zc,page,username,password,flag=False):
    try:
        curriculum(xnxqdm,zc,username,password,flag)
        achievement(page,username,password,flag)
    except Exception as e:
        print(e)

