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
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTBzeW9od29kMTk4emRrZ3B0Z2VkbGtsM2JyYTRxdjJtY2ZnYjZ3ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4JpvyNYuyf0aI/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmszZXIxYWowMjNxbmRtMDZwOGVidXRxa2M0ZmduZGR5b3VwMWp2bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lrMUMn9lnpaJDsvP0u/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHBubWpoNXJ1MjhqeXJoZHFrenpxcTRlamJ2YjZxeW1yM2prOTNsOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/b6mpA0JrIUsFSdhG9q/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OHVxM2QzNDlyMWsybjcwZDRocjlrNWV1enVsMHRtcmV6cDJ3azFhayZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/OqQOwXiCyJAmA/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OWJmcjQ4dWM3ZndybmpmcWJzbXFjMGpmaXlncjA2bWo5dndzcmVvOCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/iN4THuyyGQboRXYEkc/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OWJmcjQ4dWM3ZndybmpmcWJzbXFjMGpmaXlncjA2bWo5dndzcmVvOCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/w2OMjUGV7mCSQ/giphy.gif"
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
