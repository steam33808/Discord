import discord, random
from discord.ext import commands
import os

TOKEN = os.environ['Token']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents = intents)
guess_correct = 0


@bot.command(name = "startgame")
async def start_game(ctx):
  
  def check_for_author(m):
    return ctx.author == m.author
  
  global guess_correct
  guess_correct = 0
  number1 = random.randint(1,9)
  number2 = random.randint(1,9)
  number3 = random.randint(1,9)
  number4 = random.randint(1,9)

  while guess_correct < 4:
    guess_correct=0
    await ctx.send("Please enter your first number")
    guess1 = await bot.wait_for("message", check = check_for_author)#This checks if the number entered was entered by the same person that started the game.
    if guess1 == number1:
      await ctx.send("you got your first number corect")
      guess_correct= guess_correct + 1
    else:
      await ctx.send("Unfortunatly your first number is incorect   please try your second number")
  
    await ctx.send("Please enter your seccond number")
    guess2 = await bot.wait_for("message", check = check_for_author)#This checks if the number entered was entered by the same person that started the game.
    if guess2 == number2:
      await ctx.send("you got your forth number corect")
      guess_correct= guess_correct + 1
    else:
      await ctx.send("Unfortunatly your seccond number is incorect please try your third number")
  
  
    await ctx.send("Please enter your third number")
    guess3 = await bot.wait_for("message", check = check_for_author)#This checks if the number entered was entered by the same person that started the game.
    if guess3 == number3:
      await ctx.send("you got your forth number corect")
      guess_correct= guess_correct + 1
    else:
      await ctx.send("Unfortunatly your seccond number is incorect please try your third number")
  
    await ctx.send("Please enter your forth number")
    guess4 = await bot.wait_for("message", check = check_for_author)#This checks if the number entered was entered by the same person that started the game.
    if guess4 == number4:
      await ctx.send("you got your forth number corect")
      guess_correct= guess_correct + 1
    else:
      await ctx.send("Unfortunatly your forth number is incorect please try again")
  
  if guess_correct == 4:
    ctx.send("Congrats you guessed corectly")
  else:
    ctx.send("Plese try again")
    ctx.send("")
    ctx.send("")
    
    



  





























bot.run(TOKEN)