import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Fact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="fact", description="Get a random interesting fact")
    async def fact(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as resp:
                if resp.status != 200:
                    return await interaction.response.send_message("🤓 Couldn't find a fun fact.")
                data = await resp.json()

        embed = nextcord.Embed(
            title="📚 Did You Know?",
            description=data["text"],
            color=nextcord.Color.orange()
        )
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Fact(bot))
