from discord.ext import commands
import feedparser
from html.parser import HTMLParser


class Spoiler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.spoiler_feed = feedparser.parse("https://www.mtgsalvation.com/spoilers.rss")
        self.entry = self.spoiler_feed.entries
        print(self.entry)

    @commands.command()
    async def spoilies(self, ctx):
        parser = HTMLParser
        for spoil in self.entry:
            r
            await ctx.send(spoil.link)


def setup(bot):
    bot.add_cog(Spoiler(bot))
