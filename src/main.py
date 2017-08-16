import curses
import curses.textpad
from curses import wrapper
import time

'''
TODO: Add a class for gameobjects
Seperate thread will loop through list of gameobjects and render to the screen
This thread will loop at the desired framerate
Whenever you want to render something new, just add it to the list
'''

res_path = '../res/'
title_path = res_path + 'title-chess.txt'

instructions_str = '''Welcome to terminal chess.  It's not as sad as it sounds, it's actually a really cool game!  Here are the instructions:
Press any key to continue ...'''

currentTime = int(round(time.time() * 1000))
frameRate = 30

# Return the current system time in milliseconds
def getCurrentTime():
	return int(round(time.time() * 1000))

def getDeltaTime():
	deltaTime = getCurrentTime() - currentTime

	# Update current time
	global currentTime 
	currentTime = getCurrentTime()

	return deltaTime

# Print multiple lines to the console that are separated by newlines
def printMultiLine(stdscr, strings, y, x):
	for offset, line in enumerate(strings.splitlines()):
		stdscr.addstr(y+offset, x, line)

def printInstructions(stdscr):
	title_str = ""
	with open(title_path, 'r') as f:
		title_str = f.read()

	# Wait for user to hit a key
	while True:
		k = stdscr.getch()
		if k != -1:
			break

		printMultiLine(stdscr, title_str, 0, 0)
		printMultiLine(stdscr, instructions_str, 25, 0)
		stdscr.refresh()

# Calibration function to move art around the screen
def calibration(stdscr, strings):
	for string in strings:
		x = y = 5
		k = 0
		while k != ord('n'):
			deltaTime = getDeltaTime()

			stdscr.erase()
			k = stdscr.getch()
			printMultiLine(stdscr, string, y,  x)

			maxY, maxX = stdscr.getmaxyx()
			# UP
			if k == ord('k'):
				y -= 1
				y = max(y, 0)
			# DOWN
			elif k == ord('j'):
				y += 1
				y = min(y, maxY)
			# LEFT
			elif k == ord('h'):
				x -= 1
				x = max(x, 0)
			# RIGHT
			elif k == ord('l'):
				x += 1
				x = min(x, maxX)
			
			stdscr.refresh()

			# Wait to hit desired frame rate
			desired_delta = int(round(1/frameRate))
			difference = desired_delta - deltaTime
			if difference > 0:
				sleep(float(difference/1000))

# Main function
def main(stdscr):
	# Init
	stdscr.nodelay(True)
	curses.curs_set(0)

	# Calibrate the art
	calibration(stdscr, ['art one', 'art two', 'art three'])

	# Clear the screen
	stdscr.clear()

	printInstructions(stdscr)

# Entrypoint
if __name__ == '__main__':
	wrapper(main)
