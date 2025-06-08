import nextcord
from nextcord.ext import commands
import random
import asyncio

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Play Rock Paper Scissors with the bot")
    async def rps(self, ctx, choice: str = None):
        options = ['rock', 'paper', 'scissors']
        if choice not in options:
            return await ctx.send("❌ Please choose rock, paper, or scissors. Example: `!rps rock`")
        
        bot_choice = random.choice(options)
        outcome = {
            ('rock', 'scissors'): 'You win!',
            ('scissors', 'paper'): 'You win!',
            ('paper', 'rock'): 'You win!',
            (choice, choice): 'It\'s a tie!',
        }.get((choice, bot_choice), 'You lose!')

        embed = nextcord.Embed(
            title="🪨📄✂️ Rock Paper Scissors!",
            color=nextcord.Color.purple()
        )
        embed.add_field(name="Your Choice", value=choice.capitalize())
        embed.add_field(name="Bot's Choice", value=bot_choice.capitalize())
        embed.add_field(name="Result", value=outcome)
        await ctx.send(embed=embed)


    @commands.command(help="Play a number guessing game with the bot")
    async def guessnumber(self, ctx):
        number = random.randint(1, 10)
        await ctx.send("🎯 I’ve picked a number between 1 and 10. Try to guess it!")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

        for _ in range(3):
            try:
                msg = await self.bot.wait_for('message', timeout=20.0, check=check)
            except asyncio.TimeoutError:
                return await ctx.send(f"⏰ Time's up! The number was {number}.")

            guess = int(msg.content)
            if guess == number:
                return await ctx.send(f"🎉 Correct! You guessed it.")
            elif guess < number:
                await ctx.send("🔼 Too low!")
            else:
                await ctx.send("🔽 Too high!")

        await ctx.send(f"😢 No more tries! The number was {number}.")

    @commands.command(name="coinflip", aliases=["flip", "cf"], help="Flip a coin and see if it lands on heads or tails")
    async def coinflip(self, ctx):
        flipping = await ctx.send("🪙 Flipping the coin...")
        
        
        await asyncio.sleep(1.2)
        await flipping.edit(content="🌀 Tossing the coin high in the air...")
        await asyncio.sleep(1.2)

        
        result = random.choice(["Heads", "Tails"])
        emoji = "🪙" if result == "Heads" else "🥏"
        color = nextcord.Color.green() if result == "Heads" else nextcord.Color.blue()

        
        embed = nextcord.Embed(
            title="**Coin Flip Result!**",
            description=f"The coin landed on:\n\n{emoji} **{result.upper()}**",
            color=color
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/643/643350.png")
        await asyncio.sleep(1)
        await flipping.edit(content=None, embed=embed)



    @commands.command(name="tictactoe", help="Play a Tic-Tac-Toe game with another user.")
    async def tictactoe(self, ctx, opponent: nextcord.Member = None):
        if opponent is None:
            return await ctx.send("❗ You must mention someone to play with. Usage: `!tictactoe @user`")

        if opponent.bot or opponent == ctx.author:
            return await ctx.send("❌ Invalid opponent. Choose a human other than yourself.")

        board = [":white_large_square:"] * 9
        current_player = ctx.author
        players = {ctx.author: "❌", opponent: "⭕"}

        def format_board():
            rows = []
            for i in range(0, 9, 3):
                rows.append(" ".join(board[i:i+3]))
            return "\n".join(rows)

        embed = nextcord.Embed(
            title="🎮 Tic-Tac-Toe",
            description=f"{ctx.author.mention} vs {opponent.mention}\n\n{format_board()}",
            color=nextcord.Color.gold()
        )
        embed.set_footer(text="Type a number (1-9) to mark your move.")
        game_msg = await ctx.send(embed=embed)

        def check(m):
            return m.author == current_player and m.channel == ctx.channel and m.content.isdigit()

        for turn in range(9):
            await ctx.send(f"🔢 {current_player.mention}, choose a position (1-9):")

            try:
                msg = await self.bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                return await ctx.send(f"⏰ Time's up! {current_player.mention} didn't respond. Game over.")

            pos = int(msg.content) - 1
            if not 0 <= pos <= 8 or board[pos] != ":white_large_square:":
                await ctx.send("⚠️ Invalid move. That spot is already taken or out of bounds.")
                continue

            board[pos] = players[current_player]

            # Update the board
            embed.description = f"{ctx.author.mention} vs {opponent.mention}\n\n{format_board()}"
            embed.set_footer(text=f"Turn: {opponent.display_name if current_player == ctx.author else ctx.author.display_name}")
            await game_msg.edit(embed=embed)

            # Win checking
            win_combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            for x, y, z in win_combos:
                if board[x] == board[y] == board[z] != ":white_large_square:":
                    return await ctx.send(f"🏆 {current_player.mention} wins the game!")

            # Switch player
            current_player = opponent if current_player == ctx.author else ctx.author

        await ctx.send("🤝 It's a draw! Great match.")



def setup(bot):
    bot.add_cog(Game(bot))

