from discord.ext import commands
import feedparser
import asyncio
from datetime import datetime, timedelta
# from html.parser import HTMLParser


class Spoiler(commands.Cog):
    month_dict = {
                "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "Jun": 6,
                "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
                }

    def __init__(self, bot):
        self.bot = bot
        self.spoiler_feed = feedparser.parse("https://www.mtgsalvation.com/spoilers.rss")
        self.entry = self.spoiler_feed.entries
        self.earliest_date = datetime.now()
        self.earliest_date += timedelta(hours=3)

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
                if len(self.spoiler_feed.entries) < 10:
                    index = len(self.spoiler_feed.entries) - 1
                else:
                    self.entry = self.spoiler_feed.entries[:10]
                    index = 9
                while index >= 0:
                    date_struct = self.entry[index].published_parsed
                    date = datetime(year=date_struct.tm_year, month=date_struct.tm_mon, day=date_struct.tm_mday,
                                    hour=date_struct.tm_hour, minute=date_struct.tm_min, second=date_struct.tm_sec)
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
