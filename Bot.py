import discord
import random
import praw
import urbandictionary


token = 'NTc2MDgwMjQxOTY2MTg2NDk2.XNRdwg.DRJJrW5XGFpmbwZjvllUNCKOOdM'
reddit = praw.Reddit(client_id='Q8zRcB6y_nbgjQ',
                     client_secret='ub1hAuKYdTLqd1m37BffCuu_BSk',
                     user_agent='eagleeye2218')


class MyClient(discord.Client):
    mock = 0
    sent_message = ''

    async def on_ready(self):
        print('Logged on as', self.user)
        game = discord.Game("Bot Things")
        await client.change_presence(status=discord.Status.idle, activity=game)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == 'epicroast':
            roast_word = urbandictionary.random()
            words = []
            for i in roast_word:
                words.append(i.word)
            await message.channel.send('The epic store can ' + random.choice(words) + ' mah ' + random.choice(words))

        elif message.content == 'mockon':
            self.mock = 1
        elif message.content == 'mockoff':
            self.mock = 0

        elif self.mock:

            count = 0
            mock_message = str(message.content)
            for i in mock_message:
                if i.isspace():
                    self.sent_message += i
                elif count % 2 == 0:
                    self.sent_message += i.upper()
                else:
                    self.sent_message += i.lower()
                count += 1
            await message.delete()
            await message.channel.send(str(message.author) + " says, " + self.sent_message)
            self.sent_message = ''

        elif message.content == 'randsub':
            subreddit = reddit.subreddit('random')
            for submission in subreddit.hot(limit=1):
                await message.channel.send('subreddit   ' + subreddit.url + '\n' + submission.title + '\n' + submission.url)

        elif message.content == 'helpbot':
            embed = discord.Embed(title="WookBot", description="A bot of many things. List of commands are:",
                                  color=0xeee657)
            embed.add_field(name="epicroast", value="Roasts the epic store", inline=False)
            embed.add_field(name="mockon", value="Makes everything degenerate", inline=False)
            embed.add_field(name="mockoff", value="Saves everyone from the degeneracy", inline=False)
            #embed.add_field(name="cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
            embed.add_field(name="randsub", value="Displays a random post from reddit", inline=False)
            embed.add_field(name="helpbot", value="Gives this message", inline=False)
            await message.channel.send(embed=embed)


client = MyClient()
client.run(token)
