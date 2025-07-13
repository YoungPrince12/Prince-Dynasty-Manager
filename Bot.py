import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
rankings_list = []

@bot.event
async def on_ready():
    print(f'✅ Bot online as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('🏓 Pong!')

@bot.command()
async def nextsim(ctx):
    await ctx.send('🕒 Next Sim: Friday @ 8PM CST')

@bot.command()
async def teams(ctx):
    teams = ['Alabama', 'LSU', 'Texas', 'Florida State']
    await ctx.send('🏈 Dynasty Teams:\n' + '\n'.join(teams))

@bot.command()
async def potw(ctx):
    await ctx.send('🏆 Player of the Week:\nRB #5 – 178 YDS, 2 TDs')

@bot.command()
async def gotw(ctx):
    await ctx.send('📺 Game of the Week:\n#3 Texas vs #1 Georgia 🔥')

@bot.command()
async def rankings(ctx):
    if not rankings_list:
        await ctx.send('❌ No rankings have been set yet.')
    else:
        await ctx.send('📊 Top 25 Rankings:\n' + '\n'.join(rankings_list))

@bot.command()
@commands.has_permissions(administrator=True)
async def setrankings(ctx, *, text):
    global rankings_list
    rankings_list = text.split('\n')
    await ctx.send('✅ Rankings updated!')

token = os.getenv('DISCORD_TOKEN')
if not token:
    print('⚠️ DISCORD_TOKEN not set!')
else:
    bot.run(token)
