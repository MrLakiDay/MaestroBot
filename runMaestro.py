import discord, os, sqlite3, string, json
from discord.ext import commands 




bot = commands.Bot(command_prefix = "Maestro, ", intents = discord.Intents.all())

# information about the connection
@bot.event
async def on_ready():
	print("The maestro took the stage... ovation!")


	global base, cur
	base = sqlite3.connect("ovation.db")
	cur = base.cursor()
	if base:
		print("the audience is happy... good!")

	base.close()


@bot.command()
async def музыку(ctx):
	await ctx.send("Приветствую тебя, я Maestro. Я несу ответственность за порядок всех процесов сервера и руковожу аркестром из ботов. Ещё я храню всю информацию о пользователях и сотрудниках этого места")


@bot.command()
async def сценарий(ctx,*,arg=None):
	author = ctx.message.author
	if arg == None:
		await ctx.send(f"{author.mention}Выберите вариант используя обращение maestro,:\nстать сотрудником\nузнать информацию об уроках") 
	elif "стать сотрудником" in arg:
		await ctx.send(f"{author.mention}Как скажите, подождите немного...")
	elif arg == "узнать информацию об уроках":
		await ctx.send(f"{author.mentions} сдесь вся информацию")
		
@bot.command(pass_context = True)

async def очистка(ctx, amount = 100):
	await ctx.channel.purge(limit = amount)

# @bot.event
# async def on_message(message):
# 	if {i.lower().translate(str.maketrans("","",string.punctuation)) for i in message.content.split(" ")}.intersection(set(json.load(open("cenz.json")))) != set():
# 		await message.channel.send("coil") 
# 		await message.delete()

# 		name = message.guild.name

# 		base.execute("CREATE TABLE IF NOT EXISTS {}(userid INT, count INT)".format(name))
# 		base.commit()


# 		warning = cur.execute("SELECT = FROM {} WHERE userid == ?".format(name),(message.author.id,)).fetchome()


# 		if warning == None:
# 			cur.execute("INSERT INTO {} VALUES(?, ?)".format(name),(message.author.id,1))
# 			base.commit()
# 			await message.channel.send(f"{message.author.mention}, БУМ! Первое придупреждение, на 3-ем мы с тобой прощаемся")		

# 		elif warning[1] == 1:
# 			cur.execute("UPDATE {} SET count == ? WHERE userid == ?".format(name),(2,message.author.id))
# 			base.commit()
# 			await message.channel.send(f"{message.author.mention}, Эй! Это уже второе придупреждение, на 3-ем мы с тобой прощаемся")

# 		elif warning[1] == 2:
# 			cur.execute("UPDATE {} SET count == ? WHERE userid == ?".format(name),(3,message.author.id))
# 			base.commit()
# 			await message.channel.send(f"{message.author.mention}, К сожелению сегодня мы прощаемся с этим участником")
# 			await message.author.ban(reason="Нецензурные выражения")


# 	await bot.process.commands(message)	


bot.run(os.getenv("token"))