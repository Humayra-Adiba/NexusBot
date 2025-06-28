import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import random

class Cry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="cry", description="Show you're crying 😢")
    async def cry(self, interaction: Interaction):
        gifs = [
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3ozNGFjdjI2bG01djZhaTJ3eDluaHhnemw3d21iajdtem4wNnVpeCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/b5z9pHJxxcREI/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dTMxNHJ4OW9vY3U2cTM1d3BrYjk2dGRuNnA1NXB5eTczcHIyNmk4eCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/ujZtlj1Y7wXyE/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dTMxNHJ4OW9vY3U2cTM1d3BrYjk2dGRuNnA1NXB5eTczcHIyNmk4eCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/on9LDLF5JskaQ/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dTMxNHJ4OW9vY3U2cTM1d3BrYjk2dGRuNnA1NXB5eTczcHIyNmk4eCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/YhqyiijLeMCpq/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dTMxNHJ4OW9vY3U2cTM1d3BrYjk2dGRuNnA1NXB5eTczcHIyNmk4eCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/bTCX59I9dE1Bm/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dTMxNHJ4OW9vY3U2cTM1d3BrYjk2dGRuNnA1NXB5eTczcHIyNmk4eCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/XGS8suOMypcNq/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MXp2ZWN5aWpvOHI5NWtlODFsaHo2bjY3NGdrbjF1cWI1aHp0ODdzZCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/4xKJUTzWPAVoY/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MXp2ZWN5aWpvOHI5NWtlODFsaHo2bjY3NGdrbjF1cWI1aHp0ODdzZCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/Ui7MfO6OaLz4k/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MXp2ZWN5aWpvOHI5NWtlODFsaHo2bjY3NGdrbjF1cWI1aHp0ODdzZCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/yarJ7WfdKiAkE/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dDgxN3p6djUzODg1aTkzcHlscHdrYXEzY3Uybmw3czV6M2RveTV4dyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/oS4LjGIpwuE1O/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dDgxN3p6djUzODg1aTkzcHlscHdrYXEzY3Uybmw3czV6M2RveTV4dyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/OuKTQaitZH8Y/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dDgxN3p6djUzODg1aTkzcHlscHdrYXEzY3Uybmw3czV6M2RveTV4dyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/eDQSdixgEvsZ2/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aWZlOHZsbWp5eGRqMHlwNnNyN21zYW9haW1lYXp1b2k4cmphcWlxayZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/58jL8DlhVNgl2/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dTMxNHJ4OW9vY3U2cTM1d3BrYjk2dGRuNnA1NXB5eTczcHIyNmk4eCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/ZQRpLrGouynAs/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3emQ1c2tnOGo4dHp2cG54OXI0ajV4dXhzNjI2aGRoNXJ2OGJodWJndCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/xT1R9yzqpvhPETYoV2/giphy.gif",
        ]
        embed = nextcord.Embed(
            title=f"{interaction.user.display_name} is crying 😢. someone take care of this guy please!",
            color=nextcord.Color.blue()
        )
        embed.set_image(url=random.choice(gifs))
        embed.set_footer(text="It's okay to cry sometimes.")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Cry(bot))

    
