import discord, random
from discord.ext import commands
import os

TOKEN = os.environ['Token']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents = intents)
guess_correct = 0


@bot.command(name = "start_game")
async def start_game(ctx,num):

  global guess_correct
  guess_correct = 0
  number1 = random.randint(1,9)
  number2 = random.randint(1,9)
  number3 = random.randint(1,9)
  number4 = random.randint(1,9)

  while guess_correct < 4:
    guess_correct=0
    ctx.send("Please enter your first number")
    guess1 = int(input(""))
    if guess1 == number1:
      ctx.send("you got your first number corect")
      guess_correct= guess_correct + 1
    else:
      ctx.send("Unfortunatly your first number is incorect   please try your second number")
  
  
    guess2 = int(input("Please enter your seccond number"))
    if guess2 == number2:
      ctx.send("you got your first number corect")
      guess_correct= guess_correct + 1
    else:
      ctx.send("Unfortunatly your seccond number is incorect please try your third number")
  
  
    guess3 = int(input("Please enter your third number"))
    if guess3 == number3:
      ctx.send("you got your first number corect")
      guess_correct= guess_correct + 1
    else:
      ctx.send("Unfortunatly your third number is incorect please try your third number")
  
    guess4 = int(input("Please enter your forth number"))
    if guess4 == number4:
      ctx.send("you got your first number corect")
      guess_correct= guess_correct + 1
    else:
      ctx.send("Unfortunatly your forth number is incorect please try again next time")
  
  if guess_correct == 4:
    ctx.send("Congrats you guessed corectly")
  else:
    ctx.send("Plese try again")
    ctx.send("")
    ctx.send("")
    
    



  





























bot.run(TOKEN)