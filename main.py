import discord # type: ignore


intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bejelentkezve mint {client.user}')

@client.event
async def on_message(message):
 
    if message.author == client.user:
        return

 
    await message.channel.send('Szia! Én a KanosBot vagyok! Használd a kulcsszavaimat a bővebb beszélgetésekhez!')

async def on_message(message):
    if message.author == client.user:
        return

   
    if "ovszer" in message.content.lower():
        await message.channel.send('Az ovszer fontos az szexhez, ha nem akarsz kideket :D')

    if "ovszer2" in message.content.lower():
        await message.channel.send("200 ft a temun az ovszer")

    if "porn" in message.content.lower():
        await message.channel.send("A porno nem tesz jót az egészségedre! A legtöbb fiatal a pornot, maszturbáció (önkielégítés) segéd eszköznek is használják!")
    
    if "help" in message.content.lower():
        await message.channel.send("Kulcsszavaim: ovszer, ovszer2, porn, erreverd, help")

    if "help" in message.content.lower():
        await message.channel.send("Kulcsszavaim: ovszer, ovszer2, porn, erreverd, help")

    if "fasz" or "verem"  in message.content.lower():
        await message.channel.send("haha! szexi csajokra kell faszt veri ")

    if "geci" in message.content.lower():
       await message.channel.send("Kulcsszavaim: ovszer, ovszer2, porn, erreverd, help")


    if "geci " or "sperma" or "erreverd" in message.content.lower == "erreverd":
        imageurl = "erreverd.png"
        await message.send(imageurl)

        if "/setchannel" in message.content.lower():
            await message.channel.send("Csatorna kiválasztva! Kezdjünk el beszélgetni ott!")
    









client.run('MTI4NDk2MTQ4NTI1MjIwMjcxNw.GCl-IY.fWiSxvsEUWv4482hJohAFcS27noZsdrx-tePXc')
