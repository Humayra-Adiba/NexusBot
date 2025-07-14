import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Airkiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="kiss", description="Give a airkiss someone with love!")
    async def airkiss(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="Who are you giving airkiss?", required=True)
    ):
        gifs = [
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3czdwbzZvdWowZmYxcmx3NW1hN3d2cmkydTI0bG44M2FscHZxa29rNCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/64U7W2xsNZXG0/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Y2xkdDd5aXdlc2Flc2o1dHFjbzVzZmVvbXczOTVpbWVqbWlpYjhtMyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/QGc8RgRvMonFm/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Y2xkdDd5aXdlc2Flc2o1dHFjbzVzZmVvbXczOTVpbWVqbWlpYjhtMyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/6fY9Kpw0fz6U0/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExenhocmc4dnYycmp1NmdjbGhpYjFuazV1empvazd6bHFiYXhmamNyMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jR22gdcPiOLaE/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OGtmMGZqejh6bjJ0c3Iwa25zNDA3cXRrM2Q0N3RyaDdtZWoxM3JvZyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/QGc8RgRvMonFm/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Y2xkdDd5aXdlc2Flc2o1dHFjbzVzZmVvbXczOTVpbWVqbWlpYjhtMyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/TGqhg8CXipgzK8UEdr/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bGZydTR2bWNrcm9tcTY0OGhsMms5cmVxYW1kemJ5N2dqeG5lZWl1dCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/7QkZap9kQ1iy4/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bGZydTR2bWNrcm9tcTY0OGhsMms5cmVxYW1kemJ5N2dqeG5lZWl1dCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/JFmIDQodMScJW/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bGZydTR2bWNrcm9tcTY0OGhsMms5cmVxYW1kemJ5N2dqeG5lZWl1dCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/j98SQB5Y7WqnC/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3YnQ1MGVmdzIxMmFneGM1NmNpZnYyZ2pucnd3MHM5b2w0bXdvYXY2ZSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/Ev1hGaBuRs448/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cDQxdGlyMTltOWd2b3oyODlzamlpczdvNGpncDBrNWtoaWxyNTFxeSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/uAvMPK3narqc8/giphy.gif"
        ]
        chosen = random.choice(gifs)
        embed = nextcord.Embed(
            title="Airkissing time!~",
            description=f"{interaction.user.mention} has lovingly given airkiss to {user.mention}! ❤️‍🔥",
            color=nextcord.Color.blurple()
        )
        embed.set_image(url=chosen)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Kiss ~")
        embed.timestamp = interaction.created_at
def setup(bot):
    bot.add_cog(Airkiss(bot))
