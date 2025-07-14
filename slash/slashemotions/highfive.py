import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class HighFive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="highfive", description="Give someone a high five!")
    async def highfive(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="Who are you high-fiving?", required=True)
    ):
        gifs = [
            "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
            "https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif",
            "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
            "https://media.giphy.com/media/3oEjHP8ELRNNlnlLGM/giphy.gif",
            "https://media.giphy.com/media/xT9IgIc0lryrxvqVGM/giphy.gif"
        ]
        chosen = random.choice(gifs)
        embed = nextcord.Embed(
            title="✋ High Five!",
            description=f"{interaction.user.mention} high-fived {user.mention}!",
            color=nextcord.Color.gold()
        )
        embed.set_image(url=chosen)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="High five! ✋")
        embed.timestamp = interaction.created_at

def setup(bot):
    bot.add_cog(HighFive(bot))
