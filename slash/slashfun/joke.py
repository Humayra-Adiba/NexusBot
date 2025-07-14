import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="joke", description="Get a random joke")
    async def joke(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://v2.jokeapi.dev/joke/Any?type=single") as resp:
                if resp.status != 200:
                    return await interaction.response.send_message("😢 Couldn't fetch a joke right now.")
                data = await resp.json()

        embed = nextcord.Embed(
            title="😂 Here's a joke!",
            description=data.get("joke", "No joke found."),
            color=nextcord.Color.random()
        )
        embed.set_footer(text="NexusBot • Laughter is the best medicine 💊")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Joke(bot))
