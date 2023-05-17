from discord import Client, Intents, Message
import os
from dotenv import load_dotenv


# Bikin Client baru dengan all intent (ini bot kamu)
client = Client(intents=Intents.all())


# Event listener yang dijalankan ketika ada message
@client.event
async def on_message(message: Message):
    prefix = "d!" # Prefix bot kamu

    # Kalau prefix gak sesuai, kacangin usernya
    if not message.content.startswith(prefix):
        return

    # Ping command
    if message.content == prefix + "ping":
        await message.reply("Pong!")

    # TODO: tambahin command lagi buat botnya
    # if message.content == prefix + "command":
    #     do_something()


# Event listener yang dijalankan ketika bot ready
@client.event
async def on_ready():
    print()
    print("Siap 86, %s" % os.getenv("CLIENT_NAME"))


if __name__ == "__main__":
    load_dotenv() # Load environment variable dari file .env
    client.run(token=os.getenv("TOKEN")) # Jalanin botnya