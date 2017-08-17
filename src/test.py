import time

currentTime = time.time()
targetFrameRate = 1

def getDeltaTime():
    global currentTime
    deltaTime = time.time() - currentTime

    # Update current time
    currentTime = time.time()

    return deltaTime

while(True):
    print("Frame")
    deltaTime = getDeltaTime()
    targetDelay = 1/targetFrameRate

    if targetDelay > deltaTime:
        time.sleep(targetDelay - deltaTime)
