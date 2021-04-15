import user_table
import film_table

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
print(user_data.user_count())
print("diversion\n")

search = film_data.film_get_lev("Гена")
if bool(len(search)):
    for s in search:
        print(s[1])
else:
    print("Nothing found")

find_id = film_data.get_film_id("Гена с чебурашкой купили")
if find_id is None:
    print("Nothing found")
else:
    print(find_id[0], find_id[1])

film_data.delete_by_id(15)
