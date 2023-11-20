import discord
from discord.ext import commands
import sqlite3
import os

token = 'MTE0MzE3NzI1MjA1ODcwNjAyMA.GBhUJO.DkD70S-a3QEeimmSthPj7j_m9DI_mNyjbGLfls'
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.event
async def on_member_join(member):
    await member.send('Welcome')
    for i in bot.get_guild(member.guild.id).channels:
        if i.name == 'основной':
            await bot.get_channel(i.id).send(f'Welcome {member}')
@bot.event
async def on_member_remove(member):
    for i in bot.get_guild(member.guild.id).channels:
        if i.name == 'основной':
            await bot.get_channel(i.id).send(f'Пока, {member}')
@bot.event
async def on_ready():
    print('Готово')

@bot.command()
async def test(ctx):
    await ctx.author.send('Я тут')
@bot.command()
async def info(ctx,arg=None):
    author = ctx.message.author
    if arg == None:
        await ctx.send(f'{author.mention}, введите:\n!info общее\n!info команды')
    elif arg == 'общее':
        await ctx.send(f'{author.mention}, я бот, следящий за порядком в чате')
    elif arg == 'команды':
        await ctx.send(f'{author.mention}, !test - команда, показывающая, находиться ли бот в онлайне')
    else:
        await ctx.send(f'{author.mention}, такой команды не существует')
'''@bot.event
async def on_message(message):
    if 'дела' in message.content.lower():
        await message.channel.send('Хорошо')'''
@bot.command()
async def send(ctx):
    await ctx.author.send('Как день?')

@bot.command()
async def send_member(ctx,member:discord.Member):
    await member.send(f'{member.name}, привет от {ctx.author.name}')
@bot.command()
async def deleter(ctx,amount=100):
    await ctx.channel.purge(limit=amount)
@bot.command()
async def greeting(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{ctx.author.name},Приветствую')








bot.run(token)
