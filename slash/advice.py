import aiohttp
import json
import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Advice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="advice", description="Get a useful piece of advice")
    async def advice(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.adviceslip.com/advice") as resp:
                if resp.status != 200:
                    return await interaction.response.send_message("🧠 Couldn't fetch advice.")

                text = await resp.text()
                try:
                    data = json.loads(text)
                except Exception as e:
                    return await interaction.response.send_message(f"❌ Error: {e}")

        embed = nextcord.Embed(
            title="📌 Advice for You",
            description=data["slip"]["advice"],
            color=nextcord.Color.green()
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1040/1040204.png")
        embed.set_footer(text="NexusBot • Advice is optional, wisdom is eternal 💡")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Advice(bot))
