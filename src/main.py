import curses
import curses.textpad
from curses import wrapper
import time

def main(stdscr):
	# Clear the screen
	stdscr.clear()
	stdscr.refresh()

if __name__ == '__main__':
	wrapper(main)
