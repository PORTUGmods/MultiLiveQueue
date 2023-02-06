from discord import app_commands, Embed, File
from user.UserController import UserController


PATH = "./data/"
PATH_PLAYER = "./data/players/"

@app_commands.guild_only()
class User(app_commands.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @app_commands.command(name="stats", description="Mostra as tuas estatisticas do pareamento customizado")
    async def stats(self, ctx):
        await ctx.response.defer()
        username = ctx.user.name + "#" + ctx.user.discriminator
        user = UserController(username)
        if user.matches_played == 0:
            winrate = 0
        else:
            winrate = (user.matches_won/user.matches_played)*100

        embed = Embed(title=f"📊 {username} ranked stats!", color=0x64e4f5)
        file = File("./assets/Marvin.png")
        embed.set_thumbnail(url="attachment://Marvin.png")
        embed.add_field(name="Nome no jogo", value=user.in_game_username, inline=False)
        embed.add_field(name="⚔️ Jogadas", value=user.matches_played, inline=True)
        embed.add_field(name="✅ vencidas", value=user.matches_won, inline=True)
        embed.add_field(name="😬 MMR (Taxa de vitória)", value=f"{winrate:.2f}%", inline=True)
        embed.add_field(name="❌ Multiplicador", value=f"{user.winstreak_multiplier:.2f}", inline=True)
        embed.add_field(name="🏅 Rank", value=user.ranking, inline=True)
        embed.add_field(name="💯 Pontos", value=f"{user.ranking_points:.2f}", inline=True)
        await ctx.followup.send(file=file, embed=embed)
    
    @app_commands.command(name="rank", description="Mostra o teu rank")
    async def rank(self, ctx):
        user = UserController(ctx.user.name + "#" + ctx.user.discriminator)
        await ctx.response.send_message(
            f"{user.username} tem o rank {user.ranking} com {user.ranking_points} pontos."
        )

    @app_commands.command(name="nick", description="Coloca aqui o teu nick da conta da warner bros")
    async def ingame(self, ctx, ingame_username: str):
        user = UserController(ctx.user.name + "#" + ctx.user.discriminator)
        user.add_ingame_username(ingame_username)
        await ctx.response.send_message(f"O teu nick em jogo é {ingame_username}.")
    
    @app_commands.command(name="estatisticas", description="Mostra as tuas estatisticas no multiversus")
    async def muliversus(self, ctx):
        user = UserController(ctx.user.name + "#" + ctx.user.discriminator)
        await ctx.response.send_message(
            f"Aqui estão as tuas estatisticas https://muliversus.plsergent.xyz/{user.in_game_username}"
        )
        