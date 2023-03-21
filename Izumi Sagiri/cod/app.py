import nextcord
from nextcord.ext import commands
import opencc
from opencc import OpenCC

class SayCog(commands.Cog, name="say"):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.message_command(name="say")
    async def _say(self, interaction: nextcord.Interaction, message: nextcord.Message):
        tw_to_cn = opencc.OpenCC('t2s')
        await interaction.response.send_message(tw_to_cn.convert(message.content), ephemeral=True)

def setup(bot):
    bot.add_cog(SayCog(bot))
