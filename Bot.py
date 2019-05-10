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
            choices = ['The epic store can chordle mah ball sack',
                       'The epic store can lick mah taint',
                       'The epic store can slob on mah knob',
                       'The epic store can die in a fire']
            roast = random.choice(choices)
            await message.channel.send(roast)

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



client = MyClient()
client.run(token)
