import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'izz!')

TOKEN = 'ODkzNjIzMjk5MjQ5MTY0MzI4.YVeJjQ.l4RF-N0EHuD5rnjwiS-90fzwWGk'

@client.event
async def on_ready():
    print('hi im izzat bot')

@client.command()
async def ping(ctx):

    await ctx.send(':ping_pong: Pong , great')

@client.command()
async def say(ctx, *, message):

    await ctx.send(message)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'{user.mention} has been banned')

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"{user.mention} has been unbanned")

@client.command()
async def userinfo(ctx, *, user: discord.User = None): # b'\xfc'
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)

client.run(TOKEN)