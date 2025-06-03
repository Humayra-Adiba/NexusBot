import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__ (self,bot):
        self.bot = bot


    #Commands
    @commands.command()
    async def nexusbot(self,ctx):
        await ctx.send("Hi there👋, I am NexusBot!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Hello, Do you need help? 😄")

    #Events
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(1375436330443472928)
        if channel:
            await channel.send(f"Welcome {member.mention} to the server! Hope you have a great time here! 🎉")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(1375436330443472928)
        if channel:
            await channel.send(f"Goodbye {member.mention},hope to see you again!")


async def setup(bot):
    await bot.add_cog(Greetings(bot))
    print("Greetings cog loaded.")


