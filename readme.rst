Introduction
============
This project was developed just for show off purposes. It starts on given Wikipedia link and does breath lookup until it finds given target.

Assumptions
===========
python 2.7.x is installed

pip is installed

virtualenv is installed

Instalation
===========

1. Clone repo
2. cd wikiparser
3. virtualenv .venv
4. source .venv/bin/activate
5. pip install -r requirements.txt
6. python parse.py <start_article_name> <fishish_article_name>


Example
=======

python parse.py "Zmotoryzowane Odwody Milicji Obywatelskiej" "Józef Stalin"

After a while and lotsa debug messages you should see:


1. Zmotoryzowane Odwody Milicji Obywatelskiej
https://pl.wikipedia.org/wiki/Zmotoryzowane Odwody Milicji Obywatelskiej

2. Polska Rzeczpospolita Ludowa
https://pl.wikipedia.org/wiki/Polska_Rzeczpospolita_Ludowa

3. Józef Stalin
https://pl.wikipedia.org/wiki/J%C3%B3zef_Stalin


