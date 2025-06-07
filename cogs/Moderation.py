import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def logs(self, guild_id):
        return None

    async def send_dm(self, member, action, guild_name, reason):
        try:
            await member.send(
                f"You have been **{action}** from **{guild_name}**.\nReason: **{reason or 'No reason provided'}**"
            )
        except discord.Forbidden:
            pass  # Member has DMs closed or blocked the bot

    async def send_log(self, guild, title, member, moderator, reason):
        log_channel = self.bot.get_channel(self.logs(guild.id))
        if log_channel:
            embed = discord.Embed(
                title=title,
                description=f"**User:** {member}\n**Moderator:** {moderator}\n**Reason:** {reason or 'No reason provided'}",
                color=0x2F3136
            )
            await log_channel.send(embed=embed)

    @commands.command(help="Kick a user from the server.")
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author == member:
            return await ctx.send("🚫 You can't kick yourself!")

        if ctx.author.top_role <= member.top_role:
            return await ctx.send("🎈 You cannot kick this member. Their role is higher or equal to yours.")

        if ctx.me.top_role <= member.top_role:
            return await ctx.send("🔐 I can't kick this member because their role is higher than mine.")

        try:
            await self.send_dm(member, "kicked", ctx.guild.name, reason)
            await member.kick(reason=reason)

            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=f"✅ {member} has been kicked", icon_url=member.display_avatar.url)
            embed.set_footer(text=f"Command invoked by {ctx.author}")
            await ctx.send(embed=embed)

            await self.send_log(ctx.guild, "Kick 🦶", member, ctx.author, reason)

        except discord.Forbidden:
            await ctx.send("⚠️ I don't have permission to kick this member.")
        except discord.HTTPException as e:
            await ctx.send(f"❌ Failed to kick member: {e}")

    @commands.command(help="Ban a user from the server.")
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author == member:
            return await ctx.send("🚫 You can't ban yourself!")

        if ctx.author.top_role <= member.top_role:
            return await ctx.send("🚫 You cannot ban this member. Their role is higher or equal to yours.")

        if ctx.me.top_role <= member.top_role:
            return await ctx.send("🔐 I can't ban this member because their role is higher than mine.")

        try:
            await self.send_dm(member, "banned", ctx.guild.name, reason)
            await member.ban(reason=reason)

            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=f"✅ {member} has been banned", icon_url=member.display_avatar.url)
            embed.set_footer(text=f"Command invoked by {ctx.author}")
            await ctx.send(embed=embed)

            await self.send_log(ctx.guild, "Ban 🔨", member, ctx.author, reason)

        except discord.Forbidden:
            await ctx.send("⚠️ I don't have permission to ban this member.")
        except discord.HTTPException as e:
            await ctx.send(f"❌ Failed to ban member: {e}")

    @commands.command(help="Send a welcome message to a user.")
    async def message(self, ctx, user: nextcord.Member, *, message: str = "Welcome to the server! You are now a member of NexusBot!"):
        embed = nextcord.Embed(
            title="Message from NexusBot",
            description=message,
            color=nextcord.Color.green()
        )
        embed.set_footer(text=f"Sent by {ctx.author.name}", icon_url=ctx.author.avatar.url)

        try:
            await user.send(embed=embed)
            await ctx.send(f"✅ Message sent to {user.mention} successfully! 💌")
        except nextcord.Forbidden:
            await ctx.send(f"❌ Could not send a message to {user.mention}. They might have DMs disabled.")

def setup(bot):
    bot.add_cog(Moderation(bot))
    print("Moderation cog loaded.")
