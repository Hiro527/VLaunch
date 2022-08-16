'''
VLaunch (c) 2022 Hiro527
'''

import psutil
import threading
from pystray import Icon, Menu, MenuItem
import time
import subprocess
from PIL import Image

VALORANT_PATH = 'C:\Riot Games\VALORANT\live\VALORANT.exe'
CLAUNCH_PATH = 'C:\Program Files\CLaunch\CLaunch.exe'

CLAUNCH_PID = 0

def checkProcess(icon):
    global CLAUNCH_PATH, CLAUNCH_PID, VALORANT_PATH
    VALORANT_DETECTED = False
    CLAUNCH_DETECTED = False
    proc = psutil.process_iter()
    for i in proc:
        try:
            if (i.exe() == CLAUNCH_PATH):
                CLAUNCH_DETECTED = True
                CLAUNCH_PID = i.pid
            if (i.exe() == VALORANT_PATH):
                VALORANT_DETECTED = True
        except psutil.AccessDenied:
            # プロセスが管理者権限で動いてる場合の処理
            continue
    if VALORANT_DETECTED and CLAUNCH_DETECTED:
        # VALORANTとCLaunch検出時の処理
        proc = psutil.Process(CLAUNCH_PID)
        proc.terminate()
        print('[INFO] CLaunch has been terminated')
        icon.notify('CLaunchを停止しました', '自動検知モード')
    if not VALORANT_DETECTED:
        if not CLAUNCH_DETECTED:
            # VALORANT未検出でCLaunchが動いていないときの処理
            subprocess.Popen(r'powershell ./launch.ps1', shell=True)
            print('[INFO] CLaunch Started')
            icon.notify('CLaunchを起動', '自動検知モード')


# 定期実行
def setInterval(icon):
    icon.visible = True
    s = 5
    t0 = time.time()
    tN = 0
    while icon.visible:
        thread = threading.Thread(target=checkProcess, args=[icon])
        thread.start()
        tN = ((t0 - time.time()) % s) or s
        time.sleep(tN)


# 終了
def quitApp(icon):
    icon.visible = False
    TrayIcon.stop()

TrayImage = Image.open('./assets/VLaunch.ico')
TrayMenu = Menu(
    MenuItem(
        '終了',
        quitApp
        )
)
TrayIcon = Icon(name='VLaunch', icon=TrayImage, title='自動検知モード', menu=TrayMenu)
TrayIcon.run(setInterval)