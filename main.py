import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Bonjour {ctx.author} !")

@bot.command()
async def hey(ctx):
    await ctx.send(f"hey, are you okay? {ctx.author} !")

@bot.command()
async def bye(ctx):
    await ctx.send(f"Good night {ctx.author} !")

token = os.getenv("DISCORD_BOT_TOKEN")

bot.run(token)