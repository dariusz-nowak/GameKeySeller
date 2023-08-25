from sqlite3 import connect
from time import sleep

connection = connect("backend/database/sql.db")
cursor = connection.cursor()

# connection.execute("DROP TABLE games")
# connection.execute("DROP TABLE purchase_platforms")
connection.execute("DROP TABLE adverts")
connection.execute("DROP TABLE sales")
# connection.execute("DELETE FROM sqlite_sequence")
# connection.execute("DROP TABLE sales_platforms")
# connection.execute("DROP TABLE games_to_repair")

# connection.execute("CREATE TABLE games (id integer primary key AUTOINCREMENT, title text, old_price float, current_price float, store text, status text, time_created DATETIME, time_modyfied DATETIME)")
# connection.execute("CREATE TABLE games_to_repair (id integer primary key AUTOINCREMENT, title text)")
connection.execute("CREATE TABLE adverts (id integer primary key AUTOINCREMENT, olx_id integer, title text, buy_price float, sell_price float, fee float, currency text, buy_platform text, sell_platform text, time_created DATETIME)")
connection.execute("CREATE TABLE sales (id integer primary key AUTOINCREMENT, title text, buy_price float, sell_price float, fee float, currency text, exchange_rate float, buy_platform text, sell_platform text, time_created DATETIME)")
# connection.execute("CREATE TABLE purchase_platforms (id integer primary key AUTOINCREMENT, name text)")
# connection.execute("CREATE TABLE sales_platforms (id integer primary key AUTOINCREMENT, name text)")
connection.commit()

# cursor.execute("INSERT INTO sales VALUES(null, 'game', 100, 150, 10, 'gg.deals', 'olx.pl', strftime('%Y-%m-%d %H:%M:%S','now'))")
# connection.commit()

# cursor.execute("INSERT INTO games VALUES(null, 'WATAFAK', 10.01, 4.99, 'store', 'new', strftime('%Y-%m-%d %H:%M:%S','now'), strftime('%Y-%m-%d %H:%M:%S','now'))")
# connection.commit()

# cursor.execute(f"UPDATE games SET old_price = 176.43, current_price = 10.03, time_modyfied = strftime('%Y-%m-%d %H:%M:%S','now') WHERE id = 1")
# cursor.execute(f"UPDATE games SET old_price = 205.74, current_price = 30.01, time_modyfied = strftime('%Y-%m-%d %H:%M:%S','now') WHERE id = 2")
# cursor.execute(f"UPDATE games SET title = 'WATAFAK' WHERE id = 13")
# cursor.execute(f"UPDATE games SET title = 'WATAFAK' WHERE id = 14")
# connection.commit()

# cursor.execute("INSERT INTO adverts VALUES(null, '1', 'game name 1', 'https://img.freepik.com/darmowe-psd/ikona-google-na-bialym-tle-renderowania-3d-ilustracja_47987-9777.jpg?w=2000', 10.10, 'google.pl')")
# cursor.execute("INSERT INTO adverts VALUES(null, '2', 'looooooong game name 2', 'https://img.freepik.com/darmowe-psd/ikona-google-na-bialym-tle-renderowania-3d-ilustracja_47987-9777.jpg?w=2000', 10.10, 'google.pl')")
# cursor.execute("INSERT INTO adverts VALUES(null, '3', 'game name 3', 'https://img.freepik.com/darmowe-psd/ikona-google-na-bialym-tle-renderowania-3d-ilustracja_47987-9777.jpg?w=2000', 10.10, 'google.pl')")
# cursor.execute("INSERT INTO adverts VALUES(null, '4', 'game name 4', 'https://img.freepik.com/darmowe-psd/ikona-google-na-bialym-tle-renderowania-3d-ilustracja_47987-9777.jpg?w=2000', 10.10, 'google.pl')")
# cursor.execute("INSERT INTO adverts VALUES(null, '5', 'veeeeeeeeeeeeeeeery looooooong game name game name 5', 'https://img.freepik.com/darmowe-psd/ikona-google-na-bialym-tle-renderowania-3d-ilustracja_47987-9777.jpg?w=2000', 10.10, 'google.pl')")
# cursor.execute("INSERT INTO adverts VALUES(null, '6', 'game name 6', 'https://img.freepik.com/darmowe-psd/ikona-google-na-bialym-tle-renderowania-3d-ilustracja_47987-9777.jpg?w=2000', 10.10, 'google.pl')")
# cursor.execute("INSERT INTO adverts VALUES(null, '7', 'game name 7', 'https://img.freepik.com/darmowe-psd/ikona-google-na-bialym-tle-renderowania-3d-ilustracja_47987-9777.jpg?w=2000', 10.10, 'google.pl')")
# connection.commit()

# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 20, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '-3 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 10, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+1 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 150, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+3 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 30, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+4 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 50, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+4 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 40, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+7 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 60, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+10 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 70, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+10 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 30, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+12 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 80, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+22 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 110, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+23 days'))")
# sleep(2)
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 120, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+23 days'))")
# cursor.execute("INSERT INTO sales VALUES(null, 'title', 100, 30, 'platform', strftime('%Y-%m-%d %H:%M:%S','now', '+26 days'))")
# connection.commit()

cursor.execute("DELETE FROM purchase_platforms WHERE name = 'Test'")
# cursor.execute("DELETE FROM games WHERE id = 73")
connection.commit()