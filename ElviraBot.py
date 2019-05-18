import discord
from discord.ext import commands


class ElviraCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("it works")


def setup(bot):
    bot.add_cog(ElviraCog(bot))
