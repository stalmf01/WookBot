import discord
from discord.ext import commands


with open('Tokens.txt', 'r') as tokens_file:
    token = tokens_file.readline().strip()
    next(tokens_file)
    next(tokens_file)
    prefix = tokens_file.readline().strip()

bot = commands.Bot(command_prefix=prefix, description='Bot of many things')

# extensions = ['Birthday']
extensions = ['Spoils']
# extensions = ['Birthday', 'EpicRoast', 'Subs']
for extension in extensions:
    bot.load_extension(extension)


@bot.event
async def on_ready():
    print('logged in as ', bot.user.name)
    game = discord.Game("?help for commands")
    await bot.change_presence(status=discord.Status.online, activity=game)


# @bot.event
# async def on_message(ctx):
#     if ctx.author == bot.user:
#         return
#     await bot.process_commands(ctx)
#     # await ctx.channel.send('pong')


# @bot.command(name='ping', help='test if the bot is alive')
# async def ping_pong(ctx):
#     ctx.send('pong')

bot.run(token)
