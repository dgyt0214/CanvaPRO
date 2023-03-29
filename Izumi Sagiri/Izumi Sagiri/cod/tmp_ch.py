from ast import Pass
import nextcord
import json
from nextcord.ext import commands
from core.classes import Cog_Extension

after_channel = []    #bot created list

class tmp_channel(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        global create_channel
        create_channel = {
            member:nextcord.PermissionOverwrite(manage_channels = True),    #Give the author of the voice owner can overwrite the channel
        }

        s = self.bot.get_guild(1009522455674617867)      #get server id
        s1 = s.get_channel(1068924748102389790)     #set tmp voice id
        s2 = s1.category

        if after.channel == None:   #If after change channel not at voice channel
            if int(before.channel.id) in after_channel:     #Before leave check the channel is create by bot or not
                await before.channel.delete()
                after_channel.remove(int(before.channel.id))
                print(f'-> Delete tmp_channel {before.channel.name}!')
            elif before.channel != None:    #if before at channel is other voice cahnnel
                if int(before.channel.id) in after_channel:
                    await before.channel.delete()
                    after_channel.remove(int(before.channel.id))
                    print(before.id)

        if before.channel == None:   #if before change channel not in voice channel
            if after.channel.id == 1068924748102389790:     #set tmp ch voice channel id
                try:
                    if int(before.channel.id) in after_channel:
                        await before.channel.delete()
                        after_channel.remove(int(before.channel.id))
                        print(f'-> Delete tmp_channel {before.channel.name}!')
                except:
                    now_channel = await s.create_voice_channel(f'└[{str(member).split("#")[0]}] Voice Channel', overwrites = create_channel, category = s2)  #set name
                    after_channel.append(int(now_channel.id))
                    await member.move_to(now_channel)
                    print(f'-> Create tmp_channel {now_channel.name}!')
            else:
                try:
                    if int(before.channel.id) in after_channel:
                        await before.channel.delete()
                        after_channel.remove(int(before.channel.id))
                        print(f'-> Delete tmp_channel {before.channel.name}!')
                except:
                    pass

        if before.channel != None and after.channel  != None:   #Change between two channel
            if after.channel.id == 1068924748102389790:     #set tmp ch voice channel id
                if int(before.channel.id) in after_channel:
                    await before.channel.delete()
                    after_channel.remove(int(before.channel.id))
                    print(f'-> Delete tmp_channel {before.channel.name}!')

                now_channel = await s.create_voice_channel(f'└[{str(member).split("#")[0]}] Voice Channel', overwrites = create_channel, category = s2)  #set name
                after_channel.append(int(now_channel.id))
                await member.move_to(now_channel)
                print(f'-> Create tmp_channel {now_channel.name}!')

            else:
                if int(before.channel.id) in after_channel:
                    await before.channel.delete()
                    after_channel.remove(int(before.channel.id))
                    print(f'-> Delete tmp_channel {before.channel.name}!')

def setup(bot):
    bot.add_cog(tmp_channel(bot))