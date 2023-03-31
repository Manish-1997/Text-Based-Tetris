import unittest
from main import Piece,Block,Board,Play,PIECES,PIECES_MAP

# Test class for Piece object
class TestPiece(unittest.TestCase):

	def test_move_left(self):

		# Create a piece at (1,0)
		piece = Piece(PIECES[-1],1,0)
		piece.move_left()
		self.assertEqual(piece.current_pos(), (0,0))

	def test_move_right(self):

		# Create a piece at (1,0)
		piece = Piece(PIECES[-1],1,0)
		piece.move_right()
		self.assertEqual(piece.current_pos(), (2,0))

	def test_move_down(self):

		# Create a piece at (1,0)
		piece = Piece(PIECES[-1],1,0)
		piece.move_down()
		self.assertEqual(piece.current_pos(), (1,1))

	def test_clockwise_rotate_L_piece(self):

		# Create an L piece at (1,0)
		piece = Piece('L',1,0)
		# Dict of all possible angles of 'L' piece
		rotatedL = {
			90 : [['#', '#', '#'], ['#', ' ', ' ']], 
			180 : [['#', '#'], [' ', '#'], [' ', '#']], 
			270 : [[' ', ' ', '#'], ['#', '#', '#']], 
			360 : [["#"," "],["#"," "],["#","#"]]
		}

		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedL[90])
		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedL[180])
		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedL[270])
		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedL[360])

	def test_clockwise_rotate_line_piece(self):

		# Create a line piece at (1,0)
		piece = Piece("line",1,0)
		rotatedLine = {
			90 : [['#'], ['#'], ['#'], ['#']],
			180 : [["#","#","#","#"]]
		}

		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedLine[90])
		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedLine[180])

	def test_clockwise_rotate_reverseL_piece(self):

		# Create an reverseL piece at (1,0)
		piece = Piece('reverseL',1,0)
		# Dict of all possible angles of reverse 'L' piece
		rotatedReverseL = {
			90 : [['#', ' ', ' '], ['#', '#', '#']], 
			180 : [['#', '#'], ['#', ' '], ['#', ' ']], 
			270 : [['#', '#', '#'], [' ', ' ', '#']], 
			360 : [[" ","#"],[" ","#"],["#","#"]]
		}

		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedReverseL[90])
		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedReverseL[180])
		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedReverseL[270])
		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedReverseL[360])

	def test_clockwise_rotate_squiggly_piece(self):

		# Create a squiggly piece at (1,0)
		piece = Piece("squiggly",1,0)
		rotatedSquiggly = {
			90 : [['#', '#', ' '], [' ', '#', '#']],
			180 : [[" ","#"],["#","#"],["#"," "]]
		}

		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedSquiggly[90])
		piece.rotate_clockwise()
		self.assertEqual(piece.shape,rotatedSquiggly[180])

	def test_clockwise_rotate_square_piece(self):

		piece = Piece("square",1,0)
		rotatedSquare = piece.shape
		piece.rotate_clockwise()
		# Square doesn't change shape when rotated
		self.assertEqual(piece.shape,rotatedSquare)

	def test_anticlockwise_rotate_L_piece(self):

		# Create an L piece at (1,0)
		piece = Piece('L',1,0)
		# Dict of all possible angles of 'L' piece
		rotatedL = {
			90 : [['#', '#', '#'], ['#', ' ', ' ']], 
			180 : [['#', '#'], [' ', '#'], [' ', '#']], 
			270 : [[' ', ' ', '#'], ['#', '#', '#']], 
			360 : [["#"," "],["#"," "],["#","#"]]
		}

		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedL[270])
		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedL[180])
		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedL[90])
		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedL[360])

	def test_anticlockwise_rotate_line_piece(self):

		# Create a line piece at (1,0)
		piece = Piece("line",1,0)
		rotatedLine = {
			90 : [['#'], ['#'], ['#'], ['#']],
			180 : [["#","#","#","#"]]
		}

		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedLine[90])
		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedLine[180])

	def test_anticlockwise_rotate_reverseL_piece(self):

		# Create an reverseL piece at (1,0)
		piece = Piece('reverseL',1,0)
		# Dict of all possible angles of reverse 'L' piece
		rotatedReverseL = {
			90 : [['#', ' ', ' '], ['#', '#', '#']], 
			180 : [['#', '#'], ['#', ' '], ['#', ' ']], 
			270 : [['#', '#', '#'], [' ', ' ', '#']], 
			360 : [[" ","#"],[" ","#"],["#","#"]]
		}

		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedReverseL[270])
		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedReverseL[180])
		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedReverseL[90])
		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedReverseL[360])

	def test_anticlockwise_rotate_squiggly_piece(self):

		# Create a squiggly piece at (1,0)
		piece = Piece("squiggly",1,0)
		rotatedSquiggly = {
			90 : [['#', '#', ' '], [' ', '#', '#']],
			180 : [[" ","#"],["#","#"],["#"," "]]
		}

		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedSquiggly[90])
		piece.rotate_anticlockwise()
		self.assertEqual(piece.shape,rotatedSquiggly[180])

	def test_anticlockwise_rotate_square_piece(self):

		piece = Piece("square",1,0)
		rotatedSquare = piece.shape
		piece.rotate_anticlockwise()
		# Square doesn't change shape when rotated
		self.assertEqual(piece.shape,rotatedSquare)



# Test class for Board object
class TestBoard(unittest.TestCase):

	def test_collision_left_screen(self):

		# Create board and square piece at (0,0)
		board = Board()
		piece = Piece("square",0,0)
		self.assertTrue(board.collision(piece,-1,0))

	def test_collision_right_screen(self):

		# Create board and square piece at (0,0)
		board = Board()
		piece = Piece("square",0,0)
		self.assertTrue(board.collision(piece,board.width+1,0))

	def test_collision_board(self):

		# Create board and square piece at (0,0)
		board = Board()
		piece = Piece("square",0,0)

		# Creating a custom filled board
		for row in range(board.length-1,5,-1):
			for col in range(board.width):
				board.board[row][col].value = "#"

		self.assertTrue(board.collision(piece,0,5))

	def test_add_piece(self):

		# Create board and square piece at (0,0)
		board = Board()
		piece = Piece("square",0,0)

		board.add_piece(piece,0,board.length - 2)
		self.assertEqual(board.board[board.length - 2][0].value,"#")


# Test class for Play object
class TestPlay(unittest.TestCase):

	def test_load_piece(self):
		play = Play()
		play.load_piece()
		self.assertNotEqual(play.piece,None)



if __name__=='__main__':
	unittest.main()