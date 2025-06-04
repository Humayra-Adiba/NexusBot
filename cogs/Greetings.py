import nextcord
from nextcord.ext import commands
import random

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

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if "hello" in message.content.lower():
            await message.channel.send(f"Hello {message.author.mention}! How can I assist you today?")

        if "help" in message.content.lower():
            await message.channel.send(f"Hi {message.author.mention}! If you need assistance, feel free to ask!")

        if "bye" in message.content.lower():
            await message.channel.send(f"Goodbye {message.author.mention}! Have a great day! Wishing you all the best! 🌟")



def setup(bot):
    bot.add_cog(Greetings(bot))
    print("Greetings cog loaded.")


