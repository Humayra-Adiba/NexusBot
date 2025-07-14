
import aiohttp
import nextcord
from nextcord.ext import commands
import json

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ANIMAL_APIS = {
        "bird": {"url": "https://some-random-api.com/animal/bird", "emoji": "🕊️", "color": nextcord.Color.blue()},
        "cat": {"url": "https://some-random-api.com/animal/cat", "emoji": "🐱", "color": nextcord.Color.purple()},
        "dog": {"url": "https://some-random-api.com/animal/dog", "emoji": "🐶", "color": nextcord.Color.orange()},
        "donkey": {"url": "https://some-random-api.com/animal/donkey", "emoji": "🫏", "color": nextcord.Color.dark_orange()},
        "panda": {"url": "https://some-random-api.com/animal/panda", "emoji": "🐼", "color": nextcord.Color.green()},
        "fox": {"url": "https://some-random-api.com/animal/fox", "emoji": "🦊", "color": nextcord.Color.red()},
        "koala": {"url": "https://some-random-api.com/animal/koala", "emoji": "🐨", "color": nextcord.Color.teal()},
        "kangaroo": {"url": "https://some-random-api.com/animal/kangaroo", "emoji": "🦘", "color": nextcord.Color.gold()},
        "raccoon": {"url": "https://some-random-api.com/animal/raccoon", "emoji": "🦝", "color": nextcord.Color.dark_grey()},
        "whale": {"url": "https://some-random-api.com/animal/whale", "emoji": "🐋", "color": nextcord.Color.dark_blue()},
        "duck": {"url": "https://some-random-api.com/animal/duck", "emoji": "🦆", "color": nextcord.Color.light_grey()}
    }

    @commands.command(help="Get a random fact and image about an animal. {!animal <kind>}")
    async def animal(self, ctx, kind: str):
        kind = kind.lower()
        if kind not in self.ANIMAL_APIS:
            suggestions = ", ".join(f"`{k}`" for k in self.ANIMAL_APIS)
            return await ctx.send(f"❌ Unknown animal type. Try one of: {suggestions}")

        api = self.ANIMAL_APIS[kind]
        async with aiohttp.ClientSession() as session:
            async with session.get(api["url"]) as resp:
                if resp.status != 200:
                    return await ctx.send("⚠️ API error. Please try again later.")
                data = await resp.json()

        embed = nextcord.Embed(
            title=f"{api['emoji']} {kind.title()} Fact!",
            description=data.get("fact", "No fact found."),
            color=api["color"]
        )
        embed.set_image(url=data.get("image"))
        embed.set_footer(text="Powered by some-random-api.com • NexusBot ✨")
        await ctx.send(embed=embed)

    @commands.command(help="Tells a random joke.")
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://v2.jokeapi.dev/joke/Any?type=single") as resp:
                if resp.status != 200:
                    return await ctx.send("😢 Couldn't fetch a joke right now.")
                data = await resp.json()
        embed = nextcord.Embed(
            title="😂 Here's a joke!",
            description=data.get("joke", "No joke found."),
            color=nextcord.Color.random()
        )
        embed.set_footer(text="NexusBot • Laughter is the best medicine 💊")
        await ctx.send(embed=embed)

    @commands.command(help="Sends a random meme.")
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://meme-api.com/gimme") as resp:
                if resp.status != 200:
                    return await ctx.send("🥲 Couldn't fetch a meme.")
                data = await resp.json()
        embed = nextcord.Embed(title=data["title"], color=nextcord.Color.random(), url=data["postLink"])
        embed.set_image(url=data["url"])
        embed.set_footer(text=f"From r/{data['subreddit']} • NexusBot ✨")
        await ctx.send(embed=embed)


    @commands.command(help="Get a piece of advice.")
    async def advice(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.adviceslip.com/advice") as resp:
                if resp.status != 200:
                    return await ctx.send("🧠 Couldn't fetch advice.")

                try:
                    text = await resp.text()
                    data = json.loads(text)
                except Exception as e:
                    return await ctx.send(f"❌ Failed to parse advice. ({e})")

        embed = nextcord.Embed(
            title="📌 Advice for You....",
            description=data["slip"]["advice"],
            color=nextcord.Color.green()
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1040/1040204.png")
        embed.set_footer(text="NexusBot • Remember, advice is just a suggestion! 💡")
        await ctx.send(embed=embed)



    @commands.command(help="Get a random quote.")
    async def quote(self, ctx):
        api_url = "https://api.api-ninjas.com/v1/quotes"
        headers = {"X-Api-Key": "n3hiONPoFysP2shoeg8/lg==JyM5WVm0YwViWF9b"}  

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, headers=headers) as resp:
                if resp.status != 200:
                    return await ctx.send("❌ Failed to fetch quote.")
                data = await resp.json()

        if not data:
            return await ctx.send("⚠️ No quote data received.")

        quote_data = data[0]
        embed = nextcord.Embed(
            title=f"📖 Quote by {quote_data.get('author', 'Unknown')}",
            description=f"_{quote_data.get('quote', 'No quote text provided.')}_",
            color=nextcord.Color.blue()
        )
        await ctx.send(embed=embed)


    @commands.command(help="Get a random fact.")
    async def fact(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as resp:
                if resp.status != 200:
                    return await ctx.send("🤓 Couldn't find a fun fact.")
                data = await resp.json()
        embed = nextcord.Embed(
            title="📚 Did You Know?",
            description=data["text"],
            color=nextcord.Color.orange()
        )
        await ctx.send(embed=embed)



    def __init__(self, bot):
        self.bot = bot
        self.current_number = 0
        self.last_user = None
        self.streak = 0

    @commands.command(name="count", help="Start counting game. Use `!count <number>` to count.")
    async def count(self, ctx, number: int = None):
        # Ignore messages from bots
        if ctx.author.bot:
            return

        if number is None:
            await ctx.send("❗ Please provide a number to count. Usage: `!count <number>`")
            return

        # Check for correct next number
        if number == self.current_number + 1:
            # Check if same person counted twice
            if ctx.author == self.last_user:
                await ctx.send("❌ You can't count twice in a row!")
                return

            self.current_number += 1
            self.last_user = ctx.author
            self.streak += 1

            embed = nextcord.Embed(
                title="✅ Correct Count!",
                description=f"{ctx.author.mention} counted **{number}** correctly!",
                color=nextcord.Color.green()
            )
            embed.add_field(name="🔥 Streak", value=str(self.streak), inline=True)
            embed.add_field(name="📈 Next Number", value=str(self.current_number + 1), inline=True)
            embed.set_thumbnail(url=ctx.author.avatar.url if ctx.author.avatar else None)
            embed.set_footer(text="Keep counting together!")
            await ctx.send(embed=embed)
        else:
            # Wrong number
            embed = nextcord.Embed(
                title="❌ Wrong Count!",
                description=f"{ctx.author.mention} ruined the streak at **{number}** 😢",
                color=nextcord.Color.red()
            )
            embed.add_field(name="💔 Final Streak", value=str(self.streak), inline=True)
            embed.add_field(name="🔄 Game Restarted", value="Back to 1", inline=True)
            embed.set_thumbnail(url=ctx.author.avatar.url if ctx.author.avatar else None)
            await ctx.send(embed=embed)

            # Reset
            self.current_number = 0
            self.last_user = None
            self.streak = 0



def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun cog loaded.")


