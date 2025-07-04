import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="kick", description="Kick a user (for fun, not real kick)!")
    async def kick(self, interaction: Interaction,
            member: nextcord.Member = SlashOption(description="User to kick", required=True)
    ):
        gifs = [
            # Add kick GIF URLs here
        ]

        gif_url = random.choice(gifs) if gifs else ""
        embed = nextcord.Embed(
            title="Kick!",
            description=f"{interaction.user.mention} has given a dangerous kick to {member.mention}! 🦵",
            color=nextcord.Color.red()
        )
        if gif_url:
            embed.set_image(url=gif_url)
        embed.set_footer(text="Dangerous kick!")
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Kick(bot))
