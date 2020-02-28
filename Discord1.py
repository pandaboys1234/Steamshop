import discord
import os

client = discord.Client()
token = 'NTE1MDY3NDExMDkxOTQ3NTQx.XlhkbQ.aTo9od8Sa5hiJbS37_oHrVu5luk'

@client.event
async def on_ready():
    game = discord.Game("!도움말")
    await client.change.presence(status=discord.Status.online, activity=Game)
    print("준비완료!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "!도움말":
        await message.channel.send("!호출")

    if message.content.startswith("/DM"): /DM 12312412 메시지 내용
        author = message.guild.get.member(int(message.content[4:22]))
        msg = message.content[23:]

access_token = os.environ["BOT_TOKEN"]    
client.run(token)

