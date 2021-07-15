import discord
from discord.ext import commands
import config
intents = discord.Intents.default()
intents.members = True
import random

import time

client = commands.Bot(command_prefix='bruh', intents=intents)

@client.event
async def on_ready():
    
    print('it works, for now')

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server called {member.guild}.")

@client.event
async def on_member_remove(member):
    print(f"{member} has unjoined a server called {member.guild}.")

@client.event
async def on_command_error(ctx, error):
    await ctx.send('error')


@client.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')
# def do():
#     await schedule.every(10).seconds.do(ping)


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

@client.command(aliases=['8balls'])

async def _8ball(ctx, *, question):
    responses =['yes', 'no', 'maybe so']
   
    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}')
    
      
@client.command()
async def byenigga(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
@client.command()
async def cyanigga(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


words = ['this', 'is', 'words']
@client.command()
async def printwords(ctx):
    for i in words:
        await ctx.send(i)

@client.command()
async def xkcd(ctx, arg="def"):
    if arg == "random":
        await ctx.send("https://c.xkcd.com/random/comic/")
    elif arg == "def":
        await ctx.send("https://xkcd.com")
    else:
        await ctx.send(f"https://xkcd.com/{arg}")
    

@client.command()
async def test(ctx, arg):
    if arg == "yay":
        await ctx.send(arg)
    else:
        await ctx.send('nigga')

@client.command()
async def channel(ctx, name):
    await ctx.guild.create_text_channel(name, category="text-channels")

@client.command()
async def lista(ctx):
    await ctx.send(ctx.guild.name)

# @client.command()
# async def spot(ctx):
#     await ctx.send(ctx.BaseActivity.created_at)
@client.command()
async def timey(ctx):
   discord.ClientUser.created_at



    
    

client.run(config.TOKEN)