import aiohttp
import nextcord
from nextcord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ANIMAL_APIS = {
        "bird": {
            "url": "https://some-random-api.com/animal/bird",
            "emoji": "🕊️",
            "color": nextcord.Color.blue()
        },
        "cat": {
            "url": "https://some-random-api.com/animal/cat",
            "emoji": "🐱",
            "color": nextcord.Color.purple()
        },
        "dog": {
            "url": "https://some-random-api.com/animal/dog",
            "emoji": "🐶",
            "color": nextcord.Color.orange()
        },
        "donkey": {
            "url": "https://some-random-api.com/animal/donkey", 
            "emoji": "🫏",
            "color": nextcord.Color.dark_orange()
        },
        "panda": {
            "url": "https://some-random-api.com/animal/panda",
            "emoji": "🐼",
            "color": nextcord.Color.green()
        },
        "fox": {
            "url": "https://some-random-api.com/animal/fox",
            "emoji": "🦊",
            "color": nextcord.Color.red()
        },
        "koala": {
            "url": "https://some-random-api.com/animal/koala",
            "emoji": "🐨",
            "color": nextcord.Color.teal()
        },
        "kangaroo": {
            "url": "https://some-random-api.com/animal/kangaroo",
            "emoji": "🦘",
            "color": nextcord.Color.gold()
        },
        "raccoon": {
            "url": "https://some-random-api.com/animal/raccoon",
            "emoji": "🦝",
            "color": nextcord.Color.dark_grey()
        },
        "whale": {
            "url": "https://some-random-api.com/animal/whale",
            "emoji": "🐋",
            "color": nextcord.Color.dark_blue()
        },
        "duck": {
            "url": "https://some-random-api.com/animal/duck",
            "emoji": "🦆",
            "color": nextcord.Color.light_grey()
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
                    embed = nextcord.Embed(
                        title=f"{api['emoji']} Random {kind.title()} fact",
                        description=data.get("fact", "Here's something cute for you!"),
                        color=api["color"]
                    )
                    embed.set_image(url=data.get("image"))
                    embed.set_footer(text="Powered by some-random-api.com • NexusBot ✨")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("⚠️ Couldn't fetch animal data right now. Please try again later.")

    @commands.command()
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://v2.jokeapi.dev/joke/Any?type=single") as response:
                if response.status == 200:
                    data = await response.json()
                    joke = data.get("joke", "I couldn't find a joke 😢")
                    embed = nextcord.Embed(
                        title="Here's a joke for you! 😄",
                        description=joke,
                        color=nextcord.Color.random()
                    )
                    embed.set_footer(text="So how was it? Hope you laughed! 😂 • NexusBot ✨")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Couldn't fetch a joke right now.")

def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun cog loaded.")
