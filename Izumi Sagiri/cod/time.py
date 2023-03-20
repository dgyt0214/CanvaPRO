import nextcord
from nextcord.ext import commands, tasks
import datetime

class Scheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.send_message.start()

    @tasks.loop(seconds=60)  # check every 60 seconds
    async def send_message(self):
        now = datetime.datetime.now().strftime("%A %H:%M")
        if now == "Tuesday 07:30":
            channel = await self.bot.fetch_channel(1073692476705095770)  
            await channel.send("<@551273144535613442> , <@812208568543608863> , <@795213037095092234> , <@537846086749126657> Its Time to class at 8 am mfker")
        elif now == "Tuesday 07:40":
            channel = await self.bot.fetch_channel(1073692476705095770)  
            await channel.send("<@551273144535613442> , <@812208568543608863> , <@795213037095092234> , <@537846086749126657> Its Time to class at 8 am mfker")
        elif now == "Tuesday 07:50":
            channel = await self.bot.fetch_channel(1073692476705095770)  
            await channel.send("<@551273144535613442> , <@812208568543608863> , <@795213037095092234> , <@537846086749126657> Its Time to class at 8 am mfker")
        elif now == "Tuesday 07:55":
            channel = await self.bot.fetch_channel(1073692476705095770)  
            await channel.send("<@551273144535613442> , <@812208568543608863> , <@795213037095092234> , <@537846086749126657> Its Time to class at 8 am mfker")
        elif now == "Tuesday 09:30":
            channel = await self.bot.fetch_channel(1073692476705095770)  
            await channel.send("<@551273144535613442> , <@812208568543608863> , <@795213037095092234> , <@537846086749126657> 10am Have Class Dont Forget")
        elif now == "Wednesday 15:30":
            channel = await self.bot.fetch_channel(1073692476705095770)  
            await channel.send("<@812208568543608863>  , <@537846086749126657> 4pm Have Class Dont Forget : ) :miko_1~3: ")

    @send_message.before_loop
    async def before_send_message(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Scheduler(bot))
