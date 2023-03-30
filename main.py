import random

PIECES = ["line","L","reverseL","squiggly","square"]
PIECES_MAP = {
	"line" : [["#","#","#","#"]],
	"L" : [["#"," "],["#"," "],["#","#"]],
	"reverseL" : [[" ","#"],[" ","#"],["#","#"]],
	"squiggly" : [[" ","#"],["#","#"],["#"," "]],
	"square" : [["#","#"],["#","#"]],
}

class Piece:

	# Pieces used in the game
	def __init__(self,name):
		self.x = 0			# x-axis
		self.y = 0			# y-axis
		self.shape = PIECES_MAP[name]

	# Rotate the piece clockwise	
	def rotate_clockwise(self):
		self.shape = list(map(list,(zip(*reversed(self.shape)))))

	# Rotate the piece anti-clockwise
	def rotate_anticlockwise(self):
		self.shape = list(reversed(list(map(list,zip(*self.shape)))))

	# Move the piece to left
	def move_left(self):
		self.x -= 1

	# Move the piece to right
	def move_left(self):
		self.x += 1

	# Move the piece down
	def move_down(self):
		self.y -= 1


class Block:

	# A single block in the board
	def __init__(self):
		self.value = " "

	# Return True for empty block
	def check_empty(self):
		return self.value == " "

class Board:

	# The tetris board where game is played upon
	def __init__(self):
		self.width = 12
		self.length = 12
		self.board = [[Block() for _ in range(self.width)] for _ in range(self.length)]

	# Returns True if there is collision with other blocks
	# Returns True if piece is out of board
	def is_collision(self,piece,x,y):
		for row in range(len(piece.shape)):
            for col in range(len(piece.shape[0])):
                if piece.shape[row][col] != " " and (x + col >= self.width or x + col < 0 or y - row >= self.length or y - row < 0 or not self.board[y+row][x+col].is_empty()):
                    return True
        return False


