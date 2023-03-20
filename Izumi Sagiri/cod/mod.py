import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

class mod(Cog_Extension):
        
        @commands.command()
        async def purge(self,ctx, limit: int):
                if ctx.author.guild_permissions.manage_messages: # Check if the member has the required permission
                        await ctx.channel.purge(limit=limit+1)
                        await ctx.send(f'{limit} messages deleted', delete_after=5)
                else:
                        await ctx.send("You do not have the required permissions to use this command.", delete_after=5)

def setup(bot):
        bot.add_cog(mod(bot))
