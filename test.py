import os
import time
from tracemalloc import start

adbInputTap = 'adb shell input tap '
articleMain = 'shuitie' # 水贴内容
articleTitle = 'shuitie' # 水贴标题

genshinPubPosition = '145 420'
zzzCoffeeHubPosition = '145 900'
honkaiSRWaitingRoomPosition = '145 1230'
hongkai3Deck = '145 1530'

def intoArticle():
    print('开始水贴')
    print('进入水贴')
    os.system(adbInputTap + '540 2250')
    time.sleep(.5)
    os.system(adbInputTap + '380 1600')
    time.sleep(1.5)

def inputArticle():
    print('输入水贴内容')
    os.system('adb shell input text ' + articleMain)
    time.sleep(0.5)
    os.system(adbInputTap + '120 1630')

def inputArticleTitle():
    print('输入水贴标题')
    os.system(adbInputTap + '100 360')
    time.sleep(0.5)
    os.system('adb shell input text ' + articleTitle)
    time.sleep(0.5)
    os.system(adbInputTap + '120 1630')
    time.sleep(0.5)

def talkClass():
    print('搜索 [每日一水] 并选择')
    os.system(adbInputTap + '200 570')
    os.system('adb shell input text meiriyishui')
    time.sleep(0.5)
    os.system(adbInputTap + '120 1630')
    time.sleep(0.5)
    os.system(adbInputTap + '100 700')
    time.sleep(0.5)
    os.system(adbInputTap + '1000 150')


def sendArticle():
    print('发布按钮')
    os.system(adbInputTap + '1000 150')

def removeArticle():
    print('删除帖子')
    os.system(adbInputTap + '980 150')
    time.sleep(0.5)
    os.system(adbInputTap + '670 2050')
    time.sleep(0.5)
    os.system(adbInputTap + '730 1280')



# 水贴主任务

print('选择板块地址')
print('[0]全走一遍~ [1]原神/酒馆 [2]绝区零/咖啡馆 [3]崩坏：星穹铁道/候车室 [4]崩坏3/甲板 [5]大别野/校园 [6]崩坏学园2/学院 [7]未定事件博/律所')

articleTaskChoise = input('任务: ')

if(articleTaskChoise == '0' or articleTaskChoise == ''):
    print('开始执行: 全都走一遍咯~')
    intoArticle()
    inputArticle()
    inputArticleTitle()
    sendArticle()
    time.sleep(0.5)
    print('选择 [1]原神/酒馆')
    os.system(adbInputTap + genshinPubPosition)
    time.sleep(0.5)
    talkClass()
    time.sleep(1)
    print('发布')
    time.sleep(1)
    os.system(adbInputTap + '1000 150')
    input('请检查是否弹出验证，按任意键后执行删除行为')
    removeArticle()
    print('任务结束')

elif(articleTaskChoise == '1'):
    startNumber = 1
    while startNumber < 3:
        print('开始在:[1]原神/酒馆 水贴')
        intoArticle()
        inputArticle()
        inputArticleTitle()
        sendArticle()
        time.sleep(0.5)
        print('选择 [1]原神/酒馆')
        os.system(adbInputTap + genshinPubPosition)
        time.sleep(0.5)
        talkClass()
        time.sleep(1)
        print('发布')
        time.sleep(1)
        os.system(adbInputTap + '1000 150')
        input('请检查是否弹出验证，按任意键后执行删除行为')
        removeArticle()
        print('第' + str(startNumber) + '任务结束')
        startNumber += 1
        time.sleep(1)
    print('任务结束')
    
elif(articleTaskChoise == '2'):
    pass
elif(articleTaskChoise == '3'):
    pass
elif(articleTaskChoise == '4'):
    pass
elif(articleTaskChoise == '5'):
    pass
elif(articleTaskChoise == '6'):
    pass
elif(articleTaskChoise == '7'):
    pass
elif(articleTaskChoise == '114514'):
    print('哼，哼，啊！！！！！！！！！')
else:
    print('未知命令')
