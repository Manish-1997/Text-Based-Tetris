import random
import copy
import time
from IPython.display import clear_output

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
	def __init__(self,name,x,y):
		self.x = x			# x-axis
		self.y = y			# y-axis
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
	def move_right(self):
		self.x += 1

	# Move the piece down
	def move_down(self):
		self.y += 1

	# Return current position of the piece
	def current_pos(self):
		return(self.x,self.y)

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
    def collision(self, piece, x, y):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[0])):
                if piece.shape[row][col] != " " and (x + col >= self.width or x + col < 0 or y + row >= self.length or y + row < 0 or not self.board[y+row][x+col].check_empty()):
                    return True
        return False

    # Add the piece to board after reaching bottom
    def add_piece(self, piece, x, y):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[0])):
                if piece.shape[row][col] != " ":
                    self.board[y+row][x+col].value = piece.shape[row][col]

    # Clear single completed row and bring down above rows
    def clear_completed_row(self, row):
        for y in range(row, 0, -1):
            for x in range(self.width):
                self.board[y][x].value = self.board[y-1][x].value

    # Check if a row is completed
    def check_completed_row(self, row):
        for x in range(self.width):
            if self.board[row][x].value == " ":
                return False
        return True


class Play:

	# Start the game
	def __init__(self):
		self.board = Board()
		self.piece = None

	# Load the piece to be played with in the game
	def load_piece(self):
		pieceName = PIECES[random.randint(0,len(PIECES)-1)]
		maxX = self.board.width - len(PIECES_MAP['line'][0])
		xaxis = random.randint(0,maxX - 1)
		self.piece = Piece(pieceName,xaxis,0)

	# Take user input
	def user_input(self):
		print("Please chose one of the following option!")
		print("<a> : move piece left and move one row down")
		print("<d> : move piece right and move one row down")
		print("<w> : rotate piece counter clockwise and move one row down")
		print("<s> : rotate piece clockwise and move one row down")
		print("<space> : no action and the piece moves one row down")
		while True:
			userInput = input()
			if userInput in ['a','d','w','s',' ']:
				return userInput
			else:
				print("Your input '{}' is not in our options.".format(userInput))
				print("Please select valid option again!")

	# Make the user move
	def load_input(self,userInput):
		if userInput == 'a': 
			if not self.board.collision(self.piece,self.piece.x - 1,self.piece.y) and not self.board.collision(self.piece,self.piece.x - 1,self.piece.y + 1):
				self.piece.move_left()
				self.piece.move_down()
			else:
				print("Invalid move. Collision detected!")
		elif userInput == 'd': 
			if not self.board.collision(self.piece,self.piece.x + 1,self.piece.y) and not self.board.collision(self.piece,self.piece.x + 1,self.piece.y + 1):
				self.piece.move_right()
				self.piece.move_down()
			else:
				print("Invalid move. Collision detected!")
		elif userInput == 'w':
			self.piece.rotate_anticlockwise() 
			if not self.board.collision(self.piece,self.piece.x,self.piece.y) and not self.board.collision(self.piece,self.piece.x,self.piece.y + 1):
				self.piece.move_down()
			else:
				self.piece.rotate_clockwise()
				print("Invalid move. Collision detected!")
		elif userInput == 's':
			self.piece.rotate_clockwise() 
			if not self.board.collision(self.piece,self.piece.x,self.piece.y) and not self.board.collision(self.piece,self.piece.x,self.piece.y + 1):
				self.piece.move_down()
			else:
				self.piece.rotate_anticlockwise()
				print("Invalid move. Collision detected!")
		elif userInput == " ":
			if not self.board.collision(self.piece,self.piece.x,self.piece.y + 1):
				self.piece.move_down()

	# Check if piece has any possible move
	def check_moves_left(self):
		if self.board.collision(self.piece,self.piece.x,self.piece.y + 1):
			return False
		return True

	# Clear all the completed rows
	def clear_completed_board(self):
		for y in range(1,self.board.length):
			if self.board.check_completed_row(y):
				self.board.clear_completed_row(y)

	# Print the board
	def print_board(self):
		dummyBoard = copy.deepcopy(self.board.board)
		# Copy the tetrics piece onto dummy board for printing
		print('-'*((self.board.width*2)-1))
		for row in range(len(self.piece.shape)):
			for col in range(len(self.piece.shape[0])):
				if self.piece.shape[row][col] != " ":
					dummyBoard[self.piece.y + row][self.piece.x + col].value = self.piece.shape[row][col]
		# Print the dummy board
		for y in range(self.board.length):
			print(" ".join(list(map(lambda x : x.value,dummyBoard[y]))))

	# Start the game
	def game(self):
		playing = True
		while playing:
			game = True
			# Load the tetric piece
			self.load_piece()
			# Check if Game has ended
			if self.board.collision(self.piece,self.piece.x,self.piece.y):
				playing = False
				clear_output()
				print("GAME OVER!!!")
				self.print_board()
				continue
			# Clear the board
			self.clear_completed_board()
			while game:
				# Print the board
				clear_output()
				self.print_board()			
				# Check if tetric piece is settled in its position
				if not self.check_moves_left():
					game = False
					self.board.add_piece(self.piece,self.piece.x,self.piece.y)
					continue
				# Take the user input and perform action
				user_choice = self.user_input()
				self.load_input(user_choice)

if __name__ == "__main__":
	play = Play()
	play.game()
