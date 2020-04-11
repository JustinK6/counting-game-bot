import discord

from discord.ext import commands
class CountingGame(commands.Cog):
  previous_number = -1

  def __init__(self, client):
    self.client = client

  #Events
  @commands.Cog.listener()
  async def on_message(self, message):
    channel = message.channel
    if str(channel) == "counting_game":
      if self.previous_number < 0 and message.content.isdigit():
        self.previous_number = int(message.content)
      else:
        if not (message.content.isdigit() and int(message.content) == self.previous_number + 1) or message.content[0] == '0':
          await message.channel.purge(limit = 1)

          member = message.author
          role = discord.utils.get(member.guild.roles, name = "Can't Count")
          await member.add_roles(role)
        else:
          self.previous_number = int(message.content)



def setup(client):
  client.add_cog(CountingGame(client))
