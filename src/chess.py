import resources
import game

from enum import Enum

# Represents a chess game
class ChessGame(game.Game):
	def __init__(self, stdscr, ren):
		#Constructor of parent
		super().__init__(stdscr, ren)

		self.board = [] # 2D representation of game board
		for i in range(8):
			newRow = []
			for j in range(8):
				newRow.append(None)
			self.board.append(newRow)

		self.resetGame()

	# First screen that the user sees
	def mainMenu(self):
	    title_obj = game.GameObject(0, 0, resources.getResource('title'))
	    instructions_obj = game.GameObject(25, 0, resources.getResource('instructions'))

	    self.ren.addObj(title_obj)
	    self.ren.addObj(instructions_obj)

	    # Wait for user to hit a key
	    while True:
		    k = self.stdscr.getch()
		    if k != -1:
			    break

	    # Clear the rendered objects 
	    self.ren.clearObjects()

	# Reset the game pieces
	def resetGame(self):
		# Reset gameObjects
		self.gameObjects = []
		self.ren.clearObjects()

		# Pawns
		for i in range(8):
			pawnBlack = ChessPiece(PieceType.PAWN, 0, y=0, x=0, text=resources.getResource('pawn-black'))
			pawnWhite = ChessPiece(PieceType.PAWN, 1, y=10,x=0, text=resources.getResource('pawn-white'))
			self.gameObjects.append(pawnBlack)
			self.gameObjects.append(pawnWhite)
			self.board[1][i] = pawnBlack
			self.board[6][i] = pawnWhite
			self.ren.addObj(pawnBlack)
			self.ren.addObj(pawnWhite)

		# Rooks
		rookBlackA = ChessPiece(PieceType.ROOK, 0)
		rookBlackB = ChessPiece(PieceType.ROOK, 0)
		rookWhiteA = ChessPiece(PieceType.ROOK, 1)
		rookWhiteB = ChessPiece(PieceType.ROOK, 1)
		self.gameObjects.append(rookBlackA)
		self.gameObjects.append(rookBlackB)
		self.gameObjects.append(rookWhiteA)
		self.gameObjects.append(rookBlackB)
		self.board[0][0] = rookBlackA
		self.board[0][7] = rookBlackB
		self.board[7][0] = rookWhiteA
		self.board[7][7] = rookWhiteB

		# Knights
		knightBlackA = ChessPiece(PieceType.KNIGHT, 0)
		knightBlackB = ChessPiece(PieceType.KNIGHT, 0)
		knightWhiteA = ChessPiece(PieceType.KNIGHT, 1)
		knightWhiteB = ChessPiece(PieceType.KNIGHT, 1)
		self.gameObjects.append(knightBlackA)
		self.gameObjects.append(knightBlackB)
		self.gameObjects.append(knightWhiteA)
		self.gameObjects.append(knightWhiteB)
		self.board[0][1] = knightBlackA
		self.board[0][6] = knightBlackB
		self.board[7][1] = knightWhiteA
		self.board[7][6] = knightWhiteB

		# Bishops
		bishopBlackA = ChessPiece(PieceType.BISHOP, 0)
		bishopBlackB = ChessPiece(PieceType.BISHOP, 0)
		bishopWhiteA = ChessPiece(PieceType.BISHOP, 1)
		bishopWhiteB = ChessPiece(PieceType.BISHOP, 1)
		self.gameObjects.append(bishopBlackA)
		self.gameObjects.append(bishopBlackB)
		self.gameObjects.append(bishopWhiteA)
		self.gameObjects.append(bishopWhiteB)
		self.board[0][2] = bishopBlackA
		self.board[0][5] = bishopBlackB
		self.board[7][2] = bishopWhiteA
		self.board[7][5] = bishopWhiteB

		# Queen
		queenBlack = ChessPiece(PieceType.QUEEN, 0)
		queenWhite = ChessPiece(PieceType.QUEEN, 1)
		self.gameObjects.append(queenBlack)
		self.gameObjects.append(queenWhite)
		self.board[0][3] = queenBlack
		self.board[7][3] = queenWhite

		# King
		kingBlack = ChessPiece(PieceType.KING, 0)
		kingWhite = ChessPiece(PieceType.KING, 1)
		self.gameObjects.append(kingBlack)
		self.gameObjects.append(kingWhite)
		self.board[0][4] = kingBlack
		self.board[7][4] = kingWhite

	# Start the chess game
	def start(self):
		self.mainMenu()
		self.resetGame()

		# Game loop
		while True:
			k = self.stdscr.getch()
			if k != -1:
				break


# Represents a piece on the board
class ChessPiece(game.GameObject):
	def __init__(self, pieceType, player, y=0, x=0, text=''):
		super().__init__(y, x, text)
		self.type = pieceType
		self.player = player

class PieceType(Enum):
	PAWN = 1
	ROOK = 2
	KNIGHT = 3
	BISHOP = 4
	QUEEN = 5
	KING = 6
