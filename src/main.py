import curses
import curses.textpad
from curses import wrapper

import renderer
import resources as res
import chess

from game import GameObject

import time

currentTime = time.time()
frameRate = 30

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

# Return the string in the resource
def getResource(resourcePath):
    returnStr = ""
    with open(resourcePath, 'r') as f:
        returnStr = f.read()

    return returnStr

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

    # Create Renderer
    ren = renderer.Renderer(frameRate)
    ren.start(stdscr)

    # Create game
    chessGame = chess.ChessGame(stdscr, ren)
    chessGame.start()

    #ren.addObj(GameObject(0, 0, res.getResource('board')))
    #ren.addObj(GameObject(0, 0, res.getResource('pawn-white')))
    #ren.addObj(GameObject(5, 0, res.getResource('knight-white')))
    #ren.addObj(GameObject(10, 0, res.getResource('bishop-white')))
    #ren.addObj(GameObject(0, 7, res.getResource('king-white')))
    #ren.addObj(GameObject(5, 7, res.getResource('queen-white')))
    #ren.addObj(GameObject(10, 7, res.getResource('rook-white')))

    # Game loop
#    while True:
#        deltaTime = getDeltaTime()
#
#        # Get Input
#        k = stdscr.getch()
#        if k != -1:
#            break
#
#        # Wait to keep framerate
#        desiredDelta = 1/frameRate
#        if deltaTime < desiredDelta:
#            time.sleep(desiredDelta - deltaTime)

# Entrypoint
if __name__ == '__main__':
	wrapper(main)
