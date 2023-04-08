import io
import nextcord,aiohttp
from nextcord.ext import commands

class ImageTransferCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Replace these with your own channel and server IDs
        self.source_channel_id = 978924240776609803
        self.source_server_id = 978680658740260865
        self.destination_channel_id = 1087930639770193951
        self.destination_server_id = 1009522455674617867

    @commands.Cog.listener()
    async def on_message(self, message):
        # Only process messages in the specified source channel and server
        if message.channel.id == self.source_channel_id and message.guild.id == self.source_server_id:
            # Check if the message contains an attachment
            if message.attachments:
                # Get the first attachment and its URL
                attachment = message.attachments[0]
                url = attachment.url

                # Get the destination server and channel objects
                destination_server = self.bot.get_guild(self.destination_server_id)
                destination_channel = destination_server.get_channel(self.destination_channel_id)

                # Send the attachment to the destination channel
                await destination_channel.send(file=await self.url_to_file(url))

    # Utility function to convert an image URL to a file object
    async def url_to_file(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                buffer = await response.read()
                file = nextcord.File(io.BytesIO(buffer), filename='image.png')
                return file

def setup(bot):
    bot.add_cog(ImageTransferCog(bot))
