import discord
import random
import praw
import urbandictionary
from discord.ext import commands

prefix = '?'
bot = commands.Bot(command_prefix=prefix, description='Bot of many things')
reddit = praw.Reddit(client_id='Q8zRcB6y_nbgjQ',
                     client_secret='ub1hAuKYdTLqd1m37BffCuu_BSk',
                     user_agent='eagleeye2218')

# token for test bot
# token = 'NTc2NDM3MDYyNTA1NTk0ODgw.XNWfNQ.bpZrmbUO3ZkFluq69yGVH9uO4bk'
# token for live bot
token = 'NTc2MDgwMjQxOTY2MTg2NDk2.XNZGlA.tFYULqIRGB1JXCcN1ut4w8wQtwY'


@bot.event
async def on_ready():
    print('logged in as ', bot.user.name)
    game = discord.Game("?help for commands")
    await bot.change_presence(status=discord.Status.online, activity=game)

"""
@bot.command(description='Mocks everyone')
async def mock(ctx):
    if self.mock:
        self.mock = 0
        await ctx.send('Mocking disabled')
    elif not self.mock:
        self.mock = 1
        print(mock)
        await ctx.send('Mocking enabled')


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif self.mock and not message.content.startswith(prefix):
        count = 0
        sent_message = ''
        mock_message = str(message.content)
        for i in mock_message:
            if i.isspace():
                sent_message += i
            elif count % 2 == 0:
                sent_message += i.upper()
            else:
                sent_message += i.lower()
            count += 1
        await message.channel.send(sent_message)
    else:
        return
"""

@bot.command(description='Returns top post from a random sub',
             aliases=['randomsub'])
async def randsub(ctx):
    subreddit = reddit.subreddit('random')
    for submission in subreddit.top(limit=1):
        await ctx.send('subreddit   ' + subreddit.url + '\n' + submission.title + '\n' + submission.url)


@bot.command(description='Roasts the epic store')
async def epicroast(ctx):
    roast_word = urbandictionary.random()
    words = []
    for i in roast_word:
        words.append(i.word)
    await ctx.send('The epic store can ' + random.choice(words) + ' mah ' + random.choice(words))


@bot.command(description='Returns the top post on a specified sub')
async def topsub(ctx, sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.top(limit=1):
        await ctx.send('subreddit   ' + subreddit.url + '\n' + submission.title + '\n' + submission.url)

"""""
@bot.command(description='Returns the urban dictionary definition of a word')
async def meaning(ctx, word_to_define):
    print('hello ', word_to_define)
    await ctx.send('Implementation coming soon')
"""

bot.run(token)
