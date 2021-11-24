import nextcord
from nextcord.ext import commands

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
            await member.send(f'{member.name}! You have been banned from {ctx.channel.guild.name} \n \nReason: Not Specified')
            # This command sends message in the channel for confirming BAN!
            await ctx.channel.send(f'{member.name} has been banned')
            await member.ban() # Bans the member.

        else: # If the moderator entered a reason.
            # This command sends DM to the user about the BAN!
            await member.send(f'{member.name}! You have been banned from {ctx.channel.guild.name}. \n \nReason: {reason}')
            # This command sends message in the channel for confirming BAN!
            await ctx.channel.send(f'{member.name} has been banned')
            await member.ban() # Bans the member.

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()

	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"{member} has been unbanned")

@client.command(name="userinfo")
async def userinfo(ctx,user:nextcord.Member=None):

    embed = nextcord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Resquested by - {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

    await ctx.send(embed=embed)

@client.command()
async def hyperrofel(ctx):
    await ctx.send(f"<:HYPERROFEL:892011129004523591>")

@client.command()
async def info(ctx):
    embed = nextcord.Embed(
        title = 'Infomation',
        description = 'This is a IzzatYellowStatic is a Basic Bot Worked by Python.',
        color = nextcord.Color.blurple()
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

            await member.send(f'{member.name}! You have been warned from {ctx.channel.guild.name} \n \nReason: Not Specified')

            await ctx.channel.send(f'{member.name} has been warned')

        else: 

            await member.send(f'{member.name}! You have been warned from {ctx.channel.guild.name}. \n \nReason: {reason}')

            await ctx.channel.send(f'{member.name} has been warned')

@client.command()
async def help(ctx):
    embed = nextcord.Embed(
        title = 'Help',
        description = 'My prefix is ```izz!```',
        color = nextcord.Color.blurple()
    )

    embed.add_field(name="Basic", value = "userinfo,whois,info")
    embed.add_field(name="Moderation", value = "ban,unban,warn")
    embed.add_field(name="Fun", value = "ping,hyperrofel")


    await ctx.send(embed=embed)

client.run('your token')