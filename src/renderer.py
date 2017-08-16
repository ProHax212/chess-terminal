import curses

# Class to render objects to the screen 
class Renderer():
	gameObjects = []

# Represents a gameobject
class GameObject():
	x, y = 0, 0
	text = ""
