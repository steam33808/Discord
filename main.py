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
  number1 = str(random.randint(1,9))
  number2 = str(random.randint(1,9))
  number3 = str(random.randint(1,9))
  number4 = str(random.randint(1,9))

  await ctx.send(number1)
  await ctx.send(number2)
  await ctx.send(number3)
  await ctx.send(number4)
  
  while guess_correct < 4:
    guess_correct=0
    await ctx.send("Please enter your first number")
    guess1 = await bot.wait_for("message", check = check_for_author)#This checks if the number entered was entered by the same person that started the game.
    await ctx.send(number1)
    await ctx.send(guess1.content)
    if guess1.content == number1:
      await ctx.send("you got your first number corect")
      guess_correct= guess_correct + 1
    else:
      await ctx.send("Unfortunatly your first number is incorect   please try your second number")
    await ctx.send("Please enter your seccond number")
    guess2 = await bot.wait_for("message", check = check_for_author)#This checks if the number entered was entered by the same person that started the game.
    if guess2.content == number2:
      await ctx.send("you got your seccond number corect")
      guess_correct= guess_correct + 1
    else:
      await ctx.send("Unfortunatly your seccond number is incorect please try your third number")
  
  
    await ctx.send("Please enter your third number")
    guess3 = await bot.wait_for("message", check = check_for_author)#This checks if the number entered was entered by the same person that started the game.
    if guess3.content == number3:
      await ctx.send("you got your third number corect")
      guess_correct= guess_correct + 1
    else:
      await ctx.send("Unfortunatly your third number is incorect please try your third number")
  
    await ctx.send("Please enter your forth number")
    guess4 = await bot.wait_for("message", check = check_for_author)#This checks if the number entered was entered by the same person that started the game.
    if guess4.content == number4:
      await ctx.send("you got your forth number corect")
      guess_correct= guess_correct + 1
    else:
      await ctx.send("Unfortunatly your forth number is incorect please try again")
  
  if guess_correct == 4:
    await ctx.send("Congrats you guessed all the numbers corectly")
  else:
    ctx.send("Plese try again")
    ctx.send("")
    ctx.send("")
    
    



  





























bot.run(TOKEN)