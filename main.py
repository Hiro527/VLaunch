"""
VLaunch (c) 2022 Hiro527
"""

import psutil
import time
import threading
import subprocess
from plyer import notification

VALORANT_PATH = 'C:\Riot Games\VALORANT\live\VALORANT.exe'
CLAUNCH_PATH = 'C:\Program Files\CLaunch\CLaunch.exe'

CLAUNCH_PID = 0


def checkProcess():
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
        notification.notify(
            title="自動検知モード",
            message="CLaunchを停止しました",
            app_name="VLaunch",
            timeout=5
        )
    if not VALORANT_DETECTED:
        if not CLAUNCH_DETECTED:
            # VALORANT未検出でCLaunchが動いていないときの処理
            subprocess.Popen(r'powershell ./launch.ps1', shell=True)
            print('[INFO] CLaunch Started')
            notification.notify(
                title="自動検知モード",
                message="CLaunchを起動しました。",
                app_name="VLaunch",
                timeout=5
            )

# 定期実行


def setInterval(s, callback):
    t0 = time.time()
    tN = 0
    while True:
        thread = threading.Thread(target=callback)
        thread.start()
        tN = ((t0 - time.time()) % s) or s
        time.sleep(tN)


setInterval(5, checkProcess)
