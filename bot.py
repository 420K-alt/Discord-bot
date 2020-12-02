import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os

bot = commands.Bot(command_prefix = "ez ")
@bot.remove_command("help")

# --------------------------------------------------------------------  BOT ON READY START  --------------------------------------------------------------------
@bot.event
async def on_ready():
    print("Im runing bicth")
    await bot.change_presence(activity=discord.Game('420 & LoTus'))
# --------------------------------------------------------------------  BOT ON READY END  --------------------------------------------------------------------


#########################################
#                                       #
# [1] BOT ON READY         l.15         #
# [2] HELP PANNEL          l.30-80      #
# [3] FUN COMMAND          l.80-150     #
# [4] USFUL COMMAND        l.150-200    #
# [5] NSFW COMMAND         l.200-215    #
# [6] MODERATOR COMMAND    l.220-240    #
#                                       #
#########################################


# --------------------------------------------------------------------  HELP PANNEL START  --------------------------------------------------------------------
@bot.command()
async def help(ctx):

    modo_text = ('''
    `ez ban {user} {reasone}` = bans a user
    `ez kick {user} {reasone}` = kicks a user
    `ez clear (amount)` = clear the amount of messages
    ''')

    fun_text = ('''
    `ez chifoumi {c/f/p}` = play chifoumi with the bot
    `ez gay` = calculate your gay percentage
    `ez qi` = calculate your IQ
    `ez suicide` = kicks you from the server

    ''')

    raid_text = ('''
    NOTHING HERE FOR THE MOMENT
    ''')

    nsfw_text = ('''
    `ez nude` = sends nice nudes in your dm
    `ez hentai` = sends nice hentai in your dm
    ''')

    utile_text = ('''
    `ez userinfo` @member = get info on a user
    `ez botinfo` = show information on the bot
    `ez eztool` = show information on the Ez Tools team

    ''')


    embedVar = discord.Embed(title="Ez Tools Bot", color=0x000000)
    embedVar.add_field(name="-----FUN COMMAND-----", value=fun_text, inline=False)
    embedVar.add_field(name="-----USFUL-----", value=utile_text, inline=False)
    embedVar.add_field(name="-----MODARATION-----", value=modo_text, inline=False)
    embedVar.add_field(name="-----NSFW-----", value=nsfw_text, inline=False)
    embedVar.add_field(name="-----RAID-----", value=raid_text, inline=False)
    embedVar.set_thumbnail(url = "https://cdn.discordapp.com/attachments/737813830859489303/762087036538454026/79433c696ad38cf37f778d193d33ea69.png")
    embedVar.set_image(url="https://cdn.discordapp.com/attachments/730024711546994773/766083065654804500/unknown.png")

    await ctx.channel.send(embed=embedVar)
# --------------------------------------------------------------------  HELP PANNEL END  --------------------------------------------------------------------


# --------------------------------------------------------------------  FUN COMMAND START  --------------------------------------------------------------------
@bot.command()
async def gay(ctx):
    rand = random.randint(1,100)
    embed = discord.Embed(title = "**pourcentage de gayittude**", description = rand)
    embed.set_image(url="https://cdn.discordapp.com/attachments/730024711546994773/765995971473309736/101470739_o.png")
    embed.set_author(name="Ez Tools Bot")
    await ctx.send(embed = embed)
    print("Done")

@bot.command()
async def qi(ctx):
    rand = random.randint(1,200)
    embed = discord.Embed(title = "**Ton QI:**", description = rand)
    embed.set_image(url="https://cdn.discordapp.com/attachments/730024711546994773/765995033978732554/cannabis-qi.png")
    embed.set_author(name="Ez Tools Bot")
    await ctx.send(embed = embed)
    print("done")

@bot.command()
async def chifoumi(ctx, choix):
    result = random.randint(0,2)

    if choix == "f": user_choix = "Feuille :seedling:" 
    if choix == "p": user_choix = "Pierre :rock:"
    if choix == "c": user_choix = "Ciseaux :scissors:"

    if result == 0:
        if choix == "f": bot_choix = "Feuille :seedling:" 
        if choix == "p": bot_choix = "Pierre :rock:"
        if choix == "c": bot_choix = "Ciseaux :scissors:"

        embed = discord.Embed(colour=0x000000)
        embed = discord.Embed(title="EQUAL", description=f" User: {user_choix} \nBot: {bot_choix}", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/734943221914009660/772573603925458984/cartoon-rock-paper-scissors-vector-characters-ConvertImage.jpg")
        embed.set_author(name="Ez Tools Bot")
        await ctx.send(embed = embed)

    if result == 1:
        if choix == "c": bot_choix = "Feuille :seedling:" 
        if choix == "f": bot_choix = "Pierre :rock:"
        if choix == "p": bot_choix = "Ciseaux :scissors:"

        embed = discord.Embed(colour=0x000000)
        embed = discord.Embed(title="VICTORY", description=f" User: {user_choix} \nBot: {bot_choix}", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/734943221914009660/772573603925458984/cartoon-rock-paper-scissors-vector-characters-ConvertImage.jpg")
        embed.set_author(name="Ez Tools Bot")
        await ctx.send(embed = embed)

    if result == 2:
        if choix == "c": bot_choix = "Pierre :rock:"
        if choix == "f": bot_choix = "Ciseaux :scissors:"
        if choix == "p": bot_choix = "Feuille :seedling:" 

        embed = discord.Embed(colour=0x000000)
        embed = discord.Embed(title="DEFEAT", description=f" User: {user_choix} \nBot: {bot_choix}", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/734943221914009660/772573603925458984/cartoon-rock-paper-scissors-vector-characters-ConvertImage.jpg")
        embed.set_author(name="Ez Tools Bot")
        await ctx.send(embed = embed)


@bot.command()
async def suicide(ctx):
    rip = ctx.message.author.id
    await ctx.guild.kick(discord.Object(id=rip))
    try:
        await ctx.send(f":skull:  {ctx.message.author.mention} comited suicide")
    except:
        pass
# --------------------------------------------------------------------  FUN COMMAND END  --------------------------------------------------------------------


# --------------------------------------------------------------------  USFUL COMMAND START  --------------------------------------------------------------------
@bot.command()
async def botinfo(ctx):

    embed = discord.Embed(colour=0x000000, timestamp = ctx.message.created_at)
    embed.set_author(name="Bot Info")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/737813830859489303/762087036538454026/79433c696ad38cf37f778d193d33ea69.png")
    embed.add_field(name="NAME", value="Ez Tools Bot", inline=False)
    embed.add_field(name="PREFIX", value="ez", inline=False)
    embed.add_field(name="DEV", value="420 & loTus01", inline=False)
    embed.add_field(name="GUILDS", value=str(len(bot.guilds)), inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member:discord.Member):

    embed = discord.Embed(colour=0x000000, timestamp = ctx.message.created_at)
    embed.set_author(name="User info")
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Pseudo", value=member)
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Surnom", value=member.display_name)
    embed.add_field(name="\nCreated at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"))
    await ctx.send(embed=embed)

@bot.command()
#@commands.has_permissions(administrator=True)
async def eztool(ctx):
    embed = discord.Embed(title = "**EZ TOOLS**")
    embed = discord.Embed(description="It's a team based on the proggramation with python. The team is composed of 4 people : **Traxsab**, **420**, **Hawks** and **loTus**. They already did a lot of projet like ultra gen, keylogger, mail bomber, bot raid and more...")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/737813830859489303/762087036538454026/79433c696ad38cf37f778d193d33ea69.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/730024711546994773/766073152040075304/unknown.png")
    embed.set_author(name="Ez Tools Bot")
    await ctx.send(embed = embed)
    print("done")


# --------------------------------------------------------------------  USFUL COMMAND END  --------------------------------------------------------------------


# --------------------------------------------------------------------  NSFW COMMAND START  --------------------------------------------------------------------
@bot.command()
async def nude(ctx):
    folder = os.path.dirname(os.path.abspath(__file__))
    folder = folder + "/#THE_SHITE_WE_NEED/nude.txt"
    random_lines = random.choice(open(folder).readlines())
    embed = discord.Embed(title = f"nude asked by {ctx.message.author}")
    embed.set_image(url=random_lines)
    await ctx.author.send(embed = embed)
    await ctx.send("The command has been successfully done, check you're dm :white_check_mark:")

@bot.command()
async def hentai(ctx):
    folder = os.path.dirname(os.path.abspath(__file__))
    folder = folder + "/#THE_SHITE_WE_NEED/hentai.txt"
    random_lines = random.choice(open(folder).readlines())
    embed = discord.Embed(title = f"nude asked by {ctx.message.author}")
    embed.set_image(url=random_lines)
    await ctx.author.send(embed = embed)
    await ctx.send("The command has been successfully done, check you're dm :white_check_mark:")


# --------------------------------------------------------------------  NSFW COMMAND END  --------------------------------------------------------------------

@bot.command()
async def spam(ctx, member:discord.Member, *, why):
    for i in range(5):
        await ctx.send(f"{member.mention} {why} {ctx.message.author.mention}")

@bot.command()
async def dire(ctx, member:discord.Member, *, why):
    await ctx.send(f"{ctx.message.author.mention} {why} {member.mention} :doghehe: ")

# --------------------------------------------------------------------  MODERATOR COMMAND START  --------------------------------------------------------------------
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, why):
    try:
        await ctx.send(f":white_check_mark: {member.mention} got kick by {ctx.message.author.mention}. Reason: {why}")
        await ctx.guild.kick(member)
    except:
        await ctx.send(f":x: {ctx.message.author.mention} I can't kick {member.mention}")

@bot.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member:discord.Member, *, why):
    try:
        await ctx.send(f":white_check_mark: {member.mention} got ban by {ctx.message.author.mention}. Reason: {why}")
        await ctx.guild.ban(member)
    except:
        await ctx.send(f":x: {ctx.message.author.mention} I can't ban {member.mention}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'> {amount} messages on ete supprimer :white_check_mark:')   

# --------------------------------------------------------------------  MODERATOR COMMAND END  --------------------------------------------------------------------


bot.run("NzY2MDYwMzU1MTg4NTU1ODU3.X4d3TQ.Lv27VmgvIJKPSRNUwpv4evG13gE")