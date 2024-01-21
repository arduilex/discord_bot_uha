# Discord Bot UHA

A personal bot discord that sends **new class notes** and meals from the **Crous restaurant**. 

## Description
- Scrap data every 10min from [UHA notes](https://notes.iutmulhouse.uha.fr/) after logging in. Compare with the previous notes database and if a new note is detected, send it in an embled message to a specific Discord channel. More details on how scraping IUT notes [here](./uha_scraping_wiki.MD)
- Scrap data every day at 8am from [Crous Restaurant](https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2). Send the meal into a embled message to a specific Discord channel.


## Getting Started

### 1. Clone the repository
Clone the repository
```
git clone https://github.com/arduilex/discord_bot_uha.git
```
On Linux you have to create a virtual environement for Python :
```bash
cd discord_bot_uha
python -m venv .venv
source .venv/bin/activate
``` 
### 2. Install dependencies
```bash
pip isntall -r requirements.txt
```
`requirements.txt` include :
* [Discord.py](https://discordpy.readthedocs.io/) for the bot
* [Selenium](https://selenium-python.readthedocs.io/) for the scraping

### 3. Setup environment variable

Rename `.env.example` in `.env` and add your UHA **login**, Discord **channel ID** etc.

### 4. Choose your browser
Depending on what browser you have installed on your pc, you have to edit `src/scraping/selenium_driver.py`.  
By defaut it's already setup for Chromium. If you use Firefox, simply comment and uncomment the appropriate line.

### 5. Executing program

In your terminal, at the root of your local repository run the following programs :
- Run Discord bot
```
python src/main_bot.py &
```
`main_bot.py` communicate with other main trough socket. (See `HOST` and `PORT` in `.env`)
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

## Versions

* v1.0
    * Split notes and crous in two distinct programms.
* v0.2
    * Add scraping for Crous Mulhouse Restaurant
* legacy
    * You can find my very old version here, it works with Java Script, the process is very crappy.

## License

This project is licensed under no License so feel free to steal my work :)
