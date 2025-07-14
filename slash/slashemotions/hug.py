import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="hug", description="Give someone a warm hug 🤗")
    async def hug(self, interaction: Interaction,
                member: nextcord.Member = SlashOption(description="User to hug", required=True)
    ):
        gifs = [
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG1lNHVoMmt0empqOGZpZjI1dnJ6ajE1eDRzMTAyYTlwNGFxNWphbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10BcGXjbHOctZC/giphy.gif"
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzdxcnNwdnRiZ3Q5NDRqNHcyaTRmZzN6ZjEwc3Y5bHE0ZmhsbW1rZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wSY4wcrHnB0CA/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExczliZjhyY3JkMmxhcm15bDlqZzBmZGFvemtxcjQ4bWF4Y2FxY3RrbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/od5H3PmEG5EVq/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzVtZHVsZHNkaDQ1eDE0OGd4MHBjaHBtNWhxbHVpbzJ3NzF1dnV4byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/du8yT5dStTeMg/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzVtZHVsZHNkaDQ1eDE0OGd4MHBjaHBtNWhxbHVpbzJ3NzF1dnV4byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/du8yT5dStTeMg/giphy.gif",
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWVhMHhsYnY5cGd1NHgzaTJjaTNkZnhvNHV0ZTc3cXR2MGhtdnZhNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lrr9rHuoJOE0w/giphy.gif",
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExenc4Zms0enhmOWF4bmdmem12andhNjR6cW96cm1tcW5sb29qdTZ2ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wnsgren9NtITS/giphy.gif",
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHQ0MDlwYnN6Y2gydnprN24yb3lndjV2MmF4Z2phemUyZzgyb3ZtdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JUwliZWcyDmTQZ7m9L/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3YWE2MzJvOWx3ZDZvcXduMm4ybXVmbHVnNGVudHg2MzFvdnR1OW8waSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/svXXBgduBsJ1u/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bGZydTR2bWNrcm9tcTY0OGhsMms5cmVxYW1kemJ5N2dqeG5lZWl1dCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/143v0Z4767T15e/giphy.gif",

        ]

        gif_url = random.choice(gifs)
        embed = nextcord.Embed(
            title="A warm hug!💞",
            description=f"{interaction.user.mention} gives {member.mention} a big hug!!!🥰 ",
            color=nextcord.Color.green()
        )
        embed.set_image(url=gif_url)
        embed.set_footer(text="Hugs are the best! :3")
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Hug(bot))
