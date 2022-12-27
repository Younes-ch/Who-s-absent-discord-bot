from discord.ext import commands
from discord import app_commands
import discord

class Chkunabsent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="Tchuf les membres eli aandhum el role mawjoudin fil voice channel wela lé")
    @app_commands.describe(role="Akthar el role")
    @app_commands.checks.has_any_role("Leads", "Younes")
    async def chkunabsent(self, interaction: discord.Interaction, role: discord.Role):
        if interaction.user.voice is None:
            await interaction.response.send_message(f"{interaction.user.mention} Lezim tabda fi voice channel!", ephemeral=True)
            return
        else:
            chkun_absent: list[discord.Member] = []
            to_be_instructed: list[discord.Member] = []
            for member in role.members:
                if not member.bot:
                    if not member.voice:
                        chkun_absent.append(member)
                    elif member.voice.channel != interaction.user.voice.channel:
                        to_be_instructed.append(member)
            if to_be_instructed:
                await interaction.channel.send(f'{", ".join(map(lambda x: x.mention, to_be_instructed))} arwa7 lil channel hedhy {interaction.user.voice.channel.mention}')
            if len(chkun_absent) == 0:
                await interaction.response.send_message("Lkol hadhrin!")
            else:
                msg = ""
                for member in chkun_absent:
                    msg += member.mention + ", "
                if len(chkun_absent) == 1:
                    await interaction.response.send_message(content=f"{msg[:-2]} bech t7el el cam ki tji w ezreb ru7yk la njik bchleka.")
                else:
                    await interaction.response.send_message(content=f"{msg[:-2]}\nbech t7elu el cam ki tjiw w ezrebu rwe7kum la njikum bchleka.")

    @chkunabsent.error
    async def chkunabsent_error(self, interaction: discord.Interaction, error: Exception):
        if isinstance(error, app_commands.MissingAnyRole):
            await interaction.response.send_message("allah ghaleb sala7iyetik ma7douda. 😏", ephemeral=True)
        else:
            embed = discord.Embed(description=":no_entry: An error occured while executing this command. Please try again later.", color=0xff0000)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            print(error)

async def setup(bot: commands.Bot):
    await bot.add_cog(Chkunabsent(bot))