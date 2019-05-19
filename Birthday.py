from discord.ext import commands
from datetime import datetime
import asyncio
import discord


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
                user = words[0]
                month = words[1]
                day = words[2]
                self.birthday_days[user] = day
                self.birthday_months[user] = month
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
        if author not in self.users:
            self.users.append(author)
            self.birthday_days[author] = day
            self.birthday_months[author] = month
            with open('Birthdays.txt', 'a') as birthday:
                birthday.write('\n' + author + ' ' + month + ' ' + day)
            await ctx.send('you have been added to the birthday list')
        else:
            await ctx.send('you are already on the birthday list')

    @commands.command()
    async def get_birthday(self, ctx):
        author = str(ctx.message.author.id)
        if author in self.users:
            await ctx.send('your birthday is on ' + self.birthday_months[author] + ' '
                           + self.birthday_days[author])
        else:
            await ctx.send('your birthday is not on the list type ?addbirthday month day to add you birthday')

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
