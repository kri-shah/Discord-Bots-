#when -joke command is given, gets a random joke from url
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

    if message.content.startswith('-joke'):
      url = "https://bestlifeonline.com/dirty-jokes/"
      html = urlopen(url).read()
      soup = BeautifulSoup(html, features="html.parser")

      # kill all script and style elements
      for script in soup(["script", "style"]):
        script.extract()    # rip it out

      # get text
      text = soup.get_text()

      # break into lines and remove leading and trailing space on each
      lines = (line.strip() for line in text.splitlines())
      # break multi-headlines into a line each
      chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
      # drop blank lines
      text = '\n'.join(chunk for chunk in chunks if chunk)
      joke = text.split("\n")

      del joke[0 : 25] 
      del joke[70 : 126]

      jokeselecter = random.randrange(0, 70)
      await message.channel.send(joke[jokeselecter]) 

async def on_message(message):
    if message.author == client.user:
      return
  usmess = str(message.content)
  if usmess.find()	



client.run(os.getenv('token'))
