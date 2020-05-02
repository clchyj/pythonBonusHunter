# -*- coding: utf-8 -*-
import time
import subprocess
import random

def connect():
    return subprocess.run("adb connect 127.0.0.1:62001",shell=True)
def move_up():
    state=connect()
    print("状态：",state)
    cmd="adb -s 127.0.0.1:62001 shell input swipe 310 650 310 200"
    cmd_point="adb -s 127.0.0.1:62001 shell input tap 310 310"

    for i in range(1000):
        index = random.sample(range(5,15),10)
        print(index)
        res=subprocess.run(cmd,shell=True)
        res_point=subprocess.run(cmd_point,shell=True)
        time.sleep(index[0])
        print(res)
        print("------------------------------")
        res=int(str(res).replace(")","").split("=")[-1])
        print(res)
        print("------------------------------")
        if res!=0:
            connect()
        time.sleep(5)
        print("第%d个视频"%i)
if __name__=="__main__":
    move_up()
