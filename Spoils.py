from discord.ext import commands
import feedparser
from html.parser import HTMLParser


class Spoiler(commands.Cog):
    earliest_published = 0

    def __init__(self, bot):
        self.bot = bot
        self.spoiler_feed = feedparser.parse("https://www.mtgsalvation.com/spoilers.rss")
        self.entry = self.spoiler_feed.entries
        print(self.entry)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.feed_poll()

    async def feed_poll(self):
        await self.bot.wait_until_ready()
        while True:
            self.spoiler_feed = feedparser.parse("https://www.mtgsalvation.com/spoilers.rss")
            self.entry = self.spoiler_feed.entries[:10]
            for spoil in self.entry:
                print(spoil.published.split())

    @commands.command()
    async def spoilies(self, ctx):
        for spoil in self.entry:
            await ctx.send(spoil.published)
            print(spoil.published)


def setup(bot):
    bot.add_cog(Spoiler(bot))
