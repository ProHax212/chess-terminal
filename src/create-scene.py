# Create a scene by placing asset objects around the screen
import resources
import renderer
import game
import userinput

from curses import wrapper
import curses.textpad

def main(stdscr):
	prompt = "Enter asset name: "
	curses.curs_set(0)
	stdscr.nodelay(1)

	ren = renderer.Renderer()
	ren.start(stdscr)

	usrinp = userinput.UserInput()
	usrinp.start(stdscr)

	stdscr.clear()
	while True:
		height, width = stdscr.getmaxyx()
		win = curses.newwin(1, width - len(prompt) - 1, height-1, len(prompt)+1)

		ren.addObj(game.GameObject(height-1, 0, prompt))

		#stdscr.erase()
		#stdscr.addstr(height-1, 0, prompt)
		#stdscr.refresh()

		tb = curses.textpad.Textbox(win, insert_mode=True)
		tb.strip_spaces=True

		resourceName = tb.edit().strip()

		# Get the resource
		try:
			resourceAscii = resources.getResource(resourceName)	
		except KeyError:
			ren.clearObjects()
			ren.addObj(game.GameObject(height-2, 0, 'Resource not found'))
			#stdscr.addstr(height-2, 0, 'Resource not found')
			continue

		# Move resource around
		x = y = 0
		obj = game.GameObject(y, x, resourceAscii)
		ren.addObj(obj)
		while True:
			height, width = stdscr.getmaxyx()
			k = usrinp.lastKey
			# UP
			if k == ord('k'):
				y -= 1
				y = max(y, 0)
				obj.y = y
			# DOWN
			elif k == ord('j'):
				y += 1
				y = min(y, height - obj.height)
				obj.y = y
			# LEFT
			elif k == ord('h'):
				pass
			# RIGHT
			elif k == ord('l'):
				pass
			# QUIT
			elif k == ord('q'):
				break

		k = usrinp.lastkey
		if k == ord('q'):
			break

if __name__ == '__main__':
	wrapper(main)	
