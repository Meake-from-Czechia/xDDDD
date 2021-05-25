# Imports
import discord
import random

# Settings
token = open("token.txt").readlines()[0].replace("\n", "")
guild = open("guild.txt").readlines()[0].replace("\n", "")

# Idk copy pasted this

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        response = ("x" + "D" * random.randint(20, 35))
        await message.channel.send(response)

client.run(token)
