import discord
import discord.utils
from discord.ext import commands

# from discord.utils
from datetime import datetime
import time
import math
import random


class UtilsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

   
    @commands.command(help = "Standard information about the bot.", aliases = ['info', 'idb'])
    async def bot(self, ctx):

        em = discord.Embed(
            title="Iron Divisions",
            description="<:gear:779627570882281492> I am not complete, features will always be implemented.",
            color=discord.Colour(0xBFF93A),
        )

        em.add_field(name="Upcoming features", value="Tournament related", inline=True)
        em.add_field(
            name="Built with",
            value="discord.py and Visual Studio Code",
            inline=True,
        )
        em.add_field(
            name="Feature Suggestions",
            value="Message Vigne for any suggestions to the bots!",
            inline=False,
        )

        em.add_field(
            name = 'Special functions',
            value = "'Using 15 lines for one operation' - Vigne",
            inline = True,
        )
    

        em.set_thumbnail(
            url="https://cdn.discordapp.com/emojis/766274397257334814.png"
        )
        em.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    

        await ctx.send(embed=em)




    @commands.command(help = 'Usable by Admins, this command allows them to create custom embeds.', aliases = ['em'], invoke_without_command=True)
    @commands.has_permissions(manage_channels=True)
    async def embed(
        self,
        ctx,
        title,
        desc,
        color,
        channel: discord.TextChannel = None,
        image_url=None,
        no_footer=None,
        thumbnail=None,
    ):

        # title = Title
        # desc = Description
        # color = Color
        # color = Type
        # channel = Channel
        # image_url = Image_url
        # no_footer = Footer
        # thumbnail = Thumbnail

        # CROSS

        if color.lower() == "c":
            em = discord.Embed(title=title, description=desc, color=int(0xFF1866))

            em.set_footer(
                text="{} • {}".format(
                    ctx.message.author, datetime.date.today().strftime("%d/%m/%Y")
                ),
                icon_url=ctx.message.author.avatar_url,
            )

            if image_url != None:
                em.set_image(url=image_url)
            em.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/676436383266766858/783370923364581406/Cross.png"
            )

        # TICK

        elif color.lower() == "t":
            em = discord.Embed(title=title, description=desc, color=int(0xBFF93A))

            if no_footer == None:
                em.set_footer(
                    text="{} • {}".format(
                        ctx.message.author, datetime.date.today().strftime("%d/%m/%Y")
                    ),
                    icon_url=ctx.message.author.avatar_url,
                )

            if image_url != None:
                em.set_image(url=image_url)
            em.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/676436383266766858/783370926418296892/Tick.png"
            )

        # PROGRESS

        elif color.lower() == "p":
            em = discord.Embed(title=title, description=desc, color=int(0x52BFED))

            if no_footer == None:
                em.set_footer(
                    text="{} • {}".format(
                        ctx.message.author, datetime.date.today().strftime("%d/%m/%Y")
                    ),
                    icon_url=ctx.message.author.avatar_url,
                )

            if image_url != None:
                em.set_image(url=image_url)
            em.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/676436383266766858/783370925047414835/Progress.png"
            )

        # IMPORTANT

        elif color.lower() == "i":
            em = discord.Embed(title=title, description=desc, color=int(0xFFFFFE))

            if no_footer == None:
                em.set_footer(
                    text="{} • {}".format(
                        ctx.message.author, datetime.date.today().strftime("%d/%m/%Y")
                    ),
                    icon_url=ctx.message.author.avatar_url,
                )

            if image_url != None:
                em.set_image(url=image_url)
            em.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/676436383266766858/783374855516455022/Important.png"
            )

        # COLORS

        elif color.lower() != "c" or "t" or "i" or "p":
            em = discord.Embed(title=title, description=desc, color=int(color, 16))

            if no_footer == None:
                em.set_footer(
                    text="{} • {}".format(
                        ctx.message.author, datetime.date.today().strftime("%d/%m/%Y")
                    ),
                    icon_url=ctx.message.author.avatar_url,
                )

            if thumbnail == None:
                em.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/742447002045906954/802154358330490890/Wordmark.png"
                )

            if image_url != None:
                em.set_image(url=image_url)

        # else:
        if channel != None:
            await channel.send(embed=em)
        else:
            await ctx.send(embed=em)


    @commands.group(help = "Creates a poll with 2 options.", invoke_without_command = True)
    async def poll(self, ctx, question, option1, option2, channel: discord.TextChannel = None):

        em = discord.Embed(
            title=question,
            description="\n",
            color=discord.Colour(0xBFF93A),
            timestamp=datetime.utcnow(),
        )

        em.add_field(name="Option  <:One:802230121887957054>", value=option1)
        em.add_field(name="Option  <:Two:802230122362044446>", value=option2, inline=True)

        em.set_footer(
            text=f"Started by {ctx.message.author} • {datetime.now().strftime('%d/%m/%Y')}"
        )

        ctxmessage = await ctx.send(embed=em)

        if channel != None:
            chanmessage = await channel.send(embed=em)

            chanmessage
            await chanmessage.add_reaction("<:One:802230121887957054>")
            await chanmessage.add_reaction("<:Two:802230122362044446>")

        else:
            ctxmessage
            await ctxmessage.add_reaction("<:One:802230121887957054>")
            await ctxmessage.add_reaction("<:Two:802230122362044446>")



    @poll.command(help = "Used by staff to create match prediction polls for presentation.")
    @commands.has_permissions(manage_messages = True)
    async def team(self, ctx, team1, team2, map1, map2, map3, channel: discord.TextChannel = None):

        em1 = discord.Embed(
            title = f"{map1}",
            description = "\n",
            color = discord.Colour(0xBFF93A),
        )

        em1.add_field(
            name = f"{team1}  <:One:802230121887957054>",
            value = "Team 1",
        )

        em1.add_field(
            name = f"{team1}  <:Two:802230122362044446>",
            value = "Team 2",
        )

        em1.set_footer(
            text=f"Started by {ctx.message.author} • {datetime.now().strftime('%d/%m/%Y')}"
        )

        if channel != None:
            embed1 = await channel.send(embed = em1)
            embed1
            await embed1.add_reaction('<:One:802230121887957054>')
            await embed1.add_reaction("<:Two:802230122362044446>")

        else:
            embed1 = await ctx.send(embed = em1)
            embed1
            await embed1.add_reaction('<:One:802230121887957054>')
            await embed1.add_reaction("<:Two:802230122362044446>")

        time.sleep(3)


        em2 = discord.Embed(
            title = f"{map2}",
            description = "\n",
            color = discord.Colour(0xBFF93A),
        )

        em2.add_field(
            name = f"{team1}  <:One:802230121887957054>",
            value = "Team 1",
        )

        em2.add_field(
            name = f"{team1}  <:Two:802230122362044446>",
            value = "Team 2",
        )

        em2.set_footer(
            text=f"Started by {ctx.message.author} • {datetime.now().strftime('%d/%m/%Y')}"
        )

        if channel != None:
            embed2 = await channel.send(embed = em2)
            embed2
            await embed2.add_reaction('<:One:802230121887957054>')
            await embed2.add_reaction("<:Two:802230122362044446>")

        else:
            embed2 = await ctx.send(embed = em2)
            embed2
            await embed2.add_reaction('<:One:802230121887957054>')
            await embed2.add_reaction("<:Two:802230122362044446>")

        time.sleep(3)


        
        em3 = discord.Embed(
            title = f"{map3}",
            description = "\n",
            color = discord.Colour(0xBFF93A),
        )

        em3.add_field(
            name = f"{team1}  <:One:802230121887957054>",
            value = "Team 1",
        )

        em3.add_field(
            name = f"{team1}  <:Two:802230122362044446>",
            value = "Team 2",
        )

        em3.set_footer(
            text=f"Started by {ctx.message.author} • {datetime.now().strftime('%d/%m/%Y')}"
        )

        if channel != None:
            embed3 = await channel.send(embed = em3)
            embed3
            await embed3.add_reaction('<:One:802230121887957054>')
            await embed3.add_reaction("<:Two:802230122362044446>")

        else:
            embed3 = await ctx.send(embed = em3)
            embed3
            await embed3.add_reaction('<:One:802230121887957054>')
            await embed3.add_reaction("<:Two:802230122362044446>")

            time.sleep(3)



    @commands.command(name = "8ball", help = "Your soon to be fortune teller")
    async def _8ball(self, ctx, *, arg):
        says = ['lol', 'probably', 'ask james bond', 'dlaczego korzystasz z tłumacza?', 'no little one', "why even ask", "https://cdn.discordapp.com/attachments/412122106361282571/811816432005939230/video0-50.mp4"]
        rannum = random.randint(0, (len(says)-1))
        await ctx.send(says[rannum])


# py -3.8 'c:\Users\Fiery\OneDrive\Desktop\Cod Fish\Iron Cog Test\main.py'


def setup(bot):
    bot.add_cog(UtilsCog(bot))
