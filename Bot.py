import discord
import random
import praw
import urbandictionary
from discord.ext import commands

prefix = '?'

tokens_file = open('Tokens.txt', 'r')
token = tokens_file.readline().strip()
reddit_secret = tokens_file.readline().strip()
reddit_id = tokens_file.readline().strip()
tokens_file.close()

bot = commands.Bot(command_prefix=prefix, description='Bot of many things')

reddit = praw.Reddit(client_id=reddit_id,
                     client_secret=reddit_secret,
                     user_agent='eagleeye2218')


@bot.event
async def on_ready():
    print('logged in as ', bot.user.name)
    game = discord.Game("?help for commands")
    await bot.change_presence(status=discord.Status.online, activity=game)


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


@bot.command(description='Returns the urban dictionary definition of a word')
async def define(ctx, word_to_define):
    results = urbandictionary.define(str(word_to_define))
    results_definitions = []
    results_examples = []
    for i in results:
        results_definitions.append(i.definition)
        results_examples.append(i.example)
    await ctx.send(results_definitions[0] + '\n' + results_examples[0])


bot.run(token)
