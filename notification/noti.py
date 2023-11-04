from plyer import notification
import time

timeout=None
if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Hacker***",
            message="You let me hack your PC.",
            app_icon=r"C:\Users\Deepu\Desktop\python\notification\emblemimportant_103451.ico",
            timeout=5 )
        time.sleep(10)