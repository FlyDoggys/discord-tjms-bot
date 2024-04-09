import discord
from discord.ext import commands

TOKEN = 'your token'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="название-канала")
    if channel:
        await channel.send(f"Привет, {member.mention}! Добро пожаловать на сервер!")

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="название-канала")
    if channel:
        await channel.send(f"Жаль, что {member.name} покинул сервер.")

@bot.command()
async def info(ctx):
    await ctx.send('Команды: *msg, *mute, *kick, *ban')


bot.run(TOKEN)
