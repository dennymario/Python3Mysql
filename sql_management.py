#membuat apps sederhana menggunakan konsep OOP
#membuat apps untuk management database pegawai
#database pegawai berisikan id,nama,gaji,posisi

import mysql.connector

pegawai_db = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
)
print(pegawai_db)
#buat variabel untuk menjadi selector di database
selector=pegawai_db.cursor()
#membuat database db_pegawai dan table tbl_pegawai
selector.execute("CREATE DATABASE db_pegawai")

