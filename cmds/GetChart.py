from discord.ext import commands
import discord
import requests
import os
from finvizfinance.quote import finvizfinance as fin

class GetChart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def _getChart(self, ticker, tf):
        stock = fin(ticker)
        stock.TickerCharts(timeframe=tf, charttype="advanced", out_dir="charts")

    @commands.command(aliases=["cw", "cd", "cm", "daily", "weekly", "monthly"])
    async def chartWeekly(self, ctx, *ticker):
        cmd = ctx.invoked_with
        if cmd in ["cw", "weekly"]:
            for tickers in ticker:
                self._getChart(tickers, "weekly")
                await ctx.send(file=discord.File("charts/" + str(tickers) + ".jpg"))
                os.remove("charts/" + str(tickers) + ".jpg")
        elif cmd in ["cd", "daily", "chart"]:
            for tickers in ticker:
                self._getChart(tickers, "daily")
                await ctx.send(file=discord.File("charts/" + str(tickers) + ".jpg"))
                os.remove("charts/" + str(tickers) + ".jpg")
        elif cmd in ["cm", "monthly"]:
            for tickers in ticker:
                self._getChart(tickers, "monthly")
                await ctx.send(file=discord.File("charts/" + str(tickers) + ".jpg"))
                os.remove("charts/" + str(tickers) + ".jpg")

    # Send the user error if no ticker is found
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please make sure you have all the required arguments. Ex: $quote tickerSymbol")





def setup(bot):
    bot.add_cog(GetChart(bot))