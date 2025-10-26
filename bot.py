# Imports
import discord
import random

# Settings
token = open("token.txt").readlines()[0].replace("\n", "")
guild = open("guild.txt").readlines()[0].replace("\n", "")

# Idk copy pasted this

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
        response = ("x" + "D" * random.randint(20, 35))
        await message.channel.send(response)

client.run(token)
