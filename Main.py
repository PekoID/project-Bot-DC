from codeop import CommandCompiler
import discord
import random

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Aya'):
        calling_reply = random.randint(1, 3)
        if calling_reply == 1:
            await message.channel.send("Halo Aya disini")
        elif calling_reply == 1:
            await message.channel.send("Ya?")
        elif calling_reply == 3:
            await message.channel.send("Hmmmm?")
    elif message.content.startswith('bye'):
        goodbye_reply = random.randint(1, 3)
        if goodbye_reply == 1:
            await message.channel.send("Sampai jumpa")
        elif goodbye_reply == 1:
            await message.channel.send("dadah")
        elif goodbye_reply == 3:
            await message.channel.send("dadah")
    elif message.content.startswith('/deleteme'):
            msg = await message.channel.send('opps kata-kata dihapus')
            await msg.delete() #menghapus pesan
    else:
        await message.channel.send(message.content)

#client

@client.event #hapus pesan
async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)

@client.event #member bergabung
async def on_member_join(client.user, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

@client.event #member keluar
async def on_member_remove(client.user, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Sayonara {member.mention} !'
            await guild.system_channel.send(to_send)
