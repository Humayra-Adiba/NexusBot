import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
import discord
from nextcord.utils import get
import asyncio

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

    @commands.command(help="Warn a user with a reason.")
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: nextcord.Member, *, reason="No reason provided."):
        # Role hierarchy check
        if member.top_role >= ctx.author.top_role and ctx.author != ctx.guild.owner:
            return await ctx.send("❌ You can't warn this user because their role is higher or equal to yours.")
        
        if member == ctx.author:
            return await ctx.send("❌ You can't warn yourself.")

        if member == ctx.guild.me:
            return await ctx.send("❌ I can't warn myself!")

        # Send warning embed to channel
        embed = nextcord.Embed(
            title="⚠️ User Warned",
            description=f"{member.mention} has been warned.",
            color=nextcord.Color.orange()
        )
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Warned by", value=ctx.author.mention, inline=True)
        embed.set_footer(text=f"User ID: {member.id}")
        await ctx.send(embed=embed)

        # Try sending DM to the warned user
        try:
            dm_embed = nextcord.Embed(
                title="⚠️ You were Warned",
                description=f"You were warned in **{ctx.guild.name}**.",
                color=nextcord.Color.red()
            )
            dm_embed.add_field(name="Reason", value=reason, inline=False)
            dm_embed.add_field(name="Warned by", value=ctx.author.name, inline=True)
            await member.send(embed=dm_embed)
        except nextcord.Forbidden:
            await ctx.send("⚠️ Couldn't DM the user.")

    @commands.command(name="mute", help="Mute a user. Usage: !mute @user [duration in minutes] [reason]")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: nextcord.Member, duration: int = 0, *, reason: str = "No reason provided"):
        guild = ctx.guild

        # Prevent muting admins or users above the bot
        if member.top_role >= ctx.author.top_role and ctx.author != guild.owner:
            return await ctx.send("❌ You can't mute someone with equal or higher role than you.")
        
        if member.top_role >= guild.me.top_role:
            return await ctx.send("❌ I can't mute this user because their role is higher than mine.")

        mute_role = get(guild.roles, name="Muted")

        # Create role if not exists
        if not mute_role:
            mute_role = await guild.create_role(name="Muted", reason="Mute role for muting members")
            for channel in guild.channels:
                await channel.set_permissions(mute_role, send_messages=False, speak=False, add_reactions=False)

        await member.add_roles(mute_role, reason=reason)

        embed = nextcord.Embed(
            title="🔇 Member Muted",
            description=f"{member.mention} has been muted.",
            color=nextcord.Color.red()
        )
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Duration", value=f"{duration} minutes" if duration > 0 else "Indefinite", inline=False)
        embed.set_footer(text=f"Muted by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

        if duration > 0:
            await asyncio.sleep(duration * 60)
            await member.remove_roles(mute_role)
            try:
                await member.send(f"You have been unmuted in **{ctx.guild.name}**.")
            except:
                pass

            unmute_embed = nextcord.Embed(
                title="🔊 Member Unmuted",
                description=f"{member.mention} has been automatically unmuted after {duration} minutes.",
                color=nextcord.Color.green()
            )
            await ctx.send(embed=unmute_embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
    print("Moderation cog loaded.")
