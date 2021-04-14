import user_table
import film_table


user_data = user_table.UserTable('database.db')
user_data.add_subscriber("dyadya2")
admins = user_data.get_admin()
for s in admins:
    print(1)
person = user_data.find_user("g")
for p in person:
    print(p[3])