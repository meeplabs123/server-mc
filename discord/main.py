import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
token = os.getenv('DISCORD')

status = "Test Status"


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(status))


client.run(token)