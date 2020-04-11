import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('WTF'))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if (filename.endswith('.py')):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Njk4MjM5MzEzODIwNzc4NTM3.XpEOZQ.VFbplUV6-bx__uG_lxAR8Dg2fcI')