import aiohttp
import json
import nextcord
from nextcord.ext import commands

class Advice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="advice", help="Get a useful piece of advice")
    async def advice(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.adviceslip.com/advice") as resp:
                if resp.status != 200:
                    await ctx.send("Couldn't fetch advice.")
                    return

                text = await resp.text()
                try:
                    data = json.loads(text)
                except Exception as e:
                    await ctx.send(f"Error: {e}")
                    return

        embed = nextcord.Embed(
            title="Advice for You",
            description=data["slip"]["advice"],
            color=nextcord.Color.green()
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1040/1040204.png")
        embed.set_footer(text="NexusBot • Advice is optional, wisdom is eternal")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Advice(bot))
