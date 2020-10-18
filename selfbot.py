import asyncio
import discord
from discord.ext import commands

token = 'put_token_here'

client = discord.Client()
client = commands.Bot(command_prefix='$', case_insensitive=True, self_bot=True)

presence_set = False

@client.event
async def on_connect():
    await asyncio.sleep(5)
    print('selfbot is ready')
    if not presence_set:
        global presence_set
        await client.change_presence(status='invisible', afk=True)
        presence_set = True

"""
ping -> pong
"""
@client.command()
async def ping(ctx):
    await ctx.message.edit(content='pong')

"""
clears your messages
"""
@client.command()
async def clear(ctx):
    async for message in channel.history(limit=None).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass

"""
sets the selfbot instance presence to invisible & afk so that
when you close the client you go invisible and receive push notifications on mobile etc
"""
async def presence(client):
    await asyncio.sleep(10)
    await client.change_presence(status=invisible, afk=True)

client.run(token, bot=False)
