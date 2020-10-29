import mysql.connector

MyDb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="mydatabase"
)
print(MyDb)
#Membuat database
mycursor = MyDb.cursor()
#Jalankan Perintah untuk membuat database
#mycursor.execute("CREATE DATABASE mydatabase")
#Cek adanya database
"""
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
"""
#membuat tabel customer 
#yang berisikan name dan address
#mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")
#view table customer yang ada didalam database
"""
mycursor.execute("SHOW TABLES")
for tbl in mycursor:
    print(tbl)
"""
#menambahkan ID sebagai primary key dengan perintah ALTER
#ID menggunakan AUTO_INCREMENT 
"""
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
"""
#memasukkan data kedalam tabel customers
#gunakan perintah INSERT INTO
"""
sql_insert = "INSERT INTO customers (name, address) VALUES(%s,%s)"
sql_value = [
    ("Mario", "Kubu Km 31"),
    ("Jon", "Simpang Kanan"),
    ("Putri", "Binjai"),
    ("Riska", "Binjai"),
    ("Dedek", "Sawit Seberang"),
    ("Tazri", "Gumit")
]
mycursor.executemany(sql_insert, sql_value)
MyDb.commit()
print(mycursor.rowcount, "value dimasukkan.")
"""

#sedikit note untuk insert data silahkan dibaca dibawah
"""
Sedikit Note 
Perintah executemany digunakan untuk memasukan data banyak
Perintah execeute digunakan untuk memasukan satu data saja
"""
#sangat penting untuk mengingat perbedaan diatas!!

#Select dari table Customers
#variabel View berguna untuk membuat view
#result menampilkan isi table
"""
mycursor.execute("SELECT * FROM customers")
view = mycursor.fetchall()

for result in view:
    print(result)
"""
#Menggunakan perintah where untuk melakukan search
sql_where="SELECT * FROM customers WHERE address = 'Binjai'"
mycursor.execute(sql_where)
where_result = mycursor.fetchall()

for view_result in where_result:
    print(view_result)