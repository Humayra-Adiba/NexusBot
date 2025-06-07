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

        


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if self.bot.user in message.mentions:
            guild_name = message.guild.name if message.guild else "NexusBot"
            embed = nextcord.Embed(
                title=guild_name.upper(), 
                description=(
                    f"Hello {message.author.mention}!\n\n"
                    f"You can use my commands here using the `!` prefix. Example: `!ping`\n\n"
                    f"You can view all my commands using the `!help` command.\n"
                    f"You can configure my settings on the dashboard (coming soon)."
                ),
                color=nextcord.Color.dark_purple()
            )
            avatar_url = self.bot.user.avatar.url if self.bot.user.avatar else self.bot.user.default_avatar.url

            embed.set_author(name=self.bot.user.name, icon_url=avatar_url)
            embed.set_thumbnail(url=avatar_url)

            embed.set_footer(text="NexusBot ✨")

            view = nextcord.ui.View()
            view.add_item(nextcord.ui.Button(label="Website", url="https://yourwebsite.com"))
            view.add_item(nextcord.ui.Button(label="Invite", url="https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot&permissions=8"))
            view.add_item(nextcord.ui.Button(label="Support", url="https://discord.gg/ySusFAKw"))

            await message.channel.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Greetings(bot))
    print("Greetings cog loaded.")


