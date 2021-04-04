from discord.ext import commands
import discord
import requests
import os
from finvizfinance.quote import finvizfinance as fin

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["on"])
    async def online(self, ctx, *ticker):
        await ctx.send("Bot is live on the server")
    # Send the user error if no ticker is found
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please make sure you have all the required arguments. Ex: $quote tickerSymbol")





def setup(bot):
    bot.add_cog(Help(bot))