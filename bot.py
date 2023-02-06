import asyncio
import discord
from discord import app_commands, Embed, File
from dotenv import load_dotenv
import os
from ranking.RankingCommands import Rank
from matchmaking.QueueCommands import Queue
from user.UserCommands import User
from match.MatchCommands import Match

load_dotenv()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@app_commands.command(name="ajuda", description="Comando de ajuda")
async def help(ctx):
    await ctx.response.defer(ephemeral=True)
    embed = Embed(title=f"ajuda!!", description="Como configurar o bot", color=0x64e4f5)
    file = File("./assets/Marvin.png")
    embed.set_thumbnail(url="attachment://Marvin.png")
    embed.add_field(name="1. Usuário", value="/user ingame <your-username>", inline=False)
    embed.add_field(name="2. Iniciar modo ranqueado", value="/queue casual", inline=False)
    embed.add_field(name="3. Dar os resultados da partida", value="/match report win 4-2", inline=False)
    embed.add_field(name="4. Verifica as tuas estatisticas", value="/user stats", inline=False)
    embed.add_field(name="Full doc:", value="https://pl-sergent.gitbook.io/multilivequeue/", inline=False)
    await ctx.followup.send(file=file, embed=embed)

@client.event
async def on_ready():
    await client.wait_until_ready()
    tree.add_command(Queue(client))
    tree.add_command(User())
    tree.add_command(Rank())
    tree.add_command(Match(client))
    tree.add_command(help)
    await tree.sync()
    print("Bot online!")

client.run(os.getenv('TOKEN'))