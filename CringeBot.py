#replies to a particular user's message with a random quote messing with them
import discord
import os
import random
import urllib.request
from PIL import Image
import requests 
from bs4 import BeautifulSoup

from urllib.request import urlopen

import re


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#cringe bot
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #can adjust message and user 
    if str(message.author) == "Message Author Username":
      cringe_selecter = random.randrange(1, 5)
      if (cringe_selecter == 1):
          await message.reply('Bruh thats cringe')
      elif (cringe_selecter == 2):
          await message.reply('U must be this tall to post shit like that')
      elif (cringe_selecter == 3):
        await message.reply('Okay, but did we ask??')
      else:
          await message.reply('Ugh Im a BOT and I think that was cringe')
      
      await message.reply('Pardon?')


client.run(os.getenv('TOKEN'))
