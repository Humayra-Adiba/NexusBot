import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="quote", description="Get a random inspirational quote")
    async def quote(self, interaction: Interaction):
        api_url = "https://api.api-ninjas.com/v1/quotes"
        headers = {"X-Api-Key": "n3hiONPoFysP2shoeg8/lg==JyM5WVm0YwViWF9b"}  # Replace with your actual API key

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, headers=headers) as resp:
                if resp.status != 200:
                    return await interaction.response.send_message("❌ Failed to fetch quote.")
                data = await resp.json()

        if not data:
            return await interaction.response.send_message("⚠️ No quote data received.")

        quote_data = data[0]
        embed = nextcord.Embed(
            title=f"📖 Quote by {quote_data.get('author', 'Unknown')}",
            description=f"_{quote_data.get('quote', 'No quote text provided.')}_",
            color=nextcord.Color.blue()
        )
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Quote(bot))
