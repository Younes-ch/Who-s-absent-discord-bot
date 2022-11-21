import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
# from keep_alive import keep_alive
import os


load_dotenv()
intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.listening, name="&chkunabsent")
logging.basicConfig(level=logging.INFO)
bot = commands.Bot(command_prefix='&', intents=intents)


@bot.event
async def on_ready():
  print("Ready!")

@bot.command()
@commands.has_any_role("Leads", "Younes")
async def chkunabsent(ctx, *, role : discord.Role):
  if ctx.author.voice == None:
    await ctx.send(f"{ctx.author.mention} Lezim tabda fi voice channel!")
  else:
    chkun_absent = []
    for member in role.members:
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

@chkunabsent.error
async def chkunabsent_error(ctx, error : commands.CommandError):
  print(error)
  if isinstance(error, commands.RoleNotFound):
    await ctx.message.add_reaction("❌")
    await ctx.send("Role mahuch mawjud manaarch mnin tlaat bih. 🤔")
  elif isinstance(error, commands.CheckFailure):
    await ctx.message.add_reaction("❌")
    await ctx.send("allah ghaleb sala7iyetik ma7douda. 😏")
  else:
    await ctx.message.add_reaction("❌")
    await ctx.send("Zidna el role yarhem bouk! 🤦")

# keep_alive()
bot.run(os.environ["TOKEN"])
