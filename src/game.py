import game

# Base class for the type of game you want to make
class Game:
	def __init__(self, stdscr, ren):
		self.ren = ren
		self.gameObjects = []
		self.stdscr = stdscr

# Represents a gameobject for a game
class GameObject:
    def __init__(self, y=0, x=0, text=''):
        self.text = text
        self.x = x
        self.y = y
        self.enabled = True
        self.width, self.height = self.getWidthHeight(text)

    # Get the width and height (cols, rows) for the text
    def getWidthHeight(self, string):
        width = height = 0

        for line in string.splitlines():
            width = max(width, len(line))
            height += 1

        return width, height
