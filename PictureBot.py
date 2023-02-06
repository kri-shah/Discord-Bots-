@client.event
#replies to a particular user's message message with a picture pulled from a website (adjustable - I used pintrest)

async def on_message(message):
    if message.author == client.user:
        return
    
    if str(message.author) == "Pabst Blue Ribbon on Ice#8906":
      html = urlopen('#picture/website link')
      bs = BeautifulSoup(html, 'html.parser')
      images = bs.find_all('img', {'src':re.compile('.jpg')})
      
      size = len(images) - 1
      ran = random.randint(0, size)
      
      string = str (images[ran])
      chunks = string.split('"')
      #print(chunks) 
      
      strsize = len(chunks) - 1

      test = "https"
      for y in range(strsize):
        if test in chunks[y]:
          url = chunks[y] 
          break
      

      #print(images[ran])

      await message.channel.send(url)
