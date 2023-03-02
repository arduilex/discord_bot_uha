const fs = require('node:fs');
// const path = require('node:path');
const { Client, Events, GatewayIntentBits } = require('discord.js');
const { token } = require('./config.json');
// const { channel } = require('node:diagnostics_channel');
const { EmbedBuilder } = require('discord.js');


const client = new Client({ intents: [GatewayIntentBits.Guilds] });

// client.commands = new Collection();
// const commandsPath = path.join(__dirname, 'commands');
// const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));

// for (const file of commandFiles) {
// 	const filePath = path.join(commandsPath, file);
// 	const command = require(filePath);
// 	client.commands.set(command.data.name, command);
// }

const note_rawdata = fs.readFileSync('../python/new_note.json');
const new_note_list = JSON.parse(note_rawdata);
const picture_rawdata = fs.readFileSync('./picture.json');
const picture = JSON.parse(picture_rawdata);


function picture_linker(moy) {
	if (moy > 14) {
		return picture.nerd;
	}
	else if (moy < 10) {
		return picture.sad;
	}
	else {
		return picture.think;
	}
}
client.once(Events.ClientReady, () => {
	console.log('Ready!');
	for (let i = 0; i < new_note_list.length; i++) {
		const new_note = new_note_list[i];
		const moy = new_note.evaluation.note.moy;
		const exampleEmbed = new EmbedBuilder().setColor(0x004996)
			.setTitle('Note IUT Mulhouse')
			.setURL('https://notes.iutmulhouse.uha.fr/')
			.setAuthor({ name: 'Alerte à la note !!!', iconURL: 'https://i.imgur.com/sI7EssK.png' })
			// .setDescription('Some description here')
			.setThumbnail('https://i.imgflip.com/6bbwfy.jpg')
			.addFields(
				{ name: new_note.matiere, value: new_note.evaluation.titre },
				{ name: 'Coef', value: new_note.evaluation.coef, inline: true },
				{ name: 'Date', value: new_note.evaluation.date, inline: true },
				{ name: '\u200B', value: '\u200B', inline: true },
				{ name: 'Minimum', value: new_note.evaluation.note.min, inline: true },
				{ name: 'Moyenne', value: new_note.evaluation.note.moy, inline: true },
				{ name: 'Maximum', value: new_note.evaluation.note.max, inline: true })
			.setImage(picture_linker(moy))
			.setTimestamp()
			.setFooter({ text: 'Créé par Alexandre Bader', iconURL: 'https://i.imgur.com/sUaZ38N.png' });
		client.channels.cache.get('1079787813794492467').send({ embeds: [exampleEmbed] });
	}
	client.channels.cache.get('1079787813794492467').send('<@&1079789246841368597>');
});

setTimeout(function() {
	process.exit();
}, 10000);

// client.on(Events.InteractionCreate, async interaction => {

// 	if (!interaction.isChatInputCommand()) return;

// 	const command = client.commands.get(interaction.commandName);

// 	if (!command) return;

// 	try {
// 		await command.execute(interaction);

// 	} catch (error) {
// 		console.error(error);
// 		if (interaction.replied || interaction.deferred) {
// 			await interaction.followUp({ content: 'There was an error while executing this command!', ephemeral: true });
// 		} else {
// 			await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
// 		}
// 	}
// });

client.login(token);