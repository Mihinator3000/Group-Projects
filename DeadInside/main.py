import user_table
import film_table

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

user_data = user_table.UserTable('database.db')
user_data.add_subscriber("dyadya2")
admins = user_data.get_admin("dyadya")
person = user_data.find_user("dyadya")
for i in range(4):
    print(person[i])
film_data = film_table.FilmTable('film_database.db')
film = film_data.all_films_by_name_rus()
for i in film:
    print(i[1])
film_data.add_film_by_name("rur")
print("diversion\n")

search = film_data.film_get_lev("Гена")
if bool(len(search)):
    for s in search:
        print(s[1])
else:
    print("Nothing found")
