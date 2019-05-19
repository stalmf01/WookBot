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
    async def define(self, ctx, word_to_define):
        results = urbandictionary.define(str(word_to_define))
        results_definitions = []
        results_examples = []
        for i in results:
            results_definitions.append(i.definition)
            results_examples.append(i.example)
        await ctx.send(results_definitions[0] + '\n' + results_examples[0])


def setup(bot):
    bot.add_cog(Roast(bot))