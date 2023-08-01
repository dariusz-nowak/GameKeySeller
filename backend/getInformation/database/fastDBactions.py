from sqlite3 import connect

connection = connect("backend/database/sql.db")
cursor = connection.cursor()

# connection.execute("DROP TABLE games")
# connection.execute("DROP TABLE games_to_repair")
# connection.execute("DROP TABLE adverts")
# connection.execute("DROP TABLE sale")
# connection.execute("DELETE FROM sqlite_sequence")

# connection.execute("CREATE TABLE games (id integer primary key AUTOINCREMENT, title text, old_price float, current_price float, store text, status text, time_created DATETIME, time_modyfied DATETIME)")
# connection.execute("CREATE TABLE games_to_repair (id integer primary key AUTOINCREMENT, title text)")
# connection.execute("CREATE TABLE adverts (id integer primary key AUTOINCREMENT, title text, image text, price float, url text)")
# connection.execute("CREATE TABLE sale (id integer primary key AUTOINCREMENT, title text, buy_page text, buy_price float, sell_price float, platform text, time_created DATETIME, time_modyfied DATETIME)")
# connection.commit()

# cursor.execute("INSERT INTO games VALUES(null, 'WATAFAK', 10.01, 4.99, 'store', 'new', strftime('%Y-%m-%d %H-%M-%S','now'), strftime('%Y-%m-%d %H-%M-%S','now'))")
# cursor.execute("INSERT INTO games VALUES(null, 'WATAFAK', 10.01, 4.99, 'store', 'new', strftime('%Y-%m-%d %H-%M-%S','now'), strftime('%Y-%m-%d %H-%M-%S','now'))")
# connection.commit()

# cursor.execute(f"UPDATE games SET old_price = 176.43, current_price = 10.03, time_modyfied = strftime('%Y-%m-%d %H-%M-%S','now') WHERE id = 1")
# cursor.execute(f"UPDATE games SET old_price = 205.74, current_price = 30.01, time_modyfied = strftime('%Y-%m-%d %H-%M-%S','now') WHERE id = 2")
# cursor.execute(f"UPDATE games SET title = 'WATAFAK' WHERE id = 9")
# cursor.execute(f"UPDATE games SET title = 'WATAFAK' WHERE id = 10")
# connection.commit()

# cursor.execute("DELETE FROM games WHERE id = 72")
# cursor.execute("DELETE FROM games WHERE id = 73")
# connection.commit()

