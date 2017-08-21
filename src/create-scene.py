# Create a scene by placing asset objects around the screen
import resources
import renderer

from curses import wrapper
import curses.textpad

def main(stdscr):
	prompt = "Enter asset name: "
	curses.curs_set(0)

	# Where the user types in the resource
	win = curses.newwin(3, 20, 10, 10)

	stdscr.clear()
	while True:
		height, width = stdscr.getmaxyx()
		win = curses.newwin(1, width - len(prompt) - 1, height-1, len(prompt)+1)

		stdscr.erase()
		stdscr.addstr(height-1, 0, prompt)
		stdscr.refresh()

		tb = curses.textpad.Textbox(win, insert_mode=True)
		tb.strip_spaces=True
		resourceName = tb.edit().strip()

		with open('test.txt', 'w') as f:
			f.write(resourceName)

		# Get the resource
		try:
			resourceAscii = resources.getResource(resourceName)	
		except KeyError:
			stdscr.addstr(height-2, 0, 'Resource not found')

		# Move resource around

		k = stdscr.getch()
		if k == ord('q'):
			break

if __name__ == '__main__':
	wrapper(main)	
