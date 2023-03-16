from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from Images import ImageList


class Spoiler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list_count = 30
        self.URL = "https://mythicspoiler.com/newspoilers.html"
        self.base_url = "https://mythicspoiler.com/"
        self.images = None
        self.run = True

    @commands.Cog.listener()
    async def on_ready(self):
        await self.poll()

    # @commands.Cog.listener()
    # async def on_message(self, ctx):
    #     if ctx.bot:
    #         return
    #     if ctx.content.startswith('?') is False:
    #         return
        # if ctx.content

    @commands.command(name='kill', help='kill the bot if something bad happens')
    async def kill(self, ctx, kill):
        print('in kill')
        if int(kill) == 1 and self.run is False:
            self.run = True
            await self.poll()
            await ctx.send('Starting feed')
        elif int(kill) == 0:
            self.run = False
            await ctx.send("Ending feed")

    async def poll(self):
        await self.bot.wait_until_ready()
        self.images = ImageList(self.list_count)
        while self.run:
            await asyncio.sleep(3600)
            # await asyncio.sleep(5)
            geturl = requests.get(self.URL)
            soup = BeautifulSoup(geturl.text, 'html.parser')
            images_html = soup.find_all('img', limit=25 + self.list_count)
            images_html = images_html[25:]
            for image in reversed(images_html):  # start at the end of the list
                if self.images.add(self.base_url + image.get('src').strip()):
                    # print(self.images)
                    # print(f'New image {self.base_url + image.get("src").strip()}')
                    if len(self.images) >= self.list_count:
                        # print('sending image')
                        await self.send_image(self.base_url + image.get('src').strip())
                    else:
                        print(f'List is not full {len(self.images)}')
                        await asyncio.sleep(0.5)  # add a delay to make sure emtpy list items have different time stamps

    async def send_image(self, url):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                if channel.name == 'mtg':
                    await channel.send(url)


def setup(bot):
    bot.add_cog(Spoiler(bot))
