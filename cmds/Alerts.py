from discord.ext import commands
import discord

class Alerts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_role("Admin")
    @commands.command(aliases=[ "a"])
    async def alerts(self, ctx, *support):
        embed = discord.Embed(title=support[0], color=discord.Color.green())
        print(support[0])
        for i in range(1, len(support), 1):
            title, price = support[i].split(":")
            embed.add_field(name=title, value=price)
        channel = self.bot.get_channel(826997532504490014)
        await channel.send(embed=embed)

    # Send the user error if no ticker is found
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please make sure you have all the required arguments. Ex: $quote tickerSymbol")

def setup(bot):
    bot.add_cog(Alerts(bot))