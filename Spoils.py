from discord.ext import commands
import feedparser
import asyncio
from html.parser import HTMLParser


class Spoiler(commands.Cog):
    earliest_day = 0
    earliest_month = 0
    earliest_year = 0
    earliest_total_time = 0
    month_dict = {
                "Janurary": 1,
                "Febuary": 2,
                "March": 3,
                "April": 4,
                "May": 5
                }

    def __init__(self, bot):
        self.bot = bot
        self.spoiler_feed = feedparser.parse("https://www.mtgsalvation.com/spoilers.rss")
        self.entry = self.spoiler_feed.entries

    @commands.Cog.listener()
    async def on_ready(self):
        await self.feed_poll()
        print('here')

    # count down loop
    async def feed_poll(self):
        await self.bot.wait_until_ready()
        while True:
            self.spoiler_feed = feedparser.parse("https://www.mtgsalvation.com/spoilers.rss")
            self.entry = self.spoiler_feed.entries[:10]
            print(self.entry[0].updated_parsed)
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
                total_time = hour*360 + min*60 + sec
                print(str(hour) + ' ' + str(min) + ' ' + str(sec))
                print(str(month) + ' ' + str(day))
                print(total_time)
                print(self.earliest_total_time)
                if month >= self.earliest_month and day >= self.earliest_day and year >= self.earliest_year:
                    if total_time > self.earliest_total_time:
                        self.earliest_day = day
                        self.earliest_month = month
                        self.earliest_year = year
                        self.earliest_total_time = total_time
                        channel = self.bot.get_channel(576436682879008780)
                        print((self.entry[index].link))
                        # await channel.send(self.entry[index].link)
                        index -= 1
            await asyncio.sleep(50)
    """""
    @commands.command()
    async def spoilies(self, ctx):
        for spoil in self.entry:
            await ctx.send(spoil.published)
            print(spoil.published)
    """


def setup(bot):
    bot.add_cog(Spoiler(bot))
