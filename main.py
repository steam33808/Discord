import discord, random
from discord.ext import commands
import os

TOKEN = os.environ['Token']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents = intents)



































bot.run(TOKEN)