# Discord Bot UHA

A personal bot discord that sends **new class notes** and meals from the **Crous restaurant**. 

## Description
- Scrap data every 10min from [UHA notes](https://notes.iutmulhouse.uha.fr/) after logging in. Compare with the previous notes database and if a new note is detected, send it in an embled message to a specific Discord channel.
- Scrap data every day at 8am from [Crous Restaurant](https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2). Send the meal into a embled message to a specific Discord channel.


## Getting Started

### 1. Clone the repository
* clone the repository
```
git clone https://github.com/arduiles/discord_bot_uha.git
```
* On Linux you have to create a virtual environement for Python :
```bash
cd discord_bot_uha
python -m venv .venv
source .venv/bin/activate
``` 
### 2. Install dependencies
* [Discord.py](https://discordpy.readthedocs.io/en/stable/intro.html#installing) for the bot
- [Selenium](https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium) for the scraping

### 3. Setup login

* Rename `.env.example` in `.env` and add your **uha login** and **Discord channel ID**

### Executing program

In your terminal, at the root of your local repository run the following programs :
- Run Discord bot
```
python src/bot.py &
```
- Run notes scraping
```
python src/main_notes.py &
```
- Run crous meal scraping
```
python src/main_crous.py &
```
`&` run Python in background, you can see process with `ps` and kill it with `kill [process_id]` or `pkill [process_name]` 

## Debug

To see scraping in your computer (not in a server), simply delete this line in **scraping**'s  folder files
```
options.add_argument('--headless')
```

## Authors

This project was entierly made by me.

- e-mail: alexandre@r3tro.fr  
- Discord: `@arduilex`

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under no License so feel free to steal my work :)
