import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

sql = '''CREATE TABLE "Inventory" (
    "id"    INTEGER NOT NULL,
    "kategori"  VARCHAR(12) NOT NULL,
    "nama_produk"   VARCHAR(25) NOT NULL,
    "seri"  VARCHAR(20) NOT NULL,
    "stok"  INTEGER NOT NULL,
    "terjual"   INTEGER NOT NULL,
    "harga" INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
)'''

cur.execute(sql)
conn.commit()
conn.close()
