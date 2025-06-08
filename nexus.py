import os
import asyncio
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')

intents = nextcord.Intents.default()  # Or .all() if you need more access
intents.message_content = True       # Required for reading message content
intents.members = True              # Required for member events

client = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)


@client.event
async def on_ready():
    await client.change_presence(
        status=nextcord.Status.online,
        activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="this server")
    )
    print("Bot is ready!")



def load_extensions():
    for folder in ["cogs", "slash"]:
        for filename in os.listdir(folder):
            if filename.endswith(".py"):
                try:
                    client.load_extension(f"{folder}.{filename[:-3]}")
                    print(f"{filename[:-3]} cog loaded.")
                except Exception as e:
                    print(f"Failed to load {filename}: {e}")


if __name__ == "__main__":
    load_extensions()
    client.run(token)

