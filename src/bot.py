import asyncio, discord, os, dotenv, json
from datetime import datetime


async def get_note():
    with open("data/new_notes.json", encoding='utf-8') as json_file:
        list_eval = json.load(json_file)
        for eval in list_eval:
            await send_note(eval)


async def send_note(eval):
    guild = bot.get_guild(SERVER_GEII)
    channel = guild.get_channel(CHANNEL_NOTE)
    date_obj = datetime.fromisoformat(eval["date"])
    eval["date"] = date_obj.strftime("%d/%m/%Y")
    # Création de l'objet Embed
    crousEmbed = discord.Embed(color=0x004996, title='Note IUT Mulhouse',
                               url='https://notes.iutmulhouse.uha.fr/')
    # crousEmbed.set_author(name='Alerte à la note !!!', icon_url='https://i.imgur.com/sI7EssK.png')
    # crousEmbed.set_thumbnail(url='https://i.imgflip.com/6bbwfy.jpg')

    # Supposons que new_note est un objet avec les attributs appropriés
    crousEmbed.add_field(name='Date', value=eval["date"], inline=False)
    crousEmbed.add_field(name=eval["matiere"],
                         value=eval["titre"], inline=False)
    crousEmbed.add_field(name='Coef', value=eval["coef"], inline=False)
    note = eval["note"]
    crousEmbed.add_field(name='Minimum', value=note["min"], inline=True)
    crousEmbed.add_field(name='Moyenne', value=note["moy"], inline=True)
    crousEmbed.add_field(name='Maximum', value=note["max"], inline=True)

    # Remplacez 'picture_linker(moy)' par le lien réel de l'image
    # crousEmbed.set_image(url='https://i.imgur.com/1AUc8m7.jpg')
    crousEmbed.set_footer(
        text='BOT GEII', icon_url='https://i.imgur.com/dwti2sm.png')
    crousEmbed.timestamp = datetime.now()  # Met à jour le timestamp
    await channel.send(embed=crousEmbed)


async def send_menu():
    with open("data/menus.json", encoding='utf-8') as json_file:
        carte_crous = json.load(json_file)
    guild = bot.get_guild(SERVER_GEII)
    channel = guild.get_channel(CHANNEL_CROUS)
    crousEmbed = discord.Embed(color=0xf54242, title='RestoU CROUS',
                               url='https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2/')
    for key in carte_crous.keys():
        crousEmbed.add_field(name=key, value="\n".join(carte_crous[key]), inline=False)
    crousEmbed.set_footer(
        text='BOT GEII', icon_url='https://i.imgur.com/dwti2sm.png')
    crousEmbed.timestamp = datetime.now()  # Met à jour le timestamp
    await channel.send(embed=crousEmbed)


async def handle_client(reader, writer):
    data = await reader.read(100)  # Lire les données envoyées par le client
    message = data.decode()
    # addr = writer.get_extra_info('peername')
    # print(f"Reçu {message} de {addr}")
    if message == 'notes':
        await get_note()
    elif message == 'menu':
        await send_menu()
    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    # addr = server.sockets[0].getsockname()
    # print(f'Serveur socket en écoute à {addr}')
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    dotenv.load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    SERVER_GEII = int(os.getenv("SERVER_GEII"))
    CHANNEL_NOTE = int(os.getenv("CHANNEL_NOTE"))
    CHANNEL_CROUS = int(os.getenv("CHANNEL_CROUS"))
    HOST = str(os.getenv("HOST"))
    PORT = int(os.getenv("PORT"))
    # isntance discord
    intents = discord.Intents.default()
    bot = discord.Client(intents=intents)
    # Exécution du serveur socket et du bot dans la même boucle d'événements
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(bot.start(DISCORD_TOKEN))
    loop.run_forever()
