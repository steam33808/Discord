import discord, random
from discord.ext import commands
import os

TOKEN = os.environ['Token']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents = intents)
guess_correct = 0

number1 = random.randint(1,9)
number2 = random.randint(1,9)
number3 = random.randint(1,9)
number4 = random.randint(1,9)
print(number1, number2, number3, number4)
while guess_correct < 4:
  guess_correct=0
  guess1 = int(input("Please enter your first number"))
  if guess1 == number1:
    print("you got your first number corect")
    guess_correct= guess_correct + 1
  else:
    print("Unfortunatly your first number is incorect   please try your second number")


  guess2 = int(input("Please enter your seccond number"))
  if guess2 == number2:
    print("you got your first number corect")
    guess_correct= guess_correct + 1
  else:
    print("Unfortunatly your seccond number is incorect please try your third number")


  guess3 = int(input("Please enter your third number"))
  if guess3 == number3:
    print("you got your first number corect")
    guess_correct= guess_correct + 1
  else:
    print("Unfortunatly your third number is incorect please try your third number")

  guess4 = int(input("Please enter your forth number"))
  if guess4 == number4:
    print("you got your first number corect")
    guess_correct= guess_correct + 1
  else:
    print("Unfortunatly your forth number is incorect please try again next time")

if guess_correct == 4:
  print("Congrats you guessed corectly")
else:
  print("Plese try again")
  print("")
  print("")
    
    



  






  """
  yes = "yes"
  guess1 = 0
  guess2 = 0
  guess3 = 0
  guess4 = 0
  number1 = random.randint(1,9)
  number2 = random.randint(1,9)
  number3 = random.randint(1,9)
  number4 = random.randint(1,9)
    ctx.channel.send("You need to guees 4 numbers in     order, press enter after each number")
  guess1 = int(input(""))
  guess2 = int(input(""))
  guess3 = int(input(""))
  guess4 = int(input(""))
  for i in range(int(num)):
      ctx.channel.send(number1)




@bot.command (name="number")
async def number(ctx,num):
  for i in range(int(num)):
    number1 = random.randint(1,9)
    ctx.channel.send(number1)
    await ctx.channel.send(number1)

"""




























bot.run(TOKEN)