#scans every message in a server for a word that ends with 'er'
#replies with "I hardly know here" a la the office
import discord 
import os
import random 

import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    usmess = str(message.content)
    strlen = len(usmess) - 1
    er = "er"
  
    words = usmess.split(" ")
    lenwords = int(len(words))
    print(words)

    for x in range(lenwords):
      if er in words[x]: 
        if x == (lenwords - 1):
          if words[x].endswith(er):
            await message.reply(words[x])
            await message.channel.send("I hardly know her!")

async def on_message(message):
    if message.author == client.user:
      return
  usmess = str(message.content)
  if usmess.find()	

    

client.run(os.getenv('token'))
