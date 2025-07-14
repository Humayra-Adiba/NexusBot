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
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnI0MG13OWpteTd6aWxtdnZuaWQ2ZGV0cHJ2c28xZGRiYTI4b2Y0MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cb4Pg4jau2SEE/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnI0MG13OWpteTd6aWxtdnZuaWQ2ZGV0cHJ2c28xZGRiYTI4b2Y0MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/7To4ohzbWeBQF4I0xx/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2ZiamJtM3NsZDdsMnNrcHdsZHlvOGE0azV4N3AxNjRsNHcyN2d2NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/u2LJ0n4lx6jF6/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnI0MG13OWpteTd6aWxtdnZuaWQ2ZGV0cHJ2c28xZGRiYTI4b2Y0MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/dw49VcrmnPuL62hWn8/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHRtanhpYnd3YWhkaXV2dm1qc2FyMWNhdmE0Y2hnZ2NmeGl5OHY3aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KmG26GNmdWOUE/giphy.gif",
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExazh5NTczZXEzam9mbHJtcGRzaG12M3NwN3ZzOWZpdjRmenFia2d4MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/H10tCrEZDhbBm/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cXkwM2FhN3E2ZmZpM2hkMHQ4aHIxbzFraGVuYXU5MnpoOWR0NnhleiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/frDFCFK9S4oHm/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cXkwM2FhN3E2ZmZpM2hkMHQ4aHIxbzFraGVuYXU5MnpoOWR0NnhleiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/maINkm7zjcL4s/giphy.gif"
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
