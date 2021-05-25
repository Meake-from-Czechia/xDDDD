# Imports
import os
import discord

# Settings
token = open("token.txt").readlines()[0].replace("\n", "")
guild = open("guild.txt").readlines()[0].replace("\n", "")

# Other shit
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(token)
