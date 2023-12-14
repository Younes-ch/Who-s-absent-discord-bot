from discord.ext import commands
from discord import app_commands
import discord


class MonitorChat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.interaction = None

    @app_commands.command(description="Deletes every message sent in the channel except yours and other bots'.")
    @app_commands.checks.has_any_role("Leads", "Younes", ".")
    async def shut_up(self, interaction: discord.Interaction):
        self.interaction = interaction
        await interaction.response.send_message(
            "**================================= 🤫 Dhrari tethawech wena ndhala harka7 harka7 🤫 ========================================**"
        )

    @app_commands.command(description="Stops deleting every message sent in the channel.")
    @app_commands.checks.has_any_role("Leads", "Younes", ".")
    async def stop(self, interaction: discord.Interaction):
        if self.interaction is None:
            await interaction.response.send_message("I'm not deleting messages in this channel.", ephemeral=True)
            return
        
        self.interaction = None
        await interaction.response.send_message(
            "**===================================== Arj3u ahkiw ay ==========================================**"
        )

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if self.interaction is not None:
            if message.channel == self.interaction.channel:
                if message.author != self.interaction.user and not message.author.bot:
                    await message.delete()

    @shut_up.error
    @stop.error
    async def shut_up_error(self, interaction: discord.Interaction, error: Exception):
        if isinstance(error, app_commands.MissingAnyRole):
            await interaction.response.send_message("allah ghaleb sala7iyetik ma7douda. 😏", ephemeral=True)
        else:
            embed = discord.Embed(description=":no_entry: An error occured while executing this command. Please try again later.", color=0xff0000)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            print(error)


async def setup(bot: commands.Bot):
    await bot.add_cog(MonitorChat(bot))
