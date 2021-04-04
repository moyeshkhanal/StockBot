from discord.ext import commands
import discord
import requests
from finvizfinance.quote import finvizfinance as fin

class StockCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def _getJSON(self, ticker, apiKey):
        endPoint = f"https://api.tdameritrade.com/v1/marketdata/{ticker}/quotes"

        payload = {'apikey': apiKey}
        # Make request
        content = requests.get(url=endPoint, params=payload)
        data = content.json()
        return data

    @commands.command(aliases=["qt", "q", "Q"])
    async def quote(self, ctx, *ticker):

        apiKey = "WA6ETHZS9B54GOVSZ9GDKLAFHNLNUY7I"
        # The QUOTES endpoint

        if len(ticker) >= 1:
            for tickers in ticker:

                tickers = tickers.upper()
                embed = discord.Embed(title=tickers, color=discord.Color.green())

                data = self._getJSON(tickers, apiKey)[tickers]
                totalVol = data["totalVolume"]
                fiftyTwoWkHigh = data["52WkHigh"]


                bidPrice = data["bidPrice"]
                bidSize = data["bidSize"]
                askPrice = data["askPrice"]
                askSize = data["askSize"]

                # stock = fin(tickers)
                # stock.TickerCharts(timeframe="daily", charttype="advanced", out_dir="charts")
                # embed.set_thumbnail(url=("./charts/"+tickers+".jpg"))

                embed.add_field(name="Total Volume", value=totalVol, inline=True)
                embed.add_field(name="52 Week High", value=fiftyTwoWkHigh, inline=False)

                embed.add_field(name="Bid Price", value=bidPrice, inline=True)
                embed.add_field(name="Bid Size", value=bidSize, inline=True)

                embed.add_field(name="Ask Price", value=askPrice, inline=True)
                embed.add_field(name="Ask Size", value=askSize, inline=True)

                if askSize > bidSize:
                    embed.set_footer(text="More sellers than buyers")
                else:
                    embed.set_footer(text="More buyers than sellers")

                print("sending embed")

                await ctx.send(embed=embed)


    # Send the user error if no ticker is found
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please make sure you have all the required arguments. Ex: $quote tickerSymbol")





def setup(bot):
    bot.add_cog(StockCommands(bot))