#membuat apps sederhana menggunakan konsep OOP
#membuat apps untuk management database pegawai
#database pegawai berisikan id,nama,gaji,posisi

import mysql.connector

pegawai_db = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="db_pegawai"
)
print(pegawai_db)
#buat variabel untuk menjadi selector di database
selector=pegawai_db.cursor()
#membuat database db_pegawai dan table tbl_pegawai
"""
selector.execute("CREATE DATABASE db_pegawai")
"""
#Cek database
"""
selector.execute("SHOW DATABASES")
for db in selector:
    print(db)
"""
#Membuat tabel tbl_pegawai dan membuat view untuk tbl_pegawai
"""
selector.execute("CREATE TABLE tbl_pegawai (id INT AUTO_INCREMENT PRIMARY KEY,nama VARCHAR(255),gaji FLOAT,posisi VARCHAR(255))")
selector.execute("SHOW TABLES")
for tbl in selector:
    print(tbl)
"""
#Insert data kedalam tbl_pegawai
sql_insert = "INSERT INTO tbl_pegawai (nama, gaji, posisi) VALUE(%s, %s, %s)"
val_insert = ('Denny', 5000000,'admin')
#Execute dan Commit kedalam tbl_pegawai
selector.execute(sql_insert, val_insert)
#Commit
pegawai_db.commit()
print("Data berhasil disimpan, ID: ",selector.lastrowid) 