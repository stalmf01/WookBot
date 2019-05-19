from discord.ext import commands
import praw


class RedditSubs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('Tokens.txt', 'r') as tokens_file:
            token = tokens_file.readline().strip()
            reddit_secret = tokens_file.readline().strip()
            reddit_id = tokens_file.readline().strip()
        self.reddit = praw.Reddit(client_id=reddit_id, client_secret=reddit_secret, user_agent='eagleeye2218')

    @commands.command(description='Returns top post from a random sub', aliases=['randomsub'])
    async def randsub(self, ctx):
        subreddit = self.reddit.subreddit('random')
        for submission in subreddit.top(limit=1):
            await ctx.send('subreddit   ' + subreddit.url + '\n' + submission.title + '\n' + submission.url)

    @commands.command(description='Returns the top post on a specified sub')
    async def topsub(self, ctx, sub):
        subreddit = self.reddit.subreddit(sub)
        for submission in subreddit.top(limit=1):
            await ctx.send('subreddit   ' + subreddit.url + '\n' + submission.title + '\n' + submission.url)


def setup(bot):
    bot.add_cog(RedditSubs(bot))
