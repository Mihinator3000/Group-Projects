import user_table
import film_table

film_data = film_table.FilmTable('film_database.db')
film_data.change_name_rus(15, "ъуъ")
film_data.close()
