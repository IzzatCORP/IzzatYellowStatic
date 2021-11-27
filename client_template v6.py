import nextcord
from nextcord.ext import commands
import random

client = commands.Bot(command_prefix = 'izz!')
client.remove_command("help")

@client.event
async def on_ready():
    print('hi im izzat bot , Are you ready')

@client.command()
async def ping(ctx):
     await ctx.send(f'Pong! In {round(client.latency * 1000)}ms , Great')

@client.command()
async def say(ctx, *, message):

    await ctx.send(message)

@client.command()
@commands.has_permissions(kick_members=True, ban_members=True, manage_roles=True) # Setting permissions that a user should have to execute this command.
async def ban(ctx, member: nextcord.Member, *, reason=None):
    if member.guild_permissions.administrator: # To check if the member we are trying to mute is an admin or not.
        await ctx.channel.send(f'You cannot ban yourself or You Dont have Permissions , Missing ```Ban Member```')

    else:
        if reason is None: # If the moderator did not enter any reason.
            # This command sends DM to the user about the BAN!
            await member.send(f'{member}! You have been banned from {ctx.channel.guild.name} \n \nReason: Not Specified')
            # This command sends message in the channel for confirming BAN!
            await ctx.channel.send(f'{member} has been banned')
            await member.ban() # Bans the member.

        else: # If the moderator entered a reason.
            # This command sends DM to the user about the BAN!
            await member.send(f'{member}! You have been banned from {ctx.channel.guild.name}. \n \nReason: {reason}')
            # This command sends message in the channel for confirming BAN!
            await ctx.channel.send(f'{member} has been banned')
            await member.ban() # Bans the member.

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()

	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"{member} has been unbanned")

@client.command()
async def hyperrofel(ctx):
    await ctx.send(f"<:HYPERROFEL:892011129004523591>")

@client.command()
async def info(ctx):
    embed = nextcord.Embed(
        title = 'Infomation',
        description = 'This is a IzzatYellowStatic is a Basic Bot Worked by Python.',
        color = 0xD5B811
    )

    embed.set_footer(text='Created by IzzatCORP#5202')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/893623299249164328/3e31e996bbd962e43d2397a31dea75fa.png?size=1024')
    embed.add_field(name='Invite My Bot', value='[click here](https://discord.com/api/oauth2/authorize?client_id=893623299249164328&permissions=545460846583&scope=bot)', inline=False)
    embed.add_field(name='GitHub', value='[click here](https://github.com/IzzatCORP/IzzatYellowStatic)', inline=False)
    embed.add_field(name='My Server', value='[click here](https://dsc.gg/izzatgang)', inline=False)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx,member : nextcord.Member,*,reason=None):
    if member == ctx.author:
        await ctx.send("You cannot warn yourself")
    else:
        if reason is None: 

            await member.send(f'{member}! You have been warned from {ctx.channel.guild.name} \n \nReason: Not Specified')

            await ctx.channel.send(f'{member} has been warned')

        else: 

            await member.send(f'{member}! You have been warned from {ctx.channel.guild.name}. \n \nReason: {reason}')

            await ctx.channel.send(f'{member} has been warned')

@client.command(aliases=["whois"])
async def userinfo(ctx, user: nextcord.Member=None):

    embed = nextcord.Embed(color = 0xD5B811)

    embed.set_author(name=f"User Infomation - {user}"),
    embed.set_thumbnail(url=user.avatar),
    embed.set_footer(text=f'Requested by {ctx.author}',icon_url=ctx.author.avatar)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)


    embed.add_field(name='Bot?',value=user.bot,inline=False)

    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, user: nextcord.Member=None):

    embed = nextcord.Embed(color=0xD5B811)

    embed.set_author(name=f"Avatar of {user}")
    embed.set_image(url=user.avatar)


    await ctx.send(embed=embed)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: nextcord.Member, p2: nextcord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver
    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            myEmbed = nextcord.Embed(title= "GAME IN PROGRESS",description="IT IS <@" + str(player1.id) + ">'s TURN.",color=0xD5B811)
            await ctx.send(embed=myEmbed)
        elif num == 2:
            turn = player2
            myEmbed = nextcord.Embed(title= "GAME IN PROGRESS",description="IT IS <@" + str(player2.id) + ">'s TURN.",color=0xD5B811)
            await ctx.send(embed=myEmbed)
    else:
        myEmbed = discord.Embed(title= "GAME IN PROGRESS",description="A GAME IS STILL IN PROGRESS. FINISH IT BEFORE STARTING A NEW ONE",color=0xD5B811)
        await ctx.send(embed=myEmbed)

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    myEmbed = nextcord.Embed(title= "WINNER!",description=mark + " :crown: ",color=0xD5B811)
                    await ctx.send(embed=myEmbed)
                elif count >= 9:
                    gameOver = True
                    myEmbed = nextcord.Embed(title= "TIE",description="IT'S A TIE :handshake:",color=0xD5B811)
                    await ctx.send(embed=myEmbed)

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                myEmbed = nextcord.Embed(title= "PLACE ERROR!",description="BE SURE TO CHOOSE AN INTEGER BETWEEN 1 AND 9 (INCLUSIVE) AND AN UNMARKED TILE. ",color=0xD5B811)
                await ctx.send(embed=myEmbed)
        else:
            myEmbed = nextcord.Embed(title= "TURN ERROR!",description="IT'S NOT YOUR TURN",color=0xD5B811)
            await ctx.send(embed=myEmbed)
    else:
        myEmbed = nextcord.Embed(title= "START GAME",description="TO START A NEW GAME, USE -tictactoe COMMAND",color=0xD5B811)
        await ctx.send(embed=myEmbed)


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = nextcord.Embed(title= "MENTION ERROR!",description="PLEASE MENTION 2 USERS",color=0xD5B811)
        await ctx.send(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = nextcord.Embed(title= "ERROR!",description="PLEASE MAKE SURE TO MENTION/PING PLAYERS (ie. <@688534433879556134>)",color=0xD5B811)
        await ctx.send(embed=myEmbed)

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = nextcord.Embed(title= "NO POSITION",description="PLEASE ENTER A POSITION TO MARK",color=0xD5B811)
        await ctx.send(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = nextcord.Embed(title= "INTEGER ERROR!",description="PLEASE MAKE SURE IT'S AN INTEGER",color=0xD5B811)
        await ctx.send(embed=myEmbed)

@client.command()
async def end(ctx):
    # We need to declare them as global first
    global count
    global player1
    global player2
    global turn
    global gameOver
        
    # Assign their initial value
    count = 0
    player1 = ""
    player2 = ""
    turn = ""
    gameOver = True

    # Now print your message or whatever you want
    myEmbed = discord.Embed(title= "RESET GAME",description="TO START A NEW GAME, USE -tictactoe COMMAND",color=0x2ecc71)
    await ctx.send(embed=myEmbed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'My prefix is ```izz!```',
        color = discord.Color.blurple()
    )
    
    embed.add_field(name="Basic", value = "userinfo,whois,info")
    embed.add_field(name="Moderation", value = "ban,unban,warn")
    embed.add_field(name="Fun", value = "ping,hyperrofel")
    embed.add_field(name="Tic Tac Toe", value = "tictactoe,place,end")


    await ctx.send(embed=embed)

client.run('your token')