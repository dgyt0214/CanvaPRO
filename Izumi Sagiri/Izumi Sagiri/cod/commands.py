import nextcord,json
from nextcord.ext import commands
from core.classes import Cog_Extension
import time

class slashcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="ping", description="Shows the bot's ping")
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Pinging...")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong! `{ping:.2f} ms`")
        
    
def setup(bot):
    bot.add_cog(slashcommand(bot))