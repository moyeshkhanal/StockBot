import discord
from discord.ext import commands
import os

with open('token.txt') as file:
    token = file.readline()

# Client prefix 
client = commands.Bot(command_prefix = "$")

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        client.load_extension(f'cmds.{filename[:-3]}')


# client.load_extension('cmds.Quotes')
client.run(token)