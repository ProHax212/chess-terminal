# Create a scene by placing asset objects around the screen
import resources
import renderer
import game
import userinput

from curses import wrapper
import curses.textpad

usrinp = userinput.UserInput()
ren = renderer.Renderer()

def moveResource(obj):
	global ren
	global usrinp

	# Move resource around
	x = y = 0
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

def main(stdscr):
	prompt = "Enter asset name: "
	stdscr.nodelay(1)
	stdscr.clear()

	# Create Renderer
	global ren
	ren.start(stdscr)

	# Create input engine
	global usrinp
	usrinp.start(stdscr)

	height, width = stdscr.getmaxyx()

	promptObj = game.GameObject(height-1, 0, prompt)
	resourceNameObj = game.GameObject(height-1, len(promptObj.text)+1, "")

	ren.addObj(promptObj)
	ren.addObj(resourceNameObj)
	while True:
		height, width = stdscr.getmaxyx()

		promptObj.y = height-1
		resourceNameObj.y = height-1

		k = usrinp.lastKey

		if k != -1:
			if k == 10:
				moveResource(game.GameObject(0, 0, resources.getResource(resourceNameObj.text.strip())))
			else:
				resourceNameObj.text = k

		# Create a window to use the textbox in
#		win = stdscr.subwin(height-1, len(prompt)+1)
#
#		tb = curses.textpad.Textbox(win, insert_mode=True)
#
#		resourceName = tb.edit().strip()	

		# Get the resource


		k = usrinp.lastKey
		if k == ord('q'):
			ren.removeObj(obj)
			break

if __name__ == '__main__':
	wrapper(main)	
