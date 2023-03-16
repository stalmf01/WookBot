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

    @commands.Cog.listener()
    async def on_ready(self):
        await self.poll()

    async def poll(self):
        await self.bot.wait_until_ready()
        self.images = ImageList(self.list_count)
        while True:
            await asyncio.sleep(20)
            geturl = requests.get(self.URL)
            soup = BeautifulSoup(geturl.text, 'html.parser')
            images_html = soup.find_all('img', limit=25 + self.list_count)
            images_html = images_html[25:]
            print(f'{len(images_html)}')
            for image in images_html:
                if self.images.add(self.base_url + image.get('src').strip()):
                    print(self.images)
                    print(f'New image {self.base_url + image.get("src").strip()}')
                    for guild in self.bot.guilds:
                        for channel in guild.text_channels:
                            if channel.name == 'mtg':
                                await channel.send(self.base_url + image.get('src').strip())


def setup(bot):
    bot.add_cog(Spoiler(bot))
