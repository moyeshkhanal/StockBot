from discord.ext import commands
import discord
import requests
import os
from finvizfinance.quote import finvizfinance as fin

class Cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["cmd"])
    async def cmds(self, ctx):
        embed = discord.Embed(title="Help", color=discord.Color.red())

        fieldList = []
        with open("help.txt") as file:
            for line in file:
                embedDict = {}
                line = line.strip()
                cmd, value = line.split(":")
                embedDict["name"] = cmd
                embedDict["value"] = value
                fieldList.append(embedDict)

        await ctx.send(embed=embed)


    # Send the user error if no ticker is found
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please make sure you have all the required arguments. Ex: $quote tickerSymbol")





def setup(bot):
    bot.add_cog(Cmds(bot))