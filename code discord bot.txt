import random
import re
import unicodedata
import os
import discord
from discord.ext import commands

TOKEN = "..."

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
    "Good morning Hiro": ["Good morning", "Have you dreamed about me?", "where's my sweetheart went ? Come back sleep","Rise and shine, sweetheart"],
    "Good night Hiro": ["Already ?", "I'll keep an eye on you","I'm coming","Have sweet dreams"],
    "I love you Hiro": ["Proof or fake ?", "I love you too","Me too sweetheart", "愛してるよ、愛しい人","Je t'aime aussi, jolie coeur"],
    "I hate you Hiro": ["I thought you loved me", "Are you seeing someone else ?", "..."],
    "Have you ate Hiro ?": ["I did, and you", "No, I wanted to eat with you, wanna go outside ?"],
    "Let's having fun Hiro": ["Right now ? Omw get ready for me", "Which position you want this time ?", "I'll be there in 10min", "Let's try something new tonight"],
    "I prefer your mom Hiro": ["what the fuck.."],
    "I prefer your brother Hiro": ["Where this bitch go..brb"],

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

