import discord
import json
from discord.ext import commands

info = json.load(open('./info.json', 'r')) #Loads the bot token from a separate file
bot = commands.Bot(command_prefix='/') #Sets prefix for commands(/Command)


guild = []

# @bot.event
# async def on_connect():
#     print(bot.guild.name, '\n')

@bot.command(name='life')
async def life(ctx):
    await ctx.message.delete()
    await ctx.channel.send('https://media.giphy.com/media/26ufid7HNqbKdT5EA/giphy.gif')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.message.delete()
    await ctx.channel.send('pong')

@bot.command(name='right')
async def right(ctx):
    await ctx.message.delete()
    await ctx.channel.send('https://media.giphy.com/media/jeXiz1RAvzX44/giphy.gif')

@bot.command(name='stop')
async def stop(ctx):
    await ctx.message.delete()
    await ctx.channel.send('https://media.giphy.com/media/UVXGjSQNI88XS/giphy.gif')

@bot.command(name='create')
async def create(ctx, *args):
    helpMessage = """
    ```
    /create - create a discord and channels dependsing on args

    Usage: create *Name* *Mods* *NFSW*

        Name - The name of the main category and channels (Example: factorio makes a factorio-general)
        Mods - Yes/No for if the category needs a Mods Channel
        NFSW - Yes/No for if the category needs an NSFW channel
    ```
"""
    if 'help' in args:
        await ctx.channel.send(helpMessage)
        return
    if not args:
        await ctx.channel.send('Invalid argumnets. Type /create help for more info.')
        return
    if args and not 'help' in args: 
        categoryName = args[0].casefold()
        generalChannel = categoryName + "-general"
        print(categoryName)
        categoryLink = await ctx.guild.create_category(categoryName)
        print(generalChannel)
        await ctx.guild.create_text_channel(generalChannel, category=categoryLink, topic="All things " + categoryName, position=1)
        if args[1]: 
            if args[1].casefold() == 'yes':
                modsChannel = categoryName + "-mods"
                await ctx.guild.create_text_channel(modsChannel, category=categoryLink, topic="All things " + modsChannel, position=2)
                print(modsChannel if modsChannel else "")
        if args[2]: 
            if args[2].casefold() == 'yes':
                nsfwChannel = categoryName + "-nsfw"
                await ctx.guild.create_text_channel(nsfwChannel, category=categoryLink, topic="All things " + nsfwChannel, position=3, nsfw=True)
                print(nsfwChannel if nsfwChannel else "")

@bot.event
async def on_ready():
    guild = bot.guilds
    # print(guild[0].channels)
    # for Item in guild[0].channels: print(Item, sep='/n')
    # custAct = discord.Streaming(name="IT'S ALIVE", url="https://www.twitch.tv/kreachers", twitch_name="kreachers")
    # await bot.change_presence(status=discord.Status.online, activity=custAct)
    game = discord.Game("all alone")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('Logged on as', bot.user)
    
# this function is run when a message is sent
@bot.event
async def on_message(message):
    if message.author.bot == False:
        # print('Author: ', message.author)
        # print('Content: ', message.content, '\n')
        # print('message: \n', message)
        
        if message.content == 'ping':
            await message.channel.send('pong')
    await bot.process_commands(message)

bot.run(info["token"])