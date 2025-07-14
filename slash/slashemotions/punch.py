import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Punch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="punch", description="Punch someone playfully (or not)!")
    async def punch(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="Who are you punching?", required=True)
    ):
        gifs = [
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGN3ZnZpcHVwZXR6OXdyczBwaGF6b2lnZDFpbGdqMDR5ZTN2Mm13MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/NY3tXwOBUwQYq7lbXx/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGN3ZnZpcHVwZXR6OXdyczBwaGF6b2lnZDFpbGdqMDR5ZTN2Mm13MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/YrfARBZkReL8Q/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW9ydWFoaTQ0c2pqaHozd3NsbW15d3hmcnAzMm5sMnp3M3hhbnQxZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NuiEoMDbstN0J2KAiH/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGN3ZnZpcHVwZXR6OXdyczBwaGF6b2lnZDFpbGdqMDR5ZTN2Mm13MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/OpvUphysvKumQ/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGN3ZnZpcHVwZXR6OXdyczBwaGF6b2lnZDFpbGdqMDR5ZTN2Mm13MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/llP0ZMp0fqcA3OIB0f/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnVianZvN29ucTVwOHZzMHRqNmRsZnV1enoxa3J4cmlwczNub2h6aSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qIfG2193qAwGgw4hdg/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnVianZvN29ucTVwOHZzMHRqNmRsZnV1enoxa3J4cmlwczNub2h6aSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/vNfLJFVHlsggg/giphy.gif"
        ]
        chosen = random.choice(gifs)
        embed = nextcord.Embed(
            title="🥊 Boom!",
            description=f"{interaction.user.mention} punched {user.mention}! 👊",
            color=nextcord.Color.red()
        )
        embed.set_image(url=chosen)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Punch ~")
        embed.timestamp = interaction.created_at

def setup(bot):
    bot.add_cog(Punch(bot))
