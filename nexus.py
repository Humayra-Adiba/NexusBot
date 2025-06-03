import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()  # Or .all() if you need more access
intents.message_content = True       # Required for reading message content
intents.members = True              # Required for member events

client = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.watching, name="this server")
    )
    print("Bot is ready!")



async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded cog: {filename[:-3]}")

async def main():
    await load_cogs()
    await client.start(token)

asyncio.run(main())

