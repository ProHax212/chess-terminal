# Create a scene by placing asset objects around the screen
import resources
import renderer
import framerate
import userinput
import game

from curses import wrapper
import curses.textpad

usrinp = userinput.UserInput()
ren = renderer.Renderer()
fr = framerate.FrameRate()

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
	stdscr.nodelay(1)
	stdscr.clear()

	prompt = "Enter asset name: "

	# Create Renderer
	#global ren
	#ren.start(stdscr)

	# Create input engine
	#global usrinp
	#usrinp.start(stdscr)

	# Framerate
	global fr

	height, width = stdscr.getmaxyx()

	#promptObj = game.GameObject(height-1, 0, prompt)
	#resourceNameObj = game.GameObject(height-1, len(promptObj.text)+1, "")

	#ren.addObj(promptObj)
	while True:
		height, width = stdscr.getmaxyx()

		#promptObj.y = height-1

		# Create a window to use the textbox in
		stdscr.addstr(height-2, 0, prompt)
		win = stdscr.subwin(height-2, len(prompt)+1)
		tb = curses.textpad.Textbox(win, insert_mode=True)
		resourceName = tb.edit().strip()	

		try:
			resourceAscii = resources.getResource(resourceName)
			stdscr.addstr(0, 0, resourceAscii)
			#obj = game.GameObject(0, 0, resources.getResource(resourceName))
			#ren.addObj(obj)
		except KeyError:
			stdscr.addstr(height-3, 0, "Resource not found")
			#ren.addObj(game.GameObject(height-2, 0, "Resource not found"))
				
		stdscr.erase()
		stdscr.refresh()

if __name__ == '__main__':
	wrapper(main)	
