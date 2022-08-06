# *-*encoding:utf-8
"""
    一个简单的字符串拼接，目的是为了测试制作GUI
"""


def get_info(name, age):
    # 励志ing...
    a = '  遥想公瑾当年，小乔初嫁了，羽扇纶巾，雄姿英发...'
    zhouyu_age = 23
    count = zhouyu_age-age
    if count > 0:
        count = str(count)
        b = "  '{}',公元198年，孙策周瑜当时都是23岁，都建功立业了，你只比他小{}岁，加油啊，少年，还有机会！".format(name, count)
    else:
        count = str(count)
        b = "  '{}',公元198年，孙策周瑜当时都是23岁，都建功立业了，你比人家还大{}岁，要加把劲啊".format(name, count)
    c = a+'\n\n'+b+'\n\n'
    return c


c = get_info('哈哈',13)
print(c)

