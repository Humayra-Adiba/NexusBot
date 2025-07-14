import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Smile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="smile", description="Smile at someone warmly 😊")
    async def smile(
        self,
        interaction: Interaction,
        member: nextcord.Member = SlashOption(
            name="member",
            description="Who are you smiling at?",
            required=True
        )
    ):
        gifs = [
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2R1N2d3dHh6amRzZnFtdG1xbTU2NTNxcGkxMXRmdTF3aTN2NXB6dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nf9OkHHKlpZRK/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MWNneWcyeXNxamR4cHZzMThjb2ljNDVhaHJhbnBpbWVxb3BwN3VqcyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/WnTsYrfU1OXGE/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MWNneWcyeXNxamR4cHZzMThjb2ljNDVhaHJhbnBpbWVxb3BwN3VqcyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/J73J3JrCVJAEo/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dHRscDQ3eDRxdDlha3huZ3V4emZ2MTlqb2w2ZDA0ODQ3YjJmbXVpciZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/aqOUrkDo2fdyE/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmtpcm56dG02cXZtcXg5Y295MTM0MHU3cTdpaWI1OHR6bmthM2NzMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tXwHTbQuyjo1q/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bTFoNGI4ZGR4Y2xmMXhxMmV5anpmOXBraWMybDRndGsxZ3Y5aHlnNyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/CNUb51EbTxuRG/giphy.gif",
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcms3YjZsOXFtemxwdDVzaHphZ3Jjc2ZsNjkwcXZvZWoyOWNhMTd4dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bqSkJ4IwNcoZG/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3d3pubnUzM281ZXBzZHp2NGo4MGdlcjRjNDJnYWYxenFzZnI4Z242OSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/28AEi3TIvtSP6/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aDR3cGVjM3JybGhhODU2eXAyd3FxMGE1OTdkeTRmbnVtOWp4em9zeSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/rFfmUWVMOyKVG/giphy.gif"
        ]
        embed = nextcord.Embed(
            title="😊 A warm smile!",
            description=f"{interaction.user.mention} is smiling at {member.mention} 😊",
            color=nextcord.Color.green()
        )
        embed.set_image(url=random.choice(gifs))
        embed.set_footer(text="A smile shared is a joy doubled!")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Smile(bot))
