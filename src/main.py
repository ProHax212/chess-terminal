import curses
import curses.textpad
from curses import wrapper

import renderer

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

currentTime = time.time()
frameRate = 30

# Object to render objects to the screen
ren = renderer.Renderer()

def getDeltaTime():
        global currentTime
        deltaTime = time.time() - currentTime

	# Update current time
        currentTime = time.time()
        return deltaTime

# Print multiple lines to the console that are separated by newlines
def printMultiLine(stdscr, strings, y, x):
	for offset, line in enumerate(strings.splitlines()):
		stdscr.addstr(y+offset, x, line)

def printInstructions(stdscr):
    title_str = ""
    with open(title_path, 'r') as f:
        title_str = f.read()
    title_obj = renderer.GameObject(0, 0, title_str)
    instructions_obj = renderer.GameObject(25, 0, instructions_str)

    ren.addObj(title_obj)
    ren.addObj(instructions_obj)

    # Wait for user to hit a key
    while True:
            k = stdscr.getch()
            if k != -1:
                    break

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
			desired_delta = 1/frameRate
			difference = desired_delta - deltaTime
			if difference > 0:
				time.sleep(difference)

# Main function
def main(stdscr):
    # Init
    stdscr.nodelay(True)
    curses.curs_set(0)
    stdscr.clear()

    # Start the renderer
    ren.start(stdscr)

    printInstructions(stdscr)

    # Game loop

# Entrypoint
if __name__ == '__main__':
	wrapper(main)
