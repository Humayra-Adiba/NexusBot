import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Confused(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="confused", description="Show that you are confused!")
    async def confused(self, interaction: Interaction,
                member: nextcord.Member = SlashOption(description="User to look confused at", required=True)
    ):
        gifs = [
            "https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUyZjF5ZW81YjZ4OHdlbnc1YzF6amNtbTd1NXNoMXhhZ3huY3p0YTg3cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tUT6nrncs5eLe/giphy.gif"
        ]

        gif_url = random.choice(gifs) if gifs else ""
        embed = nextcord.Embed(
            title="So confused!",
            description=f"{interaction.user.mention} looks confused at {member.mention}! 🤔",
            color=nextcord.Color.blue()
        )
        if gif_url:
            embed.set_image(url=gif_url)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Confusion is a part of life!")
        embed.timestamp = interaction.created_at

def setup(bot):
    bot.add_cog(Confused(bot))
