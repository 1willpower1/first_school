from school.广东石油化工学院.data.achievement.achievement import  achievement
from school.广东石油化工学院.data.curriculum.curriculum import curriculum
def data(xnxqdm,zc,page):
    try:
        curriculum(xnxqdm, zc)
        achievement(page)
    except Exception as e:
        print(e)

