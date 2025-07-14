import nextcord
from nextcord.ext import commands
import asyncio
import random
from datetime import datetime, timedelta

class Giveawaycog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="giveaway", help="🎉 Start a giveaway!!!\nUsage: !giveaway <duration> <unit> <winners> <prize>")
    async def giveaway(self, ctx, time: int, unit: str, winners: int, *, prize: str):
        # Validation
        unit = unit.lower()
        if unit not in ["minute", "hour", "day"]:
            return await ctx.send("❌ Invalid time unit. Choose from `minute`, `hour`, or `day`.")

        if not (1 <= winners <= 10):
            return await ctx.send("❌ Number of winners must be between 1 and 10.")

        # Convert duration
        unit_seconds = {"minute": 60, "hour": 3600, "day": 86400}
        duration_sec = time * unit_seconds[unit]
        end_time = datetime.now() + timedelta(seconds=duration_sec)
        end_timestamp = int(end_time.timestamp())

        # Giveaway Embed
        embed = nextcord.Embed(
            title="🎉 GIVEAWAY STARTED!",
            description=(
                f"**🎁 Prize:** {prize}\n \n"
                f"**🏆 Winners:** {winners}\n \n"
                f"**⏳ Ends:** <t:{end_timestamp}:R> / <t:{end_timestamp}:F>\n\n \n"
                f"📌 **How to Enter:** React with 🎉 to enter!\n\n \n"
                f"🔔 Hosted by: {ctx.author.mention}"
            ),
            color=nextcord.Color.purple()
        )
        embed.set_footer(text="Good luck! • NexusBot 💫")
        embed.timestamp = datetime.utcnow()

        message = await ctx.send(embed=embed)
        await message.add_reaction("🎉")

        await ctx.send(f"✅ Giveaway started by {ctx.author.mention} for **{prize}**! Ends in {time} {unit}(s).")

        # Wait for the duration
        await asyncio.sleep(duration_sec)

        try:
            updated_message = await ctx.channel.fetch_message(message.id)
            reaction = next((r for r in updated_message.reactions if str(r.emoji) == "🎉"), None)

            if not reaction:
                return await ctx.send("❌ No reactions found. Giveaway cancelled.")

            users = []
            async for user in reaction.users():
                if not user.bot:
                    users.append(user)

            if not users:
                return await ctx.send("❌ No one joined the giveaway. Cancelled.")

            winners = min(winners, len(users))
            selected = random.sample(users, winners)
            winner_mentions = ", ".join(user.mention for user in selected)

            result_embed = nextcord.Embed(
                title="🎊 GIVEAWAY ENDED!",
                description=f"**🎁 Prize:** {prize}\n\n🎉 Congratulations to: {winner_mentions}",
                color=nextcord.Color.green()
            )
            result_embed.set_footer(text="Thanks for participating! 🎈")

            await ctx.send(embed=result_embed)

        except Exception as error:
            await ctx.send(f"⚠️ An error occurred: `{error}`")

def setup(bot):
    bot.add_cog(Giveawaycog(bot))
    print("Giveawaycog loaded successfully!")