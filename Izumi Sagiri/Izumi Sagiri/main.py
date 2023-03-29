# -*- coding: utf-8 -*- 
from encodings import utf_8
from lib2to3.pgen2 import token
from turtle import end_fill 
import os, json, nextcord, logging, datetime, random, time ,sentry_sdk ,asyncio,openai,requests
from opencc import OpenCC
from ssl import CHANNEL_BINDING_TYPES
from nextcord.ext import commands
from nextcord.ui import *
from nextcord import TextChannel
from nextcord.utils import get
server_id = 978680658740260865 # replace with your server ID
intents=nextcord.Intents.all() 
bot = commands.Bot(command_prefix='$',intents=nextcord.Intents.all()) 
with open ("utilis/test.json","r",encoding='utf8') as jfile:
  jdate=json.load(jfile)

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cod.{extension}')
    await ctx.send(f'load {extension} successful')
    print(f'-> Loaded {extension} successful!')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cod.{extension}')
    await ctx.send(f'unload {extension} succesful')
    print(f'-> Unloaded {extension} successful!')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cod.{extension}')
    await ctx.send(f'reload {extension} succesful')
    print(f'-> Reloaded {extension} successful!')
    
@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game("Use $help to cyberbully MIngQuan or just type mingquan"), status=nextcord.Status.online)
    print(f'Logged in as {bot.user.name}')

for filename in os.listdir('./cod'):
    if filename.endswith('.py'):
        bot.load_extension(f'cod.{filename[:-3]}')
        
if __name__ == "__main__":  
    bot.run(jdate['token'])