import nextcord
from nextcord.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Example command
    @nextcord.slash_command(name="dice", description="Roll a dice")
    async def dice(self, interaction: nextcord.Interaction):
        import random
        result = random.randint(1, 6)
        await interaction.response.send_message(f"🎲 You rolled a {result}!")

# THIS IS THE REQUIRED SETUP FUNCTION
def setup(bot):
    bot.add_cog(Game(bot))
