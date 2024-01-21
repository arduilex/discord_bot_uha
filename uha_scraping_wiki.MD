# UHA Scraping Wiki


## How it works
The scraping is very simple, we just have to POST a php request and we get a JSON file with the full page data inside /o

Let's take a look at how find this request url 

1. Go to https://notes.iutmulhouse.uha.fr/ in your favorite browser, you must login.
2. Open the inspector (`ctrl+maj+i` or `F12`)
3. Go to Network tab 
4. Clic on an other semester i.e "Semestre 1"
5. Watch out the inspector, there must be 2 new `POST`
6. In `File` column, double click on `data.php?q=relevéEtudiant&Semestre=***`
7. You got it ! the number in `***` is the value of `php_request` you have to put in `.env` ;)


