import nextcord
from nextcord.ext import commands
import random
import asyncio
import operator
import time

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


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
                    return await ctx.send(f"🏆 {current_player.mention} wins the game! Congrats!!! 🎉")

            # Switch player
            current_player = opponent if current_player == ctx.author else ctx.author

            await ctx.send("🤝 It's a draw! Great match.")


    @commands.command(name="rps", help="Play Rock Paper Scissors with the bot.")
    async def rps(self, ctx, choice: str = None):
        options = {
            "rock": "🪨 Rock",
            "paper": "📄 Paper",
            "scissors": "✂️ Scissors"
        }

        if choice is None or choice.lower() not in options:
            return await ctx.send(
                "❌ Please choose rock, paper, or scissors.\n \n"
                "Example: `!rps rock`"
            )

        user_choice = choice.lower()
        bot_choice = random.choice(list(options.keys()))

        # Determine outcome
        if user_choice == bot_choice:
            result = "🤝 It's a tie!"
        elif (user_choice == "rock" and bot_choice == "scissors") or \
            (user_choice == "scissors" and bot_choice == "paper") or \
            (user_choice == "paper" and bot_choice == "rock"):
            result = "✅ You win!"
        else:
            result = "💀 You lose!"

        # Embed for better UX
        embed = nextcord.Embed(
            title="🎮 Rock Paper Scissors",
            description="Let's see who wins...",
            color=nextcord.Color.blurple()
        )
        embed.add_field(name="**🧑 Your Choice**", value=f"{options[user_choice]}\n\u200b", inline=True)
        embed.add_field(name="**🤖 Bot's Choice**", value=f"{options[bot_choice]}\n\u200b", inline=True)
        embed.add_field(name="**🏁 Result**", value=f"{result}\n\u200b", inline=True)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/616/616555.png")
        embed.set_footer(text="Thanks for playing RPS!")
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

    
    @commands.command(name="trivia", help="Play a trivia game with the bot")    
    async def trivia(self, ctx):
        questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
                "answer": "B"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": ["A) Charles Dickens", "B) William Shakespeare", "C) J.K. Rowling", "D) Mark Twain"],
                "answer": "B"
            },
            {
                "question": "Which language is used for web apps?",
                "options": ["A) Python", "B) Java", "C) JavaScript", "D) C++"],
                "answer": "C"
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
                "answer": "C"
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Oxide"],
                "answer": "B"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
                "answer": "C"
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["A) 1912", "B) 1921", "C) 1905", "D) 1899"],
                "answer": "A"
            },
            {
                "question": "Which video game features the character Master Chief?",
                "options": ["A) Halo", "B) Call of Duty", "C) Destiny", "D) Apex Legends"],
                "answer": "A"
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "options": ["A) Steel", "B) Quartz", "C) Diamond", "D) Obsidian"],
                "answer": "C"
            },
            {
                "question": "Which continent has the most countries?",
                "options": ["A) Asia", "B) Africa", "C) Europe", "D) South America"],
                "answer": "B"
            },
            {
                "question": "What is the square root of 144?",
                "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
                "answer": "B"
            },
            {
                "question": "Which programming language is known for its snake logo?",
                "options": ["A) Ruby", "B) C++", "C) Python", "D) Perl"],
                "answer": "C"
            },
            {
                "question": "What is the longest river in the world?",
                "options": ["A) Amazon", "B) Yangtze", "C) Nile", "D) Mississippi"],
                "answer": "C"
            },
            {
                "question": "What does HTTP stand for?",
                "options": ["A) HyperText Transfer Protocol", "B) HighText Transfer Protocol", "C) HyperText Transmission Process", "D) High-Tech Transfer Protocol"],
                "answer": "A"
            },
            {
                "question": "Which movie features the quote, 'I am your father'?",
                "options": ["A) Harry Potter", "B) The Matrix", "C) Star Wars", "D) Lord of the Rings"],
                "answer": "C"
            },
            {
                "question": "Which animal can sleep for up to 3 years?",
                "options": ["A) Snail", "B) Bear", "C) Koala", "D) Sloth"],
                "answer": "A"
            },
            {
                "question": "What planet has the most moons?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
                "answer": "D"
            },
            {
                "question": "Who invented the World Wide Web?",
                "options": ["A) Bill Gates", "B) Steve Jobs", "C) Tim Berners-Lee", "D) Alan Turing"],
                "answer": "C"
            },
            {
                "question": "Which country gifted the Statue of Liberty to the USA?",
                "options": ["A) England", "B) Germany", "C) France", "D) Spain"],
                "answer": "C"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A) O+", "B) AB-", "C) A-", "D) B+"],
                "answer": "B"
            },
            {
                "question": "What is the main ingredient in guacamole?",
                "options": ["A) Tomato", "B) Avocado", "C) Onion", "D) Cucumber"],
                "answer": "B"
            },
            {
                "question": "Which game holds the title for best-selling of all time (as of 2024)?",
                "options": ["A) GTA V", "B) Minecraft", "C) Tetris", "D) Fortnite"],
                "answer": "B"
            },
            {
                "question": "What is the tallest mountain in the world?",
                "options": ["A) K2", "B) Everest", "C) Kilimanjaro", "D) Elbrus"],
                "answer": "B"
            },
            {
                "question": "Which organ is the heaviest in the human body?",
                "options": ["A) Heart", "B) Brain", "C) Liver", "D) Lungs"],
                "answer": "C"
            },
            {
                "question": "What is the name of Thor’s hammer?",
                "options": ["A) Stormbreaker", "B) Excalibur", "C) Gungnir", "D) Mjolnir"],
                "answer": "D"
            },
            {
                "question": "How many legs does a spider have?",
                "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
                "answer": "B"
            },
            {
                "question": "Which color absorbs the most heat?",
                "options": ["A) White", "B) Yellow", "C) Black", "D) Red"],
                "answer": "C"
            },
            {
                "question": "What year was YouTube founded?",
                "options": ["A) 2003", "B) 2005", "C) 2007", "D) 2010"],
                "answer": "B"
            }


        ]
    
        question = random.choice(questions)
        embed = nextcord.Embed(
            title="🧠 Trivia Time! " "\n",
            description=f"**{question['question']}**\n\n" + "\n \n".join(question["options"]),
            color=nextcord.Color.blurple()
        )
        embed.set_footer(text="Reply with A, B, C, or D. You have 10 seconds!")
    
        await ctx.send(embed=embed)
    
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.upper() in ['A', 'B', 'C', 'D']
    
        try:
            msg = await self.bot.wait_for("message", check=check, timeout=20.0)
            if msg.content.upper() == question["answer"]:
                await ctx.send(f"✅ Correct, {ctx.author.mention}!You have given the right answer. 🎉")
            else:
                await ctx.send(f"❌ Oops! The correct answer was **{question['answer']}**.You should be careful next time.")
        except asyncio.TimeoutError:
            await ctx.send(f"⌛ Time's up! The correct answer was **{question['answer']}**.")      



    @commands.command(name="hangman", help="Play a game of Hangman with the bot")
    async def hangman(self, ctx):
        words = [
            "python", "discord", "hangman", "computer", "programming","game", "bot", "music", "artificial", "intelligence",
            "machine", "learning", "data", "science", "algorithm", "network", "security", "database", "software",
            "developer", "keyboard", "internet", "science", "technology"
        ]

        word = random.choice(words).upper()
        guessed = []
        attempts = 6
        display = ["_" if letter.isalpha() else letter for letter in word]

        def render_word():
            return " ".join(display)

        def get_embed():
            embed = nextcord.Embed(
                title="🎯 Hangman Game",
                description=f"```{render_word()}```",
                color=nextcord.Color.blurple()
            )
            embed.add_field(name="🧪 Attempts Left", value=str(attempts), inline=True)
            embed.add_field(name="🔠 Guessed Letters", value=", ".join(guessed) or "None", inline=True)
            embed.set_footer(text="Type a single letter. You have 60 seconds per guess.")
            return embed

        await ctx.send(embed=get_embed())

        while attempts > 0 and "_" in display:
            def check(m):
                return (
                    m.author == ctx.author and 
                    m.channel == ctx.channel and 
                    m.content.isalpha() and 
                    len(m.content) == 1
                )

            try:
                msg = await self.bot.wait_for("message", timeout=60.0, check=check)
                guess = msg.content.upper()

                if guess in guessed:
                    await ctx.send(f"🔁 You already guessed `{guess}`.")
                    continue

                guessed.append(guess)

                if guess in word:
                    for i, letter in enumerate(word):
                        if letter == guess:
                            display[i] = guess
                    await ctx.send(f"✅ Nice! `{guess}` is in the word.")
                else:
                    attempts -= 1
                    await ctx.send(f"❌ Nope! `{guess}` is not in the word. Attempts left: {attempts}")

                await ctx.send(embed=get_embed())

            except asyncio.TimeoutError:
                await ctx.send("⏰ Time's up! Game over.")
                return

        if "_" not in display:
            await ctx.send(f"🎉 Congratulations {ctx.author.mention}! You guessed the word: **{word}**")
        else:
            await ctx.send(f"💀 You lost! The word was **{word}**. Better luck next time!")


    @commands.command(name="unscramble", help="Unscramble the jumbled word!")
    async def unscramble(self, ctx):
        words = ["python", "discord", "game", "keyboard", "internet", "science", "computer", "programming", "bangladesh", "bot", "kingdom", "developer","joke", "honey",  "artificial", "intelligence", "machine", "learning", "data", "science", "algorithm", "network", "security", "database", "software"]
        word = random.choice(words)
        scrambled = ''.join(random.sample(word, len(word)))

        embed = nextcord.Embed(
            title="🔤 Unscramble the Word!",
            description=f"**Jumbled Word:** `{scrambled}`\n\n⏳ You have 30 seconds to guess!",
            color=nextcord.Color.orange()
        )
        embed.set_footer(text="Type your guess in chat!")

        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await self.bot.wait_for("message", timeout=30.0, check=check)
            if msg.content.lower() == word.lower():
                await ctx.send(f"✅ Correct! The word was **{word}**.Congrats!!! 🎉")
            else:
                await ctx.send(f"❌ Wrong! The correct word was **{word}**.Better luck next time!")
        except asyncio.TimeoutError:
            await ctx.send(f"⏰ Time's up! The word was **{word}**.Be careful next time!")


    @commands.command(name="mathquiz", help="Solve a random math problem!")
    async def mathquiz(self, ctx):
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul
        }

        op_symbol = random.choice(list(operations.keys()))
        num1 = random.randint(10, 1000)
        num2 = random.randint(1,50) if op_symbol == "*" else random.randint(10, 99)
        correct_answer = operations[op_symbol](num1, num2)

        embed = nextcord.Embed(
            title="🧮 Math Quiz",
            description=f"**Solve:** `{num1} {op_symbol} {num2}`\n⏳ You have 20 seconds!",
            color=nextcord.Color.teal()
        )
        embed.set_footer(text="Type your answer in chat!")

        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        try:
            msg = await self.bot.wait_for("message", timeout=20.0, check=check)
            if int(msg.content) == correct_answer:
                await ctx.send(f"✅ Correct! `{num1} {op_symbol} {num2} = {correct_answer}` is right. Congrats!!! 🎉")
            else:
                await ctx.send(f"❌ Wrong! The correct answer was `{correct_answer}`.Better luck next time!")
        except asyncio.TimeoutError:
            await ctx.send(f"⏰ Time's up! The correct answer was `{correct_answer}`.Be careful next time!")




    @commands.command(name="typingrace", help="Race to type a sentence the fastest!")
    async def typingrace(self, ctx):
        sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Discord bots are fun to build and play with.",
            "Typing speed is a cool skill to practice.",
            "I love programming in Python with Nextcord.",
            "Fast fingers make a big difference here!"
        ]

        sentence = random.choice(sentences)

        embed = nextcord.Embed(
            title="⌨ Typing Race Challenge!",
            description=f"Type this sentence **exactly** as fast as you can:\n\n```{sentence}```",
            color=nextcord.Color.blue()
        )
        embed.set_footer(text="First correct message wins! You have 30 seconds.")

        await ctx.send(embed=embed)

        def check(m):
            return m.channel == ctx.channel and m.content == sentence

        try:
            msg = await self.bot.wait_for("message", timeout=30.0, check=check)
            await ctx.send(f"🏆 {msg.author.mention} wins! Well done.Congrats!!! 🎉 You typed it correctly in {round((time.time() - msg.created_at.timestamp()) * 1000)} ms.")
        except asyncio.TimeoutError:
            await ctx.send(f"⏰ Time's up! Nobody typed it correctly. The sentence was:\n```{sentence}```")


    @commands.command(name="wouldyourather", help="Get a fun 'Would You Rather' question!")
    async def wouldyourather(self, ctx):
        questions = [
                ("Always speak the truth", "Always keep secrets"),
                ("Be trusted by everyone", "Be loved by everyone"),
                ("Have a loyal friend", "Be a loyal friend"),
                ("Know someone’s true feelings", "Let them know yours"),
                ("Lose all your money", "Lose all your friends"),
                ("Be honest and hurt someone", "Lie to protect their feelings"),
                ("Have a friend who tells harsh truths", "Have a friend who always agrees with you"),
                ("Be honest and misunderstood", "Hide your truth and be liked"),
                ("Never lie again", "Never trust again"),
                ("Love someone who doesn't love you", "Be loved by someone you don't love"),
                ("Always win arguments", "Always win games"),
                ("Be rich but sad", "Be happy but poor"),
                ("Fall in love with your best friend", "Fall in love with a stranger"),
                ("Be in a long-distance relationship", "Live together but rarely talk"),
                ("Love someone who doesn’t love you back", "Be loved by someone you don’t love"),
                ("Find true love but lose them", "Never find true love but avoid heartbreak"),
                ("Be with someone who makes you laugh", "Be with someone who understands your silence"),
                ("Confess your love and be rejected", "Stay silent and wonder forever"),
                ("Love once deeply", "Love many people lightly"),
                ("Be in a relationship with no trust", "Be alone but at peace"),
                ("Marry your soulmate and be poor", "Marry someone rich without love"),
                ("Lose all memories of your love", "Keep the memories but never see them again")
            ]

        option1, option2 = random.choice(questions)

        embed = nextcord.Embed(
            title="🤔 Would You Rather...",
            description=f"🔵 {option1}\n \n🔴 {option2}",
            color=nextcord.Color.purple()
        )
        embed.set_footer(text="React with 🔵 or 🔴 to choose!")

        message = await ctx.send(embed=embed)
        await message.add_reaction("🔵")
        await message.add_reaction("🔴")



def setup(bot):
    bot.add_cog(Game(bot))

