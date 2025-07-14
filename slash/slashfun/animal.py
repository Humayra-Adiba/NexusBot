import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Animal(commands.Cog):
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

    @nextcord.slash_command(name="animal", description="Get a random fact and image about an animal.")
    async def animal(
        self,
        interaction: Interaction,
        kind: str = SlashOption(
            description="Choose an animal",
            choices=list(ANIMAL_APIS.keys())
        )
    ):
        api = self.ANIMAL_APIS[kind]
        async with aiohttp.ClientSession() as session:
            async with session.get(api["url"]) as resp:
                if resp.status != 200:
                    return await interaction.response.send_message("⚠️ API error. Please try again later.")
                data = await resp.json()

        embed = nextcord.Embed(
            title=f"{api['emoji']} {kind.title()} Fact!",
            description=data.get("fact", "No fact found."),
            color=api["color"]
        )
        embed.set_image(url=data.get("image"))
        embed.set_footer(text="Powered by some-random-api.com • NexusBot ✨")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Animal(bot))
