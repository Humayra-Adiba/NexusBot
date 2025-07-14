import nextcord
from nextcord.ext import commands

class Pollcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll", help="Create a poll. Usage: !poll Question | Option 1 | Option 2 | Option 3")
    async def poll(self, ctx, *, args):
        parts = [p.strip() for p in args.split('|')]
        if len(parts) != 4:
            await ctx.send("❌ Invalid format. Use: `!poll Question | Option1 | Option2 | Option3`")
            return

        question, option1, option2, option3 = parts

        embed = nextcord.Embed(
            title="💹 Community Poll",
            description=(
                f"**{question}**\n\n"
                f"1️⃣ {option1}\n\n"
                f"2️⃣ {option2}\n\n"
                f"3️⃣ {option3} \n\n"
            ),
            color=nextcord.Color.blurple()
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        embed.set_footer(text="React below to vote! • NexusBot")
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2662/2662503.png")
        embed.timestamp = ctx.message.created_at

        poll_msg = await ctx.send(embed=embed)
        await poll_msg.add_reaction("1️⃣")
        await poll_msg.add_reaction("2️⃣")
        await poll_msg.add_reaction("3️⃣")

def setup(bot):
    bot.add_cog(Pollcog(bot))
    print("Pollcog loaded successfully!")
