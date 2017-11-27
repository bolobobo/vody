import mysql.connector

class Searcher(object):
    '''create the searcher'''

    def __init__(self):
        '''searcher configuration'''

    def default_display(self):
        '''select the popular movies and tvs from database'''
        conn = mysql.connector.connect(user='root', password='jackie', database='IMDB', use_unicode=True)
        cursor = conn.cursor()
        # get movie
        sql_statement = "select * from Movies where source_type = 'movie' limit 10"
        cursor.execute(sql_statement)
        values = cursor.fetchall()
        conn.commit()
        movies = self.get_JSON("top movies", values)

        # get tv
        sql_statement = "select * from Movies where source_type = 'tv' limit 10"
        cursor.execute(sql_statement)
        values = cursor.fetchall()
        conn.commit()
        tvs = self.get_JSON("top tvs", values)

        cursor.close()
        return movies, tvs

    def search(self, query, field):
        '''Search the database'''
        conn = mysql.connector.connect(user='root', password='jackie', database='IMDB', use_unicode=True)
        cursor = conn.cursor()
        sql_statement = ""
        if field == "Title":
            sql_statement = "select * from Movies where title like '%%%s%%'" % (query)
        if field == "Genre":
            sql_statement = "select * from Movies where source_id in (select source_id from Genres where genre like '%%%s%%')" % (query)
        cursor.execute(sql_statement)
        values = cursor.fetchall()
        # print values
        conn.commit()
        cursor.close()
        return self.get_JSON(query, values)

    def get_JSON(self, query, values):
        '''generate JSON of list of movies or tv shows'''
        result = {}
        result["query"] = query;
        videos = []
        for value in values:
            video = {}
            video["title"] = value[1]
            video["year"] = value[2]
            video["rate"] = value[3]
            video["source_type"] = value[4]
            video["url"] = value[5]
            video["img"] = value[6]
            videos.append(video)
        result["videos"] = videos
        return result

# a test of searching the query "American"
if __name__ == "__main__":
    searcher = Searcher()
    # searcher.search("Thor", "Title")
    searcher.default_display()
 