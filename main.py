import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We are logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if "help" in message.content:
    await message.channel.send("How can I help you?")

client.run(os.getenv('token'))