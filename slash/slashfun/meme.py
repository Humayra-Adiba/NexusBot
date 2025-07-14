import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="meme", description="Get a random meme")
    async def meme(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://meme-api.com/gimme") as resp:
                if resp.status != 200:
                    return await interaction.response.send_message("🥲 Couldn't fetch a meme.")
                data = await resp.json()

        embed = nextcord.Embed(
            title=data["title"],
            url=data["postLink"],
            color=nextcord.Color.random()
        )
        embed.set_image(url=data["url"])
        embed.set_footer(text=f"From r/{data['subreddit']} • NexusBot ✨")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Meme(bot))
