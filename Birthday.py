from discord.ext import commands
from datetime import datetime
import asyncio
import discord
import BirthDate


class BirthdayList(commands.Cog):
    users = []

    def __init__(self, bot):
        with open('Birthdays.txt', 'r') as birthday_file:
            for line in birthday_file:
                words = line.split(',')
                guild = words[0]
                user = words[1]
                channel = words[2]
                display_name = words[3]
                month = words[4]
                day = words[5]
                user = BirthDate.UsersBirthdays(guild=guild, user=user, channel=channel, display_name=display_name,
                                                month=month, day=day)
                self.users.append(user)
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('starting date poll')
        await self.birthday()

    async def birthday(self):
        await self.bot.wait_until_ready()

        while True:
            now = datetime.now()
            hour = now.hour
            await asyncio.sleep(50)
            if hour == 8:
                for user in self.users:
                    if user.get_day() == now.day and user.get_month() == now.month and user.celebrated != now.year:
                        guild = self.bot.get_guild(user.get_guild())
                        channels = guild.text_channels
                        for channel in channels:
                            if channel.name == user.channelid:
                                user.set_celebrated(now.year)
                                await channel.send('@everyone happy birthday ' + user.display_name)

    @commands.command(description='adds your birthday to the list to be celebrated')
    async def addbirthday(self, ctx, month, day):
        if int(month) > 12 or int(month) < 1:
            await ctx.send('Invalid number for month')
            return
        if int(day) > 31 or int(day) < 1:
            await ctx.send('Invalid number for day')
            return

        author = ctx.message.author.id
        for user in self.users:
            if author == user.userid:
                await ctx.send('you are already on the birthday list')
                return

        user = BirthDate.UsersBirthdays(guild=ctx.message.author.guild.id, user=ctx.author.id,
                                        channel='general', display_name=ctx.message.author.display_name,
                                        month=month, day=day)
        self.users.append(user)
        for user in self.users:
            if user.get_userid() == author:
                user.write_to_file()
                await ctx.send('you have been added to the birthday list')
                return
        await ctx.send('something went wrong')

    @commands.command(description='checks if you are on the birthday list')
    async def get_birthday(self, ctx):
        author = str(ctx.message.author.id)
        for user in self.users:
            if author == user.userid:
                await ctx.send('your birthday is on ' + user.month + ' ' + user.day)
                return
        await ctx.send('your birthday is not on the list type ?addbirthday month day to add you birthday')

    @commands.command(description='returns all the birthdays in this guild')
    async def get_birthdays(self, ctx):
        embed = discord.Embed(title='list of birthdays in the guild')
        for member in ctx.guild.members:
            for user in self.users:
                if member == self.bot.get_user(user.get_userid()):
                    embed.add_field(name=user.display_name, value=user.month + ' ' + user.day)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BirthdayList(bot))
