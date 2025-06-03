import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):
    def __init__ (self,bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author == member:
            await ctx.send("You can't kick yourself!")
            # return

        if ctx.author.top_role <= member.top_role:
            await ctx.send("You cannot kick this member.🎈")
            return

        if ctx.me.top_role <= member.top_role:
            await ctx.send("I can't kick this member because their role is higher than mine. 🔐")
            return

        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked from the server.🔥")


    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author == member:
            await ctx.send("You can't ban yourself!")
            return

        if ctx.author.top_role <= member.top_role:
            await ctx.send("You cannot ban this member.🎈")
            return

        if ctx.me.top_role <= member.top_role:
            await ctx.send("I can't ban this member because their role is higher than mine. 🔐")
            return

        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned from the server.🔥")

    @commands.command()
    async def message(self,ctx, user: discord.Member, *, message: str = "Welcome to the server! You are now a member of NexusBot!"):
        if not user:
            await ctx.send("Please mention a user to send a massage.")
            return

        embed = discord.Embed(
            title="Massage from NexusBot",
            description=message,
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Sent by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        
        try:
            await user.send(embed=embed)
            await ctx.send(f"Massage sent to {user.mention} successfully! 💌")
        except discord.Forbidden:
            await ctx.send(f"Could not send a massage to {user.mention}. They might have DMs disabled.")



async def setup(bot):
    await bot.add_cog(Moderation(bot))
    print("Moderation cog loaded.")