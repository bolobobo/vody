'''
This program is used to crawl the popular movies and tv shows from IMDB website(http://www.imdb.com/chart/moviemeter, http://www.imdb.com/chart/tvmeter).
Then crawl each video description page from the video list and parse the page to get the meta data of each movie or tv show.
Store these data into MySQL database.
'''
from urllib import urlopen
import re
import mysql.connector

def parse_page(page_url, source_type):
    '''parse each description page of each movie and tv show'''
    id = re.match(r'^(.+)(tt\d+)\/$', page_url).group(2)
    rate = 0.0
    title = ""
    year = 2017
    img = ""
    genres = []
    if urlopen(page_url).info().gettype() == 'text/html':
        response = urlopen(page_url)
        html_bytes = response.read()
        html = html_bytes.decode("UTF-8")
        title_exist = re.search("<title>(.*?) \(.*?(\d+).*?\) - IMDb</title>", html, re.DOTALL + re.MULTILINE)
        # title, year
        if title_exist:
            title = title_exist.group(1).strip()
            year = title_exist.group(2)

        # rate
        rate_exist = re.search('<span itemprop="ratingValue">(.*?)</span>', html,re.DOTALL + re.MULTILINE)
        if rate_exist:
            rate = rate_exist.group(1)
        
        # genres
        genres_div = re.search('<h4 class="inline">Genres:</h4>(.*?)</div>', html, re.DOTALL + re.MULTILINE)
        genres = re.findall('<a href="/genre/(.*?)\?', genres_div.group(1), re.DOTALL + re.MULTILINE)

        # img
        img_div = re.search('<div class="poster">(.*?)</div>', html, re.DOTALL + re.MULTILINE)
        img_exist = re.search('(.*)src="(.*?)"(.*)', img_div.group(1))
        max_len = 0
        if img_exist:
            img = img_exist.group(2)
    # store data into SQL database
    store_to_SQL(id, title, year, rate, source_type, page_url, img)
    store_genres_to_SQL(id, genres)

def store_to_SQL(id, title, year, rate, source_type, url, img):
    '''store the meta data of each video into database'''
    conn = mysql.connector.connect(user='root', password='jackie', database='IMDB', use_unicode=True)
    cursor = conn.cursor()
    # insert
    cursor.execute('insert into Movies(source_id, title, year, rate, source_type, url, img) values (%s, %s, %s, %s, %s, %s, %s)', [id, title, year, rate, source_type, url, img])
    conn.commit()
    cursor.close()

def store_genres_to_SQL(id, genres):
    '''store the mapping relationship of each video and its genre'''
    conn = mysql.connector.connect(user='root', password='jackie', database='IMDB', use_unicode=True)
    cursor = conn.cursor()
    # insert
    for genre in genres:
        cursor.execute('insert into Genres(source_id, genre) values (%s, %s)', [id, genre])
    conn.commit()
    cursor.close()

def crawl_list(list_url):
    '''crawl url of description page of each movie or tv show and generate url seeds'''
    url_seeds = []
    if urlopen(list_url).info().gettype() == 'text/html':
        response = urlopen(list_url)
        html_bytes = response.read()
        html = html_bytes.decode("UTF-8")
        # html = html_bytes
        match = re.search('<tbody class="lister-list">(.*?)</tbody>', html, re.DOTALL + re.MULTILINE)
        id_seed = re.findall('<div class="wlb_ribbon" data-tconst="(.*?)" data-recordmetrics="true"></div>', match.group(1))
        for id in id_seed:
            url_seeds.append('http://www.imdb.com/title/' + id + '/')
    return url_seeds

def generate_data(list_url, source_type):
    '''generate the data from IMDB website'''
    url_seeds = crawl_list(list_url)
    for url in url_seeds:
        parse_page(url, source_type)

# call the main function and crawl
if __name__ == "__main__":
    generate_data('http://www.imdb.com/chart/moviemeter', "movie")
    generate_data('http://www.imdb.com/chart/tvmeter', "tv")
    