API for Popular Movies and TV Shows from IMDb website


Description:
---------------------------------------------------------
This application is used to browse through the popular movies and tv shows from IMDB website.
It crawls 100 moives and tv shows and stores them into MySQL database.
It provides search function and you can search the videos by title or genre.


Author:
---------------------------------------------------------
Jiaqi Guan (jg4803@nyu.edu)


Prerequisite:
---------------------------------------------------------
Python
flask
MySQL

Install:
---------------------------------------------------------
* install python-pip
  $ apt-get install python-pip
* intall all the dependency(the requirements.txt is already in this directory)
  $ pip install -r requirements.txt 

Usage:
---------------------------------------------------------
1. Use it in local:
   After installing all the dependency, run the file "webapp.py" in the directory.
   Then open the brower and input "http://127.0.0.1:5000/" to visit this port.
   * search
   You can just put the query on the search blank and select the field for searching and then submit it. 
   Then you will get the results on the results page which you can click each of them to visit the specific page.

2. Use it through http://104.199.158.79:5000/
   You can only search in the website(IMDB) and can get part of the pages in this website.
   get json api use : http://104.199.158.79:5000/api/videos/search?query=<your query>&field=<Title or Genre>
   Eg.http://104.199.158.79:5000/api/videos/search?query=just&field=Title


History:
---------------------------------------------------------
11/26/2017 version 1.0 