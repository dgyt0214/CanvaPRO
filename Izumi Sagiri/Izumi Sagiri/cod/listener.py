import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_id = 1009522455674617867 # replace with the ID of the server you want to target


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == self.server_id:
            if (message.author.id == 812208568543608863 or message.author.id == 537846086749126657) and ('class' in message.content):
                    channel = message.channel
                    await channel.send('https://cdn.discordapp.com/attachments/1073692476705095770/1087044077515702352/image-62.png')
            elif message.author.id == 795213037095092234 and ('class' in message.content):
                    channel = message.channel
                    await channel.send("https://cdn.discordapp.com/attachments/1068920606277505034/1087352195827118111/image.png")
            elif message.content == "mingchai":
                    channel=message.channel
                    await channel.send("https://cdn.discordapp.com/attachments/1068920606277505034/1087277099477368832/IMG-20221228-WA0064.jpg")
            elif message.content == "mingquan":
                    channel=message.channel
                    await channel.send("https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/msnbc/Components/Photos/051006/051006_croc_hmed.jpg")         
            elif message.author.id == 551273144535613442 and ('class' in message.content):
                    channel = message.channel
                    await channel.send("https://cdn.discordapp.com/attachments/1075053012457902190/1087358231371862096/image.png")
            elif message.content == "yuhe":
                    channel=message.channel
                    await channel.send("https://cdn.discordapp.com/attachments/1068920606277505034/1087914150304419870/IMG-20221228-WA0063.jpg")
            elif message.content == "kelvin":
                    channel=message.channel
                    await channel.send("https://cdn.discordapp.com/attachments/1075061997248458824/1087929474294751292/IMG-20230322-WA0000.jpg")        
            elif message.content == "darren":
                    channel=message.channel
                    await channel.send("https://cdn.discordapp.com/attachments/1068920606277505034/1087934528628203520/IMG-20230106-WA0003.jpg")
            elif message.content == "jiajing":
                    channel=message.channel
                    await channel.send("https://cdn.discordapp.com/attachments/1068920606277505034/1087935065457164348/IMG-20230104-WA0002.jpg")            
def setup(bot):
    bot.add_cog(MyCog(bot))
