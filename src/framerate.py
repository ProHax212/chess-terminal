import time

# Class to run a loop at a certain framerate
class FrameRate:
	def __init__(self, framerate=30):
		self.framerate=framerate
		self.currentTime = time.time()

	# Update the current timestamp (call at beginning of a loop)
	def update(self):
		self.currentTime = time.time()

	# Sleep the thread based on the framerate
	def wait(self):
		delta = time.time() - self.currentTime
		desiredDelta = 1/self.framerate

		# Wait
		if desiredDelta > delta:
			time.sleep(desiredDelta - delta)
