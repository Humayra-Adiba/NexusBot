import aiohttp
import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ANIMAL_APIS = {
        "bird": {
            "url": "https://some-random-api.com/animal/bird",
            "emoji": "🕊️",
            "color": discord.Color.blue()
        },
        "cat": {
            "url": "https://some-random-api.com/animal/cat",
            "emoji": "🐱",
            "color": discord.Color.purple()
        },
        "dog": {
            "url": "https://some-random-api.com/animal/dog",
            "emoji": "🐶",
            "color": discord.Color.orange()
        }
    }

    @commands.command()
    async def animal(self, ctx, kind: str):
        kind = kind.lower()
        if kind not in self.ANIMAL_APIS:
            available = ", ".join(f"`{k}`" for k in self.ANIMAL_APIS)
            await ctx.send(f"❌ Unknown animal type. Try one of: {available}")
            return

        api = self.ANIMAL_APIS[kind]

        async with aiohttp.ClientSession() as session:
            async with session.get(api["url"]) as response:
                if response.status == 200:
                    data = await response.json()
                    embed = discord.Embed(
                        title=f"{api['emoji']} Random {kind.title()} fact",
                        description=data.get("fact", "Here's something cute for you!"),
                        color=api["color"]
                    )
                    embed.set_image(url=data.get("image"))
                    embed.set_footer(text="Powered by some-random-api.com • NexusBot ✨")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("⚠️ Couldn't fetch animal data right now. Please try again later.")


async def setup(bot):
    await bot.add_cog(Fun(bot))
    print("Fun cog loaded.")