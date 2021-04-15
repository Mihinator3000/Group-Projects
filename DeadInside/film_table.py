import sqlite3


class FilmTable:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_film(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `Films` WHERE `id` >= 0").fetchall()

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

    def all_films_by_name_rus(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `Films` ORDER BY `film_name_rus`").fetchall()

    def close(self):
        self.connection.close()
