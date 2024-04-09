import discord
from discord.ext import commands

TOKEN = 'your token'

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='/', intents=intents)

# С помощью декоратора создаём первую команду
@bot.command()
async def info(ctx):
    await ctx.send('Commands: msg')

async def message(ctx):
    await ctx.send('Hello, world!')

bot.run(TOKEN)
