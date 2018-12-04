import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = '?')
chatFilter = ['HECK', 'APPLE']

@client.event
async def on_ready():
    print('Bot is online')

@client.event
async def on_message(message):
    contents = message.content.split(' ')
    for word in contents:
        if word.upper() in chatFilter:
            try:
                await client.delete_message(message)
                await client.send_message(message.channel, "Don't use that word blyat")
            except discord.errors.NotFound:
                return



client.run("NTE5NDIyNjMyNzMxNDc1OTY4.DufFlw.Epy5mRtsYSNmbSSaODuDlAJw4BM")

