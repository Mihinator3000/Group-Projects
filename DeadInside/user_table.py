import sqlite3


class UserTable:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `Users` WHERE `status_of_subscription` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `Users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status=True):
        with self.connection:
            return self.cursor.execute("INSERT INTO `Users` (`user_id`, `status_of_subscription`) VALUES (?,?)", (user_id, status))

    def update_subscription(self, user_id, status):
        return self.cursor.execute("UPDATE `Users` SET `status_of_subscription` = ? WHERE `user_id` = ?", (status, user_id))

    def get_admin(self, status=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `Users` WHERE `admin` = ?", (status,)).fetchall()

    def find_user(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `Users` WHERE `user_id` = ?", (user_id,)).fetchall()


    def close(self):
        self.connection.close()
