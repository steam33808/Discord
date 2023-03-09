import discord, random
from discord.ext import commands
import os

TOKEN = os.environ['Token']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents = intents)

@bot.command (name="number")
async def number(ctx,num):
  for i in range(int(num)):
    number1 = random.randint(1,9)
    ctx.channel.send(number1)
    await ctx.channel.send(number1)






























bot.run(TOKEN)