import random
import re
import unicodedata
import os
import discord
from discord.ext import commands

TOKEN = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix ="!", intents=intents)

def normaliser(s: str) -> str:
    s = s.lower().strip()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")  # enlève accents
    s = re.sub(r"[^a-z0-9\s]", "", s)  # enlève ponctuation
    s = re.sub(r"\s+", " ", s)         # espaces multiples -> 1 espace
    return s

PROMPTS = {
    "Good morning Eden": ["Gm", "'Sup", "Move your ass and make me a coffee"],
    "Good night Eden": ["Gn", "Don't dream about me","I'm coming"],
    "I love you Eden": ["I love myself too", "Who ?", "..me too.."],
    "I hate you Eden": ["I hate you too", "cool", "lol"],
    "Have you ate Eden ?": ["Yes", "Did you ? Nvm I don't care"],
    "Let's having fun Eden": ["||Don't say it twice||", "||Get on your knees, open your mouth and close your eyes||", "||No||", "||Ask someone else||", "||Let's make it in Hiro room||"],
    "I prefer your mom Eden": ["i know right", "I do too"],
    "I prefer your brother Eden": ["This man have too much fan", "Liar"],
}

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    texte = normaliser(message.content)

    for key, reponses in PROMPTS.items():
        if texte == normaliser(key):
            await message.channel.send(random.choice(reponses))
            return

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await bot.process_commands(message)

bot.run(TOKEN)

