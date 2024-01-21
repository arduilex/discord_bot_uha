import discord, os, dotenv
from datetime import datetime

# Charge les variables d'environnement à partir du fichier .env
dotenv.load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Création du client bot
intents = discord.Intents.default()
bot = discord.Client(intents=intents)

# Événement qui se produit lorsque le bot est prêt


@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')
    await send_menu()

# Fonction pour envoyer un message "testing" dans un salon spécifique d'un serveur spécifique


async def send_menu():
    server_id = 1079355386953482281  # ID du serveur
    channel_id = 1079787813794492467  # ID du salon
    guild = bot.get_guild(server_id)
    channel = guild.get_channel(channel_id)
    # Création de l'objet Embed
    crousEmbed = discord.Embed(color=0x004996, title='Note IUT Mulhouse',
                               url='https://notes.iutmulhouse.uha.fr/')
    crousEmbed.set_author(name='Alerte à la note !!!',
                          icon_url='https://i.imgur.com/sI7EssK.png')
    crousEmbed.set_thumbnail(url='https://i.imgflip.com/6bbwfy.jpg')

    # Supposons que new_note est un objet avec les attributs appropriés
    crousEmbed.add_field(name='hello', value='hello')
    crousEmbed.add_field(name='Coef', value='hello', inline=False)
    crousEmbed.add_field(name='Date', value='hello', inline=True)

    crousEmbed.add_field(name='Minimum', value='hello', inline=True)
    crousEmbed.add_field(name='Moyenne', value='hello', inline=True)
    crousEmbed.add_field(name='Maximum', value='hello', inline=False)

    # Remplacez 'picture_linker(moy)' par le lien réel de l'image
    crousEmbed.set_image(url='https://i.imgur.com/1AUc8m7.jpg')
    crousEmbed.set_footer(text='Créé par Alexandre Bader',
                          icon_url='https://i.imgur.com/sUaZ38N.png')
    crousEmbed.timestamp = datetime.now()  # Met à jour le timestamp
    await channel.send(embed=crousEmbed)

# Commande pour appeler la fonction send_testing_message
# send_testing_message()

# Exécutez le bot avec votre token
bot.run(DISCORD_TOKEN)
