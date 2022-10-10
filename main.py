import discord
from discord.ext import tasks, commands
import logging
import os

intents = discord.Intents.all()
logging.basicConfig(level=logging.INFO)
activity = discord.Activity(type=discord.ActivityType.listening, name="&help")
bot = commands.Bot(command_prefix='&', intents=intents, activity=activity)


@bot.event
async def on_ready():
  print("Ready!")

@bot.command()
async def chkunabsent(ctx):
  if ctx.author.voice == None:
    await ctx.send(f"{ctx.author.mention} Lezim tabda fi voice channel!")
  else:
    core_team_role = ctx.guild.get_role(1028809168875966526)
    chkun_absent = []
    for member in core_team_role.members:
      if not member.voice:
        chkun_absent.append(member)
      elif member.voice.channel != ctx.author.voice.channel:
        await ctx.send(f"{member.mention} arwa7 lil channel hedhy {ctx.author.voice.channel.mention}")
    print(chkun_absent)
    if len(chkun_absent) == 0:
      await ctx.send("Lkol hadhrin!")
    else:
      msg = ""
      for member in chkun_absent:
        msg += member.mention + ", "
      if len(chkun_absent) == 1:
        await ctx.send(f"{msg[:-2]} bech t7el el cam ki tji w ezreb ru7yk la njik bchleka.")
      else:
        await ctx.send(f"{msg[:-2]}\nbech t7elu el cam ki tjiw w ezrebu rwe7kum la njikum bchleka.")
        
bot.run(os.getenv("TOKEN"))
