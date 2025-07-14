import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Pat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="pat", description="Pat someone gently!")
    async def pat(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="Who are you patting?", required=True)
    ):
        gifs = [
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDA1bGNuMW1vZGVpdTV6bXhmcmIycG43djdzbzFxZDRpdnVpdGJjOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4HP0ddZnNVvKU/giphy.gif",
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3lwOHBmYjBsbmFzZjdsZjRnankxa2JudWlpeTVuNXE4NTNiYmt4dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5tmRHwTlHAA9WkVxTU/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExendwcDNqM21nY2xkN3lnNHRiczY3N3djY3hvbmM5aTFvMXFsYjVrbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ye7OTQgwmVuVy/giphy.gif",
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWdicmZuc3V3NHRuZDNyd2I5eDA4MzUxdXl3NzIxZjFhZ24zcjJ2eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/e7xQm1dtF9Zni/giphy.gif",
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxyZDBuZnhva2VrY25oOGtlcXZ1dzN5OHgwcmw0NDFta3lnd3Y0cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ARSp9T7wwxNcs/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OWJmcjQ4dWM3ZndybmpmcWJzbXFjMGpmaXlncjA2bWo5dndzcmVvOCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/w2OMjUGV7mCSQ/giphy.gif"
        ]
        chosen = random.choice(gifs)
        embed = nextcord.Embed(
            title="💆 Pat Time!",
            description=f"{interaction.user.mention} gave {user.mention} a gentle pat!",
            color=nextcord.Color.purple()
        )
        embed.set_image(url=chosen)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Pat ~")
        embed.timestamp = interaction.created_at
def setup(bot):
    bot.add_cog(Pat(bot))
