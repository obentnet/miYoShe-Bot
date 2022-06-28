# miHoYo AUTOBBS
# 米游社bbs自动签到
# v 0.1

from enum import auto
import os
import time

adbInputTap = 'adb shell input tap '

cutLine = '=================================================' # 分割线

openApp = 'adb shell am start com.mihoyo.hyperion/com.mihoyo.hyperion.main.HyperionMainActivity' # 打开APP
getWm = 'adb shell wm size' # 获取当前手机分辨率
autoBack = 'adb shell input keyevent BACK' # 全局返回
autoTalkZone = 'adb shell input tap 900 650' # 通用讨论区
autoChangeBBS = 'adb shell input swipe 900 1000 500 1000' # 通用切换板块



# 通用点赞分享
def autoLikeAndShare():
    print(cutLine)
    print('执行通用帖子分享点赞')
    print('点赞')
    os.system('adb shell input tap 720 2270')
    time.sleep(1)
    print('点赞结束')
    print('进行分享')
    os.system(adbInputTap + '980 160')
    time.sleep(1)
    os.system('adb shell input tap 100 1800')
    time.sleep(1)
    os.system(autoBack)
    time.sleep(2)
    os.system(autoBack)

## 讨论区任务
def TalkZone():
    print(cutLine)
    print('讨论区签到')
    os.system('adb shell input tap 900 650')
    print('执行完成，休眠3s')
    time.sleep(3)
    print('返回主页')
    os.system(autoBack)
    time.sleep(1)

def autoArticleCheck():
    print(cutLine)
    print('开始通用帖子查看')

    # 前四次

    sc = 0
    while sc < 10:
        print('刷新')
        os.system('adb shell input swipe 560 850 560 1600')
        time.sleep(2)
        print('模拟点击')
        os.system('adb shell input tap 550 1660')
        print('进入帖子，等待1秒')
        time.sleep(1)
        print('点赞')
        os.system('adb shell input tap 720 2270')
        time.sleep(1)
        print('点赞结束')
        print('返回')
        os.system(autoBack)
        time.sleep(2)
        sc += 1

    print('第十次')
    print('刷新')
    os.system('adb shell input swipe 560 850 560 1600')
    time.sleep(3)
    print('模拟点击')
    os.system('adb shell input tap 550 1660')
    print('进入帖子，等待2秒')
    time.sleep(2)

###################################################################################

print('确保手机打开 开发者选项')
print('建议板块排序为：原神 → 绝区零 → 崩坏：星穹铁道 → 崩坏3 → 大别野')
print('推荐屏幕分辨率为：1080x2340px')
print('当前手机分辨率为：')
os.system(getWm)
print('适配机型：小米10s （没有别的手机用来测试了，理论上只要是这个分辨率的都可以用')
input('请按任意键')
print('原神BBS任务')

print('打开米游社')

os.system(openApp)
time.sleep(2)
# 原神任务区
## 讨论区任务
TalkZone()
## 执行帖子查看
autoArticleCheck()
## 通用点赞分享
autoLikeAndShare()


print('原神BBS任务区执行完毕')
print('准备执行 绝区零板块任务')
time.sleep(1)
os.system(autoChangeBBS)
time.sleep(1)
print('切换板块:原神 → 绝区零')

# 绝区零任务区
## 讨论区任务
TalkZone()
## 执行帖子查看
autoArticleCheck()
## 通用点赞分享
autoLikeAndShare()

print('绝区零任务区执行完毕')
print('准备执行 崩坏：星穹铁道板块任务')
time.sleep(1)
os.system(autoChangeBBS)
time.sleep(1)
print('切换板块:绝区零 → 崩坏：星穹铁道')

# 崩坏：星穹铁道 任务区
## 讨论区任务
TalkZone()
## 执行帖子查看
autoArticleCheck()
## 通用点赞分享
autoLikeAndShare()

print('崩坏：星穹铁道任务区执行完毕')
print('准备执行 崩坏3板块任务')
time.sleep(1)
os.system(autoChangeBBS)
time.sleep(1)
print('切换板块:崩坏：星穹铁道 → 崩坏3')

# 崩坏：3 任务区
## 讨论区任务
TalkZone()
## 执行帖子查看
autoArticleCheck()
## 通用点赞分享
autoLikeAndShare()

print('崩坏：3任务区执行完毕')
print('准备执行 大别野板块任务')
time.sleep(1)
os.system(autoChangeBBS)
time.sleep(1)
print('切换板块:崩坏3 → 大别野')

# 大别野
## 讨论区任务
TalkZone()
## 执行帖子查看
print('开始大别野专用帖子查看')
# 前四次
sc = 0
while sc < 4:
    print('刷新')
    os.system('adb shell input swipe 560 850 560 1600')
    time.sleep(2)
    print('模拟点击')
    os.system('adb shell input tap 550 1000')
    print('进入帖子，等待1秒')
    time.sleep(1)
    print('点赞')
    os.system('adb shell input tap 720 2270')
    time.sleep(1)
    print('点赞结束')
    print('返回')
    os.system(autoBack)
    time.sleep(2)
    sc += 1
print('第五次')
print('刷新')
os.system('adb shell input swipe 560 850 560 1600')
time.sleep(3)
print('模拟点击')
os.system('adb shell input tap 550 1000')
print('进入帖子，等待2秒')
time.sleep(2)

## 通用点赞分享
autoLikeAndShare()



print(cutLine)
print('签到/分享/点赞 均已结束')
print('执行：水贴')