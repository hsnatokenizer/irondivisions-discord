import discord
from discord.ext import commands

# from discord.utils
# from datetime import datetime
# import time
# import math
# import random
# import re
# import string

initial_extensions = ['cogs.util']
                     # 'cogs.tour',
                     # 'cogs.mod']

token = "UH OH"

client = commands.Bot(command_prefix=">", case_insensitive=True)


class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)


    async def send_bot_help(self, mapping):
        embed = discord.Embed(title = "Help", color = discord.Colour(0xBFF93A))
        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort = True)
           command_signatures = [self.get_command_signature(c) for c in filtered]
           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name = cog_name, value = "\n".join(command_signatures), inline = False)

        channel = self.get_destination()
        await channel.send(embed = embed)


    async def send_command_help(self, command):
        embed = discord.Embed(title=str(command).capitalize(), 
        description = f'```py\n{self.get_command_signature(command)}```', 
        color = discord.Colour(0xBFF93A))

        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)


    async def send_error_message(self, error):
        embed = discord.Embed(Title = "Error",
                              description = error,
                              color = discord.Colour(0xFF3333))

        channel = self.get_destination()
        await channel.send(embed = embed)

   


client.help_command = MyHelp()

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)



@client.event
async def on_ready():
    print("COGSSSS TURNINGGGGGGG")
    await client.change_presence(
        activity=discord.Activity(
            name="Vigne. Please send a professional", type = discord.ActivityType.watching
        )
    )



@client.event
async def on_message(message):
    mention = "<@!{}>".format(client.user.id)
    if mention in message.content:
        await message.channel.send("My prefix is '>'!")

    await client.process_commands(message)



client.run(token, bot = True, reconnect = True)
