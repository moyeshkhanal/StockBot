from discord.ext import commands
import discord

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_role("Admin")
    @commands.command(aliases=["o", "op", "entry"])
    async def option(self, ctx, *alert):
        if ctx.author.id == 710319553573289987 or ctx.author.id == 682487741958979594:
            embed = discord.Embed(title=alert[0], color=discord.Color.green())
            embed.add_field(name="Strike Price", value=alert[1])
            embed.add_field(name="Expiration", value=alert[2])
            embed.set_footer(text="Make sure to follow 20% stop loss, take profits when happy with profits!")
            channel = self.bot.get_channel(816498810394116106)
            await channel.send("<@&815799102146740265>", embed=embed)
        else:
            await ctx.send("You do not have permission to use this command")

    @commands.has_role("Admin")
    @commands.command(aliases=["s", "sw"])
    async def swing(self, ctx, *alert):
        if ctx.author.id == 710319553573289987 or ctx.author.id == 682487741958979594:
            embed = discord.Embed(title=alert[0], color=discord.Color.green())
            embed.add_field(name="Strike Price", value=alert[1])
            embed.add_field(name="Expiration", value=alert[2])
            embed.set_footer(text="Make sure to follow 20% stop loss, take profits when happy with profits!")
            channel = self.bot.get_channel(826996954902691850)
            await channel.send("<@&815799102146740265>", embed=embed)
        else:
            await ctx.send("You do not have permission to use this command")

    @commands.has_role("Admin")
    @commands.command(aliases=["d", "dt"])
    async def day(self, ctx, *alert):
        if ctx.author.id == 710319553573289987 or ctx.author.id == 682487741958979594:
            embed = discord.Embed(title=alert[0], color=discord.Color.green())
            embed.add_field(name="Strike Price", value=alert[1])
            embed.add_field(name="Expiration", value=alert[2])
            embed.set_footer(text="Make sure to follow 20% stop loss, take profits when happy with profits!")
            channel = self.bot.get_channel(826996797376692234)
            await channel.send("<@&815799102146740265>", embed=embed)
        else:
            await ctx.send("You do not have permission to use this command")

    # Send the user error if no ticker is found
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please make sure you have all the required arguments. Ex: $quote tickerSymbol")

def setup(bot):
    bot.add_cog(Dev(bot))