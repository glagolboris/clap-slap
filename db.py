import sqlite3


class Base:
    def __init__(self):
        self.connect = sqlite3.connect('users.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS scores(
        left_player TEXT, right_player TEXT, l_score bigint, r_score bigint)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS nicks(
        lp_nick TEXT, rp_nick TEXT)""")
        if len(self.cursor.execute("SELECT * FROM nicks").fetchall()) == 0:
            self.cursor.execute('INSERT INTO nicks VALUES ("Игрок 1", "Игрок 2")')
        self.connect.commit()


    def edit_ln(self, new_name):
        self.cursor.execute("UPDATE nicks SET lp_nick = ?", (new_name,))

    def edit_rn(self, new_name):
        self.cursor.execute("UPDATE nicks SET rp_nick = ?", (new_name,))

    def get_ln(self):
        lst = self.cursor.execute("SELECT lp_nick FROM nicks").fetchall()
        result = lst[0][0]
        self.connect.commit()
        return result

    def get_rn(self):
        lst = self.cursor.execute("SELECT rp_nick FROM nicks").fetchall()
        result = lst[0][0]
        self.connect.commit()
        return result

    def pages_count(self):
        lst = self.cursor.execute("SELECT * FROM scores").fetchall()
        self.connect.commit()
        return len(lst) // 5

    def get_page(self, num):
        num -= 1
        lst = self.cursor.execute("SELECT * FROM scores").fetchall()
        result = lst[num * 5:num * 5 + 5]
        return result