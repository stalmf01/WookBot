import discord
import random
from _datetime import datetime
from discord.ext import commands


class ElviraCog(commands.Cog):
    event_flag = 0
    choices = []

    def __init__(self, bot):
        self.bot = bot
        with open('advice.txt', 'r') as advice_file:
            for line in advice_file:
                self.choices.append(line)

    @commands.command()
    async def advice(self, ctx):
        await ctx.send(random.choice(self.choices))

    @commands.Cog.listener()
    async def on_ready(self):
        print('Upcoming event:')


def setup(bot):
    bot.add_cog(ElviraCog(bot))
