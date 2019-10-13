import discord
from discord.ext import commands


with open('Tokens.txt', 'r') as tokens_file:
    token = tokens_file.readline().strip()
    next(tokens_file)
    next(tokens_file)
    prefix = tokens_file.readline().strip()

bot = commands.Bot(command_prefix=prefix, description='Bot of many things')

extensions = ['ElviraBot', 'Birthday', 'EpicRoast', 'Subs']
# extensions = ['ElviraBot', 'Birthday', 'EpicRoast', 'Subs', 'Spoils']
for extension in extensions:
    bot.load_extension(extension)


@bot.event
async def on_ready():
    print('logged in as ', bot.user.name)
    game = discord.Game("?help for commands")
    await bot.change_presence(status=discord.Status.online, activity=game)

bot.run(token)
