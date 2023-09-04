import nextcord
from nextcord import Interaction, ButtonStyle
from nextcord.ext import commands
from nextcord.ui import Button, View

class feature-ticTacToe(commands.Cog):
	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='tictactoe',
				description='Starts the tic tac toe game)
	async def tictactoe(self, interaction: Interaction):
		cell1 = Button(label='1', style=ButtonStyle.blurple)
