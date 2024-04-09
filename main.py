import discord
from discord.ext import commands

TOKEN = 'твой токен'

intents = discord.Intents.default()
intents.message_content = True
intents.bans = True
intents.members = True

bot = commands.Bot(command_prefix="*", intents=intents)

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="TJMS")
    if channel:
        await channel.send(f"Привет, {member.mention}! Добро пожаловать на сервер!")

@bot.command()
async def info(ctx):
    await ctx.send('Команды: *msg, *mute, *kick, *ban')

@bot.command()
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(role, send_messages=False)
    await member.add_roles(role)
    await ctx.send(f"{member.mention} теперь в муте.")

@bot.command()
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"{member.mention} был кикнут.")

@bot.command()
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f"{member.mention} был забанен.")

@bot.command()
async def msg(ctx):
    await ctx.send('Привет, мир!')

bot.run(TOKEN)
