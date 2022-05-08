import discord
from discord.ext import commands
import os
import sys

intents = discord.Intents.default()
token = os.getenv('DISCORD')
client = commands.Bot(command_prefix="server-mc:", help_command=None, intents=intents)

status = sys.argv[1]


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(status))


client.run(token)