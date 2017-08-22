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
		    # Clear the screen
		    stdscr.erase()
		    deltaTime = getDeltaTime()

		    # Draw all of the objects in order
		    for obj in self.gameObjects:
		    	printObj(stdscr, obj)

		    # Match the frame rate
		    targetDelay = 1/self.frameRate
		    if targetDelay > deltaTime:
		    	time.sleep(targetDelay - deltaTime)

	# Clear all of the objects on the screen
	def clearObjects(self):
		self.gameObjects = []

	# Remove an object from the render list
	def removeObj(obj):
		self.gameObjects.remove(obj)

	# Starts rendering on a separate thread
	def start(self, stdscr):
		global currentTime

		currentTime = time.time()

		threading.Thread(target=self.renderLoop, args=(stdscr,), daemon=True).start()
