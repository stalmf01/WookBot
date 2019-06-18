from discord.ext import commands
import urbandictionary
import random


class Roast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Roasts the epic store')
    async def epicroast(self, ctx):
        roast_word = urbandictionary.random()
        words = []
        for i in roast_word:
            words.append(i.word)
        await ctx.send('The epic store can ' + random.choice(words) + ' mah ' + random.choice(words))

    @commands.command(description='Returns the urban dictionary definition of a word')
    async def define(self, ctx):

        parsed_words = ctx.message.content.partition(' ')
        split_words = parsed_words[2].split(' ')
        number = split_words[len(split_words) - 1]

        if number == '1' or number == '2' or number == '3':
            index = int(number)
        else:
            index = 1

        results = urbandictionary.define(str(parsed_words[2]))
        results_definitions = []
        results_examples = []
        for i in results:
            results_definitions.append(i.definition)
            results_examples.append(i.example)
        if index >= len(results_definitions) or index < 1:
            index = 1
        await ctx.send(results_definitions[index-1] + '\n' + results_examples[index-1])


def setup(bot):
    bot.add_cog(Roast(bot))
