import discord
from discord import app_commands
from discord.ui import Button, View, Modal, Select
import json, requests, os
from dotenv import load_dotenv
# โหลด token จาก .env
load_dotenv()
token = os.getenv("MTQzMDg3NDgzOTUyNjI3NzMwMA.GZXx4o.nwI7OU_lN6Dgci9g9r688L3YhZGUlOD4MkDygY")


serverID = 1430391277618200618
phone = "0950189983"
admin_id = 1430381718447325307  # แทนด้วย Discord ID จริงของคุณ

intents = discord.Intents.all()

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=discord.Object(id=serverID))
        await self.tree.sync(guild=discord.Object(id=serverID))

client = MyClient(intents=intents)

# ---------------- เติมเงิน ----------------
class ShoppingModal(discord.ui.Modal, title="เติมเงิน"):
    link_angpao = discord.ui.TextInput(label="ลิ้งค์อั่งเปา", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        user = interaction.user
        redeem_link = self.link_angpao.value
        response = requests.post("https://restapi.kdkddmdmdd.repl.co/undefined_store/topupwallet",
                                 json={"mobile": phone,"link": redeem_link}).json()
        
        if response.get("status") == True:
            money = response["amount"]
            filepath = f"{user.id}.json"
            if os.path.exists(filepath):
                with open(filepath, "r") as f:
                    database = json.load(f)
                last_money = database[str(user.id)]["money"]
                last_accumulate = database[str(user.id)]["accumulate"]
            else:
                last_money, last_accumulate = 0, 0
            
            update_money = float(last_money) + float(money)
            update_accumulate = float(last_accumulate) + float(money)
            data = {
                str(user.id): {
                    "name": user.name,
                    "money": update_money,
                    "accumulate": update_accumulate
                }
            }
            with open(filepath, "w") as f:
                json.dump(data, f, indent=4)

            embed = discord.Embed(title="เติมเงินสำเร็จ", description=f"จำนวน {money} บาท", color=0x00ff00)
            embed.set_footer(text=f"ยอดเงินคงเหลือ : {update_money} บาท")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("เติมเงินไม่สำเร็จ ❌", ephemeral=True)

# ---------------- คำสั่ง shop ----------------
@client.tree.command(description="ร้านค้า")
async def shop(interaction: discord.Interaction):
    if interaction.user.id != admin_id:
        await interaction.response.send_message("คุณไม่มีสิทธิ์ใช้คำสั่งนี้", ephemeral=True)
        return

    async def button_callback(interaction: discord.Interaction):
        await interaction.response.send_modal(ShoppingModal())

    button = Button(label="เติมเงิน", style=discord.ButtonStyle.green, emoji="🧧")
    button.callback = button_callback

    embed = discord.Embed(title="ร้านค้า", description="กดปุ่มเพื่อเติมเงิน", color=0x00ff00)
    view = View()
    view.add_item(button)
    await interaction.response.send_message(embed=embed, view=view)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

client.run("MTQzMDg3NDgzOTUyNjI3NzMwMA.GZXx4o.nwI7OU_lN6Dgci9g9r688L3YhZGUlOD4MkDygY")
