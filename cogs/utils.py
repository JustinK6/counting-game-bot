import discord

from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command()
    @has_permissions(administrator = True, manage_messages = True, manage_roles = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        try:
            await member.kick(reason = reason)
            await ctx.send(f'{str(member)} has been kicked.')
        except Exception as error:
            await ctx.send(f"Can't kick {str(member)} : {error}")

    @commands.command()
    @has_permissions(administrator = True, manage_messages = True, manage_roles = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        try:
            await member.ban(reason = reason)
            await ctx.send(f'{str(member)} has been banned.')
        except Exception as error:
            await ctx.send(f"Can't ban {str(member)} : {error}")

    @commands.command()
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount + 1)

def setup(client):
    client.add_cog(Utils(client))