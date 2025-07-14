import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Slap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="slap", description="Give someone a slap!")
    async def slap(self, interaction: Interaction,
                member: nextcord.Member = SlashOption(description="User to slap", required=True)
    ):
        gifs = [
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWZ6bHB3OWhzdzFqMW53YzdtbWk1M3RrMWttaW9vN29qemY0YTViZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RXGNsyRb1hDJm/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dWFyd3FidXVyazUwaDZub2xvM211M2E2NXVqenZhZHVheWdjZno1YSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/6Fad0loHc6Cbe/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZDAyYTFsdGc0bHR2ZzZwOTh1dG8wdTM0dnIxbnNrMGt0OWJpYWR5aSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/Gf3AUz3eBNbTW/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZDAyYTFsdGc0bHR2ZzZwOTh1dG8wdTM0dnIxbnNrMGt0OWJpYWR5aSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/Gf3AUz3eBNbTW/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZDAyYTFsdGc0bHR2ZzZwOTh1dG8wdTM0dnIxbnNrMGt0OWJpYWR5aSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/xUNd9HZq1itMkiK652/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZDAyYTFsdGc0bHR2ZzZwOTh1dG8wdTM0dnIxbnNrMGt0OWJpYWR5aSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/xUO4t2gkWBxDi/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZDAyYTFsdGc0bHR2ZzZwOTh1dG8wdTM0dnIxbnNrMGt0OWJpYWR5aSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/OQ7phVSLg3xio/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3amcwYnMyN2N1NWU4eHdzbmFxNWtwNXZpOTFnM3N3d204a3B3bzlmMCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/ubQw6SnG0NvCNewS7i/giphy.gif"
        ]

        gif_url = random.choice(gifs)
        embed = nextcord.Embed(
            title="A cool slap!",
            description=f"{interaction.user.mention} gives {member.mention} a cool slap!😎",
            color=nextcord.Color.green()
        )
        embed.set_image(url=gif_url)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Slap ~")
        embed.timestamp = interaction.created_at

def setup(bot):
    bot.add_cog(Slap(bot))
