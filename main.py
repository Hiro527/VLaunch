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

def checkProc() -> None:
    global CLAUNCH_PATH, CLAUNCH_PID, VALORANT_PATH
    VALORANT_DETECTED = False
    CLAUNCH_DETECTED = False
    proc = psutil.process_iter()
    for i in proc:
        try:
            if (i.exe() == CLAUNCH_PATH):
                CLAUNCH_PID = i.pid
                CLAUNCH_DETECTED = True
            if (i.exe() == VALORANT_PATH):
                VALORANT_DETECTED = True
                if (CLAUNCH_PID != 0):
                    proc = psutil.Process(CLAUNCH_PID)
                    proc.terminate()
                    CLAUNCH_PID = 0
                    print('[INFO] CLaunch has been terminated')
                    notification.notify(
                        title="自動検知モード",
                        message="CLaunchを停止しました",
                        app_name="VLaunch",
                        timeout=5
                    )
        except psutil.AccessDenied:
            continue
    if not CLAUNCH_DETECTED:
        CLAUNCH_PID = 0
    if (not VALORANT_DETECTED) and (not CLAUNCH_DETECTED):
        subprocess.Popen(r'powershell ./launch.ps1', shell=True)
        print('[INFO] CLaunch Started')
        notification.notify(
            title="自動検知モード",
            message="CLaunchを起動しました。",
            app_name="VLaunch",
            timeout=5
        )

# 定期実行
def setInterval(s: int, callback: function) -> None:
    t0 = time.time()
    tN = 0
    while True:
        thread = threading.Thread(target=callback)
        thread.start()
        tN = ((t0 - time.time()) % s) or s
        time.sleep(tN)

setInterval(5, checkProc)