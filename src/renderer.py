import curses
import threading
import time
import sys

currentTime = time.time()

# Get the change in time since last call
def getDeltaTime():
    global currentTime

    deltaTime = time.time() - currentTime
    currentTime = time.time()

    return deltaTime

# Print an object to the screen
def printObj(stdscr, obj):
    x, y = obj.x, obj.y
    for offset, line in enumerate(obj.text.splitlines()):
        stdscr.addstr(y + offset, x, line)

# Class to render objects to the screen 
class Renderer:
    def __init__(self, frameRate=30):
        self.gameObjects = []
        self.frameRate = frameRate

    def addObj(self, obj):
        self.gameObjects.append(obj)

    def render(self, stdscr):
        for obj in gameObjects:
            printMultiline(stdscr, obj)

    def renderLoop(self, stdscr):
        while True:
            deltaTime = getDeltaTime()

            for obj in self.gameObjects:
                printObj(stdscr, obj)

            # Match the frame rate
            targetDelay = 1/self.frameRate
            if targetDelay > deltaTime:
                time.sleep(targetDelay - deltaTime)

    # Starts rendering on a separate thread
    def start(self, stdscr):
        global currentTime

        currentTime = time.time()

        try:
            threading.Thread(target=self.renderLoop, args=(stdscr,)).start()
        except (KeyboardInterrupt, SystemExit):
            sys.exit()

# Represents a gameobject
class GameObject:
    def __init__(self, y=0, x=0, text=''):
        self.text = text
        self.x = x
        self.y = y
        self.enabled = True
