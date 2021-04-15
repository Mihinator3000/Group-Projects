import sqlite3
from fuzzywuzzy import fuzz


class FilmTable:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def film_exists(self, name_rus):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `Films` WHERE `name_rus` = ?", (name_rus,)).fetchall()
            return bool(len(result))

    def add_film(self, name_rus, link):
        with self.connection:
            return self.cursor.execute("INSERT INTO `Films` (`film_name_rus`, `link`) VALUES (?,?)", (name_rus, link))
        
    def add_film_by_name(self, name_rus):
        with self.connection:
            return self.cursor.execute("INSERT INTO `Films` (`film_name_rus`) VALUES (?)", (name_rus,))

    def update_link(self, name_rus, link):
        with self.connection:
            return self.cursor.execute("UPDATE `Films` SET `link` = ? WHERE `name_rus` = ?", (link, name_rus))

    def update_link_id(self, id, link):
        with self.connection:
            return self.cursor.execute("UPDATE `Films` SET `link` = ? WHERE `id` = ?", (link, id))

    def find_film(self, film_name):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `Films` WHERE `film_name_rus` = ?", (film_name,)).fetchall()[0]

    def change_name_rus(self, id, new_name):
        with self.connection:
            return self.cursor.execute("UPDATE `Films` SET `film_name_rus` = ? WHERE `id` = ?", (new_name, id))

    def change_genre(self, id, new_genre):
        with self.connection:
            return self.cursor.execute("UPDATE `Films` SET `genre` = ? WHERE `id` = ?", (new_genre, id))

    def change_year(self, id, new_year):
        with self.connection:
            return self.cursor.execute("UPDATE `Films` SET `year` = ? WHERE `id` = ?", (new_year, id))

    def all_films_by_name_rus(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `Films` ORDER BY `film_name_rus`").fetchall()

    def get_film_id(self, name, distance=70):
        with self.connection:
            result = None
            for film in self.cursor.execute("SELECT * FROM `Films`"):
                lev = fuzz.token_sort_ratio(film[1], name)
                if lev > distance:
                    distance = lev
                    result = film
            return result

    def film_get_lev(self, name, distance=70, add_dist=20):
        with self.connection:
            result = []
            res_add = []
            for film in self.cursor.execute("SELECT * FROM `Films`"):
                lev = fuzz.token_sort_ratio(film[1], name)
                if lev > distance:
                    result.append(film)
                elif lev > add_dist:
                    res_add.append(film)
            if not bool(len(result)):
                return res_add
            return result

    def film_count(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `Films`").fetchall()
            return len(result)

    def delete_by_id(self, id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `Films` WHERE `id` = ?", (id,))

    def close(self):
        self.connection.close()
