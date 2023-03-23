import asyncio
import os
import spotify
import nextcord
import yt_dlp as youtube_dl
from nextcord.ext import commands
from nextcord.ext.commands import BadArgument
from core.simple_queue import Queue


# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'encoding': 'utf_8',
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(nextcord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')
        self.duration = data.get('duration')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(nextcord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = Queue()
        self.bg_task = None

    @commands.command()
    async def join(self, ctx, *, channel: nextcord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            self.queue.push(url)
            if not ctx.voice_client.is_playing():
                self.play_songs(ctx)
        
        await ctx.send(f'Added to queue!'.encode('UTF-8').decode())


    @commands.command()
    async def skip(self, ctx):
        """Skips the current song"""

        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send('Skipped!')
            if not self.queue.isEmpty():
                self.play_songs(ctx)
                
    @commands.command()
    async def songlist(self, ctx):
        """Displays the list of songs in the queue"""
        if not self.queue.isEmpty():
            songs = '\n'.join(self.queue.get_list())
            embed = nextcord.Embed(title="Songs in the queue", description=songs, color=nextcord.Color.blue())
            await ctx.send(embed=embed)
        else:
            await ctx.send('```\nNo songs in the queue\n```')        

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        self.queue.clear()
        await ctx.voice_client.disconnect()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")

    def play_songs(self, ctx):
        self.bg_task = self.bot.loop.create_task(self.play_songs_task(ctx))

    async def play_songs_task(self, ctx):
        if not self.queue.isEmpty():
            try:
                url = self.queue.pop()
                print(url)
                if ctx.voice_client.is_playing() or url is None:
                    return
                player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                print(f'[{player.title}] playing...')
                ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else self.play_songs(ctx))
                await ctx.send(f'Now playing: {player.title}')
            except Exception as e:
                print(e)
                await ctx.send(f'An error occured: {e}')
        else:
            print('Queue empty, stopping...')
            await ctx.send('Queue empty, goodbye!')
            await ctx.voice_client.disconnect()
            
    
activity = nextcord.Activity(name='music.', type=nextcord.ActivityType.listening)

            
def setup(bot):
    bot.add_cog(Music(bot))
