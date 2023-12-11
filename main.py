import discord
from discord.ext import commands
import random

description = "Bot of memes"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(name='meme')
async def mem(ctx):
    imagen = str(random.randint(1, 3))
    with open("images/" + imagen + ".jpg", 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    print("Sended ", imagen)


bot.run("Token")
