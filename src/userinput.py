# Get the user input at a certain rate (frame rate)
import time
import threading

currentTime = time.time()

def getDeltaTime():
	global currentTime
	deltaTime = time.time() - currentTime
	currentTime = time.time()

	return deltaTime

class UserInput:
	def __init__(self, framerate=30):
		self.lastKey = ''
		self.framerate = framerate

	def inputLoop(self, stdscr):
		while True:
			self.lastKey = stdscr.getch()

			# Wait for the framerate
			desiredDelta = 1/self.framerate
			delta = getDeltaTime()
			if desiredDelta > delta:
				time.sleep(desiredDelta - delta)

	def start(self, stdscr):
        	threading.Thread(target=self.inputLoop, args=(stdscr,), daemon=True).start()
