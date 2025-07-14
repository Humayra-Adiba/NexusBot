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
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Zjgxb2Nhb3luNHBwaDB5anh1eWthNm94ZzZkMjB6dmF5d253eTBxcSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/3ohjV5DluQXRbRbbPy/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXV6MXozeDd5d2h1azNrdGttOWdtaDJ3Z3pydW8wcG1kMmI1a2JjdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2eK5QjgedZ92fckV9K/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWY5aDlrN2dodTQxcjN3cDZqeXN4NWE3c2Y0cXVxeW9samJrYXBwMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l0HlK1OcsNRl3NYu4/giphy.gif"
        ]
        chosen = random.choice(gifs)
        embed = nextcord.Embed(
            title="🍴 Feeding Time!",
            description=f"{interaction.user.mention} lovingly fed {user.mention}!",
            color=nextcord.Color.orange()
        )
        embed.set_image(url=chosen)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Feeding is caring!")
        embed.timestamp = interaction.created_at

def setup(bot):
    bot.add_cog(Feed(bot))
