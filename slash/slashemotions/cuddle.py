import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Cuddle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="cuddle", description="Cuddle someone softly 🧸")
    async def cuddle(self, interaction: Interaction,
                    member: nextcord.Member = SlashOption(description="Mention the user you want to cuddle")):

        gifs = [
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXNjdnQzYXUzOXhibXljbjg3azBwaGsybWRnZWsxajc1M2FoNzMyNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C4gbG94zAjyYE/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWZteDFud2Y0OTE5OWV4OWNpbmJyZmhzM2JqMWI3ODEydGttbmdmayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7ZsnUYLno9IWI/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmtkNjg5bjFyNmJ6djFnYXJ0bTJzMDgwNDJrcmd4YW1iNjBnMTI3cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LIqFOpO9Qh0uA/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2I2OXY5bG1mdGJkNmdsZmRiZDd2dHJkMGNybWR5aXhxb2EzcDVoZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3bqtLDeiDtwhq/giphy.gif",
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExejB2aXRibTN0cDl2bWM1Z2x3Y3A4ODA5cTJldGRwM3UxbzM4MzlkZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/trJ68zLtt85QA/giphy.gif"
        ]

        embed = nextcord.Embed(
            title="So cozy~",
            description=f"{interaction.user.mention} cuddles with {member.mention} ☁️💗",
            color=nextcord.Color.magenta()
        )
        embed.set_image(url=random.choice(gifs))
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Cuddle ~")
        embed.timestamp = interaction.created_at

def setup(bot):
    bot.add_cog(Cuddle(bot))
