import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

class Join(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
        self.server_id = 1009522455674617867 # replace with the ID of the server you want to target

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == self.server_id:
            channel = self.bot.get_channel(1068920606277505034)
            embeds = nextcord.Embed(title="Cyberbully", description="网络霸凌", color=0xe32626)
            embeds.add_field(name="Something You Should Need To Know", value=f"{member.mention} We dont cyberbullying other!", inline=False)
            embeds.set_image("https://genshin.global/wp-content/uploads/2023/02/hutao-yelan-xiao-lantern-rite-2023-official-wallpaper-genshin.jpg")
            await channel.send(embed=embeds)

def setup(bot):
    bot.add_cog(Join(bot))
