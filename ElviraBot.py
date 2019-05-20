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
    """
    @commands.command(description='Adds event to event calendar:')
    async def schedule(self, ctx, event, month, day, time):
        print('scheduling')
        await ctx.send('event added')
    """
    @commands.command()
    async def advice(self, ctx):
        await ctx.send(random.choice(self.choices))
    """
    #@commands.command()
    #async def add_advice(self, ctx, advice):
    #   
    #   await ctx.send('Thank you for the advice!')
    """

    @commands.Cog.listener()
    async def on_ready(self):
        print('Upcoming event:')


def setup(bot):
    bot.add_cog(ElviraCog(bot))
