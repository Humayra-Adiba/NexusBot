import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Hail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="hail", description="Send a greeting gif to someone!")
    async def greet(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="The user to greet", required=True)
    ):
        gifs = [
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3V1bHN5ZTZiMWRldmV2aWRla2x5N24wcnllbWdyY2oxNng3MXU4ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F99PZtJC8Hxm0/giphy.gif",
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmd1ZXA1amhvNjhzbjdxYjdzN25mcGlwc3A0MTJ0ajh2NjJ5NXV1ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yyVph7ANKftIs/giphy.gif",
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW1xZHh3MHdtZGcxMXdjNHY1NnQwY29wMzEzeXkzZmlrMnE4MHR0aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VUC9YdLSnKuJy/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGNmdXk2eTQ2NTc4bG94YzN1OWw0d29pOHN0bDd3eWx5dGdyMDlzbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qR1fIvTV6hN16/giphy.gif",
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExajUyMTdvOHlycmNndmt0a3diZ215cjVmdGtjaXd4czQ3eWhwaDBlbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ASd0Ukj0y3qMM/giphy.gif",
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2ZzaG44bnJ3cTF2ZXJqcTdtb2Vzc3M1NGRpOWpoeXFmYm1rd25pZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C6pu9lnGtZsnUo2ftC/giphy.gif",
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExenR5NDU1MGJkbGgzZjV4OGN2djd0dHZvdmdiODZ2cXZxZGNnanRiNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eEkMQpOdOY58tPbLY6/giphy.gif"
        ]

        chosen_gif = random.choice(gifs)

        embed = nextcord.Embed(
            title="👋 Greeting!",
            description=f"{interaction.user.mention} greets {user.mention} warmly!🤩",
            color=nextcord.Color.green()
        )
        embed.set_image(url=chosen_gif)
        embed.set_footer(text="Spread some smiles!", icon_url=interaction.user.display_avatar.url)
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Hail(bot))
    print("Greet command loaded.")
