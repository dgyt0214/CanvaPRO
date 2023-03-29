import nextcord
from nextcord.ext import commands

class Serverinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['si'])
    async def serverinfo(self, ctx, guild=None):
      if guild==None:
        guild = ctx.message.guild
      name = guild.name


      id = guild.id
      memberCount = guild.member_count
      roles = len(guild.roles)
      channels = len(guild.channels)

   
      embed = nextcord.Embed(
          title=name + " Server Information",
          color=nextcord.Color.blue()
        )
      embed.add_field(name="Owner", value="<@537846086749126657>", inline=True)
      embed.add_field(name="Server ID", value=id, inline=True)
      embed.add_field(name="Member Count", value=memberCount, inline=True)
      embed.add_field(name="# of roles:", value=roles, inline=True)
      embed.add_field(name="# of channels (including voice channels and categories):", value=channels, inline=True)
      await ctx.send(embed=embed)

    @commands.command(aliases=['mc'])
    async def membercount(self, ctx, guild=None):
      guild = ctx.message.guild
      memberCount = guild.member_count
      serverName = guild.name
      await ctx.send(f"{serverName} current member count is {memberCount}.")
      
def setup(client):
    client.add_cog(Serverinfo(client))