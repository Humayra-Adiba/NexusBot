import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Feed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="feed", description="Feed someone with love!")
    async def feed(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="Who are you feeding?", required=True)
    ):
        gifs = [
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHVtZ2o5czBqN3RiZzBlcTl1ZzdkOWxzdWNkeGN5cHIybDNkdDJmbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RltQlCSRa2UMg/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3c3p5ZGw2MXdwM2gxZXpvMTRwbXA3Y3dpY29jdXQxNHRweHllY2lpdSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/uu3vrODux7HTG/giphy.gif",
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHVtZ2o5czBqN3RiZzBlcTl1ZzdkOWxzdWNkeGN5cHIybDNkdDJmbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RltQlCSRa2UMg/giphy.gif",
        ]
        chosen = random.choice(gifs)
        embed = nextcord.Embed(
            title="🍴 Feeding Time!",
            description=f"{interaction.user.mention} lovingly fed {user.mention}!",
            color=nextcord.Color.orange()
        )
        embed.set_image(url=chosen)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Feed(bot))
