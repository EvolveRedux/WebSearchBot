# Code made and developed by EvolveRedux. I am not responsible for any misuse of this bot or the code so use it at your own risk.
# You will need to register a ApiFlash account here and enter the key in the SEARCH_KEY variable. You can register here: https://apiflash.com
# You also will need a Discord bot token which you can get here: https://discord.com/developers. Once you have set up a bot account paste the token in the token variable.
import discord
import requests
from discord import Game
from discord.ext.commands import Bot
from urllib.parse import urlencode
from urllib.request import urlretrieve


TOKEN = ‘insert bot token here’
SEARCH_KEY = ‘insert ApiFlash token here'

client = discord.Client()
    
@client.event


async def on_message(message):

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('=help'):
        embed = discord.Embed(title="Commands:", description="These are the commands for WebSearchBot.", color=0x00ff00)
        embed.add_field(name="=google", value="Type in your search query after this, and it will generate a link to a Google page with your search query and a screenshot of the image.", inline=False)
        embed.add_field(name="=youtube", value="Type in your YouTube search query and it generates a link to a YouTube page with your search query and a screenshot of the page.", inline=False)
        embed.add_field(name="=image", value="Type in a search query for an image and the bot will take a screenshot of the desired webpage and send a photo with the images.", inline=False)
        embed.add_field(name="=web", value="Takes a screenshot of the desired webpage, e.g =web example.com", inline=False)
        
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('=google'):
               
                msg = message.content
                msg = msg.replace('=google', '')
                msg = msg.replace(' ', '+')
                google = "https://www.google.com/search?q=varo"
                google = google.replace('varo', msg)
                if msg == '':
                    google = "You need to type in something after =google!"
                

                params = urlencode(dict(access_key=SEARCH_KEY,
                        url=google))
                urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.jpeg")
                await client.send_file(message.channel, "screenshot.jpeg", filename="screenshot.jpeg")

                await client.send_message(message.channel, google)
    if message.content.startswith('=youtube'):
                
                msg = message.content
                msg = msg.replace('=youtube', '')
                msg = msg.replace(' ', '+')
                youtube = "https://www.youtube.com/results?search_query=jkj"
                if msg == '':
                    youtube = "You need to type in something after =youtube!"
                 

                youtube = youtube.replace('jkj', msg)
                params = urlencode(dict(access_key=SEARCH_KEY,
                        url=youtube))
                urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.jpeg")
                await client.send_file(message.channel, "screenshot.jpeg", filename="screenshot.jpeg")


                await client.send_message(message.channel, youtube)
    
    if message.content.startswith('=image'):
                msg = message.content
                msg = msg.replace('=image', '')
                msg = msg.replace(' ', '+')
                image = "https://www.google.com/search?hl=en&tbm=isch&source=hp&biw=1440&bih=821&ei=KlbjXr_pJaiO4-EPoeys6AE&q=varo&oq=varo&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BQgAELEDUOZkWLGSAWDblAFoBnAAeACAAYwDiAG8E5IBBzAuMS44LjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAA&sclient=img&ved=0ahUKEwi_pq-MhvzpAhUoxzgGHSE2Cx0Q4dUDCAc&uact=5"
                if msg == '':
                    image = "You need to type in something after =image!"
                 

                image = image.replace('varo', msg)
                params = urlencode(dict(access_key=SEARCH_KEY,
                        url=image))
                urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.jpeg")
                await client.send_file(message.channel, "screenshot.jpeg", filename="screenshot.jpeg")
                await client.send_message(message.channel, image)
    if message.content.startswith('=web'):
                msg = message.content
                msg = msg.replace('=web', '')
                msg = msg.replace(' ', '')
                msg = "https://" + msg
                params = urlencode(dict(access_key=SEARCH_KEY,
                        url=msg))
                urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.jpeg")
                await client.send_file(message.channel, "screenshot.jpeg", filename="screenshot.jpeg")
                
                




@client.event
async def on_ready():
    await client.change_presence(game=Game(name="=help"))
    print("Bot successfully logged in as " + client.user.name)

client.run(TOKEN)

