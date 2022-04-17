import discord
import os

client = discord.Client()


@client.event
async def on_ready():
  print('We are logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
  async def adminquery():
    await message.channel.send("Congratulations you have reached Admin query portal. Here are a list of FAQs that might be similar to your question\n")
    await message.channel.send("$1a Am I eligible to join AccioJob \n$1b What's the minimum educational qualification to join the course? \n$1c When will I get joining details of my Batch? "
    )
    
  if message.author == client.user:
    return
  
  if "help" in message.content:
    await message.channel.send("How can I help you?\n$1 - Admin query\n$2 - course query\n$3 - Interview based query\n$4 - Coding Query" )
    
  if "$1"==message.content:
    await adminquery()
    
  if "$1a"==message.content:
    await message.channel.send("answer for 1a")

  if "$1b"==message.content:
    await message.channel.send("answer for 1b")

  if "$2"==message.content:
    await coursequery()

  if "$3"==message.content:
    await interviewquery()

  if "$4"==message.content:
    await message.channel.send("Your question will be resolved shortly by a human. Stay tuned!")

client.run(os.getenv('token'))