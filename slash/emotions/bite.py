import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Bite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="bite", description="Bite a user!")
    async def bite(self, interaction: Interaction,
            member: nextcord.Member = SlashOption(description="User to bite", required=True)
    ):
        gifs = [
            # Add bite GIF URLs here
        ]

        gif_url = random.choice(gifs) if gifs else ""
        embed = nextcord.Embed(
            title="Ouch! A bite!",
            description=f"{interaction.user.mention} bites {member.mention}! 🦷",
            color=nextcord.Color.red()
        )
        if gif_url:
            embed.set_image(url=gif_url)
        embed.set_footer(text="That must have hurt!")
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Bite(bot))
