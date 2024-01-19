import sqlite3
import math


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
        self.connect.commit()

    def edit_rn(self, new_name):
        self.cursor.execute("UPDATE nicks SET rp_nick = ?", (new_name,))
        self.connect.commit()

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
        return math.ceil(len(lst) / 8)

    def get_page(self, num):
        num -= 1
        lst = self.cursor.execute("SELECT * FROM scores").fetchall()[::-1]

        result = lst[num * 8:num * 8 + 8]
        return result

    def add_score(self, l_nick, r_nick, l_score, r_score):
        self.cursor.execute('''INSERT INTO scores VALUES(?, ?, ?, ?)''', (l_nick, r_nick, l_score, r_score))
        self.connect.commit()

    def delete_scores(self):
        self.cursor.execute('''DELETE FROM scores''')
        self.connect.commit()
