import nextcord
import random
from nextcord import Interaction, ButtonStyle
from nextcord.ext import commands
from nextcord.ui import Button, View

class feature-ticTacToe(commands.Cog):
	def __init__(self, client):
		self.client = client
	winningConditions = [
 [0, 1, 2],
 [3, 4, 5],
 [6, 7, 8],
 [0, 3, 6],
 [1, 4, 7],
 [2, 5, 8],
 [0, 4, 8],
 [2, 4, 6]
]

	player1 = ""
	player2 = ""
	turn = ""
	gameOver = True

	board = []
	@nextcord.slash_command(name='tictactoe start',
				description='Starts the tic tac toe game.')
	async def tictactoe(self, interaction: Interaction, p1 : nextcord.Member, p2 : nextcord.Member):
		global player1
		global player2
		global turn
		global gameOver
		global count

		if gameOver:
			global board
			board = [":white_large_square:" for i in range(9)]
			turn = ""
			gameOver = False
			count = 0
			
			player1 = p1
			player2 = p2

			line = ""
			for x in range(len(board)):
				line += " " + board[x]
				if x % 3 == 2:
					await interaction.response.send_message(line)
					line = ""

			num = random.randint(1, 2)
			if num == 1:
				turn = player1
			else:
				turn = player2
			await interaction.response.send_message("It is currently <@" + str(turn.id) + ">'s turn.")
		else:
			await interaction.response.send_message("A game is currently in progress!")

	@nextcord.slash_command(name="tictactoe place",
				description="Places your marker.")
	async def place(self, interaction: Interaction, position : int):
		global turn
		global player1
		global player2
		global board
		global count

		if not gameOver:
			mark = ""
			if turn == interaction.user:
				if turn == player1:
					mark = ":regional_indicator_x:"
				elif turn == player2:
					mark = ":o2:"
				if 0 < pos and pos < 10 and board[pos-1] == ":white_large_square:":
					board[pos-1] = mark
					count += 1
					# Prints the board.
					line = ""
					for x in range(len(board)):
						line += " " + board[x]
						if x % 3 == 2:
							await interaction.response.send_message(line)
							line = ""
					checkWinner(winningConditions, mark)
					if gameOver:
						await interaction.response.send_message(mark + " wins! GG!")
					elif count >= 9:
						await interaction.response.send_message("It is a tie! GG!")
					# Switch turns
					if turn == player1:
						turn = player2
					elif turn == player2:
						turn = player1
				else:
					await interaction.response.send_message("Invalid input (position) in command!")
			else:
				await interaction.response.send_message("It is currently not your turn.")
		else:
			await interaction.response.send_message("Please start a new game using `/tictactoe start`.")

	def checkWinner(self, winningConditions, mark):
		global gameOver
		for condition in winningConditions:
			if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
				gameOver = True
