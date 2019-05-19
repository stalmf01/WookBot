from discord.ext import commands
from datetime import datetime
import asyncio
import discord
import BirthDate


class BirthdayList(commands.Cog):
    month = 0
    day = 0
    birthday_days = {}
    birthday_months = {}
    users = []

    def __init__(self, bot):
        with open('Birthdays.txt', 'r') as birthday_file:
            for line in birthday_file:
                words = line.split(' ')
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

    def get_day(self, user):
        return int(self.birthday_days[user])

    def get_month(self, user):
        return int(self.birthday_months[user])

    # need to change to object list
    async def birthday(self):
        await self.bot.wait_until_ready()
        birthday_flag = 0

        while True:
            now = datetime.now()
            hour = now.hour
            await asyncio.sleep(50)
            if hour == 8:
                for user in self.users:
                    if self.get_day(user) == now.day and self.get_month(user) == now.month and birthday_flag != now.day:
                        for guild in self.bot.guilds:
                            for member in guild.members:
                                if member == self.bot.get_user(int(user)):
                                    channels = guild.channels
                                    for channel in channels:
                                        if channel.name == 'general':
                                            birthday_flag = now.day
                                            await channel.send('@everyone happy birthday ' + member.display_name)

    @commands.command()
    async def addbirthday(self, ctx, month, day):
        if int(month) > 12 or int(month) < 1:
            await ctx.send('Invalid number for month')
            return
        if int(day) > 31 or int(day) < 1:
            await ctx.send('Invalid number for day')
            return

        author = str(ctx.message.author.id)
        for user in self.users:
            if author == user.userid:
                await ctx.send('you are already on the birthday list')
                return

        user = BirthDate.UsersBirthdays(guild=ctx.message.author.guild, user=ctx.author.id,
                                        channel='general', display_name=ctx.message.author.display_name,
                                        month=month, day=day)
        self.users.append(user)
        for user in self.users:
            if user.get_userid() == author:
                user.write_to_file()
                await ctx.send('you have been added to the birthday list')
                return
        await ctx.send('something went wrong')

    @commands.command()
    async def get_birthday(self, ctx):
        author = str(ctx.message.author.id)
        for user in self.users:
            if author == user.userid:
                await ctx.send('your birthday is on ' + user.month + ' ' + user.day)
                return
        await ctx.send('your birthday is not on the list type ?addbirthday month day to add you birthday')

    # look at this command
    @commands.command()
    async def get_birthdays(self, ctx):
        embed = discord.Embed(title='list of birthdays in the guild')
        for member in ctx.guild.members:
            for user in self.users:
                person = self.bot.get_user(int(user))
                if member == person:
                    embed.add_field(name=person.display_name, value=str(self.get_month(user)) + ' '
                                    + str(self.get_day(user)))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BirthdayList(bot))
