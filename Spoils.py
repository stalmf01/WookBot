from discord.ext import commands
import feedparser
import asyncio
from datetime import datetime
# from html.parser import HTMLParser


class Spoiler(commands.Cog):
    month_dict = {
                "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
                }

    def __init__(self, bot):
        self.bot = bot
        self.spoiler_feed = feedparser.parse("https://www.mtgsalvation.com/spoilers.rss")
        self.entry = self.spoiler_feed.entries
        self.earliest_date = datetime(year=2019, month=5, day=24, hour=23)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.feed_poll()

    async def feed_poll(self):
        await self.bot.wait_until_ready()
        while True:
            await asyncio.sleep(20)
            now = datetime.now()
            if now.minute % 3 == 0:
                self.spoiler_feed = feedparser.parse("https://www.mtgsalvation.com/spoilers.rss")
                self.entry = self.spoiler_feed.entries[:10]
                index = 9
                while index >= 0:
                    unparsed_date = self.entry[index].published.split()
                    day = int(unparsed_date[1])
                    month = self.month_dict[unparsed_date[2]]
                    year = int(unparsed_date[3])
                    time = unparsed_date[4].split(':')
                    hour = int(time[0])
                    min = int(time[1])
                    sec = int(time[2])
                    date = datetime(year=year, month=month, day=day, hour=hour, minute=min, second=sec)
                    if date > self.earliest_date:
                        self.earliest_date = date
                        for guild in self.bot.guilds:
                            for channel in guild.text_channels:
                                if channel.name == 'mtg':
                                    await channel.send(self.entry[index].link)
                    index -= 1

    """""
    @commands.command()
    async def spoilies(self, ctx):
        for spoil in self.entry:
            await ctx.send(spoil.published)
            print(spoil.published)
    """


def setup(bot):
    bot.add_cog(Spoiler(bot))
