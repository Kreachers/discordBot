import discord
import json

info = json.load(open('./info.json', 'r'))

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as', client.user)

@client.event
async def on_message(message):
    print('Author: ', message.author)
    print('Content: ', message.content, '\n')
    # print('message: \n', message)
    # don't respond to ourselves
    if message.author == client.user:
        return

    if message.content == 'ping':
        await message.channel.send('pong')
    if message.content == 'right':
        await message.delete()
        await message.channel.send('https://media.giphy.com/media/jeXiz1RAvzX44/giphy.gif')
    # if message.channel.nsfw == True:
        # await message.channel.send('https://media.giphy.com/media/UVXGjSQNI88XS/giphy.gif')

client.run(info["token"])

#from discord.ext import commands
#
#bot = commands.Bot(command_prefix='>')
#
#@bot.command()
#async def ping(ctx):
#    await ctx.send('pong')
#
