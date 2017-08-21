import curses
from curses import wrapper

import renderer
import userinput
import game
import time

ren = renderer.Renderer()
usrinp = userinput.UserInput()

def main(stdscr):
	stdscr.clear()
	stdscr.nodelay(1)
	curses.curs_set(0)

	ren.start(stdscr)
	usrinp.start(stdscr)

	obj = game.GameObject(10, 10, "Hello World")
	ren.addObj(obj)
	for i in range(100):
		time.sleep(1)
		k = usrinp.lastKey
		if k == -1:
			obj.text = "No key pressed"
		else:
			obj.text = str(unichr(k))


if __name__ == "__main__":
	wrapper(main)
