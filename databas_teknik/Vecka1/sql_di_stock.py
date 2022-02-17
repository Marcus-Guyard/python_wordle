import sqlite3

con = sqlite3.connect("di_stock_data.db")
cur = con.cursor()


for row in cur.execute(f"SELECT * FROM di_stock_data where name like '% b'"):
    print(row)
