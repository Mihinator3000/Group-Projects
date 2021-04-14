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

    def update_link(self, name_rus, link):
        return self.cursor.execute("UPDATE `Films` SET `link` = ? WHERE `name_rus` = ?", link, name_rus)

    def close(self):
        self.connection.close()
