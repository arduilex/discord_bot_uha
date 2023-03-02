# Fapi Bot

A private bot alert when a new note is released in my school  

## Description
Scrap data from https://notes.iutmulhouse.uha.fr/ after logging in. Compare the json data with the previous scrap and if a new note is detected, send an embled message to a discord channel.


## Getting Started

### Dependencies

* Python 3.9
* node js 18.7.0
* module (discord.js, selenium)

### Installing

* clone the repository
* add an .env file to login 

### Executing program

* run the **main.py**
* for testing the bot, run
```
npm start
```

## Help

To see scraping in action, simply delete this line in **scraping.py**
```
options.add_argument('--headless')
```

## Authors

This project was entierly made by me.

[Alexandre BADER](alexandrebader3@gmail.com)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under no License so feel free to steal my work :)

## Acknowledgments

Inspiration, code snippets, etc.
* [selenium](https://selenium-python.readthedocs.io/getting-started.html)
