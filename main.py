import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from g4f.client import Client

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Bonjour {ctx.author} !")

@bot.command()
async def Hey(ctx):
    await ctx.send(f"hey, are you okay? {ctx.author} !")

@bot.command()
async def bye(ctx):
    await ctx.send(f"Good night {ctx.author} !")

@bot.command()
async def please(ctx, *, message: str):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
    )
    await ctx.send(response.choices[0].message.content)

@bot.command()
async def draw(ctx, *, message: str):
    client = Client()
    response = client.images.generate(
        model="flux",
        prompt=message,
    )
    image_url = response.data[0].url
    await ctx.send({image_url})

@bot.command()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Tu n'as pas dis le mot magique {ctx.author} !")
    else:
        await ctx.send("Commande introuvable")

token = os.getenv("DISCORD_BOT_TOKEN")

bot.run(token)
