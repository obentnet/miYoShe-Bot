import os
import time
sTime = 1
while 1<2:
    os.system('adb shell input tap 540 1000') # 2244
    sTime += 1
    print('ok ' + str(sTime))
    