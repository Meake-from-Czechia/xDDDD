# Imports
import os
import discord

# Settings
token = open("token.txt").readlines()[0].replace("\n", "")
guild = open("guild.txt").readlines()[0].replace("\n", "")

# Idk copy pasted this

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()


client.run(token)
