import discord
import random 
import os

intents = discord.Intents(messages=True)
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
  if client.user.mentioned_in(message):
    await message.reply(file=discord.File(f"images/{image()}"))

def image():
  i = os.listdir('images')
  return random.choice(i)

client.run("")