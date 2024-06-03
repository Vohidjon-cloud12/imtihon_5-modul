import psycopg2
import time
import requests
import threading
from typing import Optional
from contextlib import contextmanager


# 1-masala

# # avvalo localhost dagi n47 nomli database bilan Pycharm o'rtasida aloqa ornatib olamiz:
# conn = psycopg2.connect(dbname='n47',
#                         user='postgres',
#                         password='123',
#                         host='localhost',
#                         port=5432)
#
# cur = conn.cursor()
#
#
# # psql da Product nomli table hosil qilinishi uchun  pythonda quyidagicha query code yozamiz:
# create_table_query = '''CREATE TABLE IF NOT EXISTS product
#           (id serial PRIMARY KEY     NOT NULL,
#            name           VARCHAR(80)    NOT NULL,
#            price           decimal NOT NULL,
#            color         VARCHAR(80)    NOT NULL,
#            image        VARCHAR(255)    NOT NULL); '''
#
# cur.execute(create_table_query)
# conn.commit()
# print("Table created successfully in PostgreSQL ")
#


# 2-masala
# def insert_product():
#     """Product jadvaliga malumotlarni qoshuvchi funksiya"""
#     name = input("Enter Product Name: ")
#     price = input("Enter Product Price: ")
#     color = input("Enter Product Color: ")
#     image = input("Enter Product Image: ")
#     # Products jadvaliga ma'lumotlarni kiritish
#     cur.execute("""
#        INSERT INTO product (name, price,color,image)
#         VALUES (%s, %s, %s, %s)
#     """, (name, price, color, image))
#     conn.commit()
# insert_product()
#
# #
# def select_data():
#     """ product jadvalidagi barcha ma'lumotlarni tanlash"""
#     cur.execute("SELECT * FROM product")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
# select_data()
#
# #
# def select_data_from_input():
#     """ inputdan id olib, usha id malumotlarini bazadan chaqirish:"""
#     id = input("Mahsulot IDsi: ")
#     cur.execute("SELECT * FROM product WHERE id = %s", (id,))
#     row = cur.fetchone()
#     print(row)
# # select_data_from_input()
# #
# #
# #
# def update_data():
#         """Jadval malumotlarini, input orqali yangilaymiz:"""
#
#
# id = input("Yangilash kerak bo'lgan mahsulot id si: ")
# name = input("Yangi mahsulot nomini kiriting: ")
#
# cur.execute("""
#       UPDATE product
#       SET name = %s
#       WHERE id = %s
#       """, (name, id))
# conn.commit()
# print('UPDATED SECSESFULLY!!! ')
# update_data()
#
#
# #
# def delete_data():
#     """jadval malumotlarini o'chirish:"""
#     id = input("O'chirish kerak bo'lgan mahsulot IDsi: ")
#
#     # Products jadvalidagi ma'lumotni o'chirish
#     cur.execute("""
#     DELETE FROM product
#     WHERE id = %s
#     """,
#                 (id,))
#     conn.commit()
#     print('deleted secsesfully!!!')
#
# delete_data()

# 3-masala

# class Alphabet:
#     def __init__(self):
#         self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index < len(self.letters):
#             letter = self.letters[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
# alphabet = Alphabet()
# for letter in alphabet:
#     print(letter)
#
# 4-masala
# def print_numbers():
#     for i in range(1,5):
#         print(i)
#         time.sleep(1)
#
# def print_letters():
#     for i in ("ABCDE"):
#         print(i)
#         time.sleep(1)
#
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Done")
#
#
##5-masala

 # (id serial PRIMARY KEY     NOT NULL,
#            name           VARCHAR(80)    NOT NULL,
#            price           decimal NOT NULL,
#            color         VARCHAR(80)    NOT NULL,
#            image        VARCHAR(255)    NOT NULL); '''
# class Product:
#         def __init__(self,
#                      name: str,
#                      price: Optional[float] = None,
#                      color: Optional[str] = None,
#                      image: Optional[str] = None,
#
#                      ):
#
#             self.name =name
#             self.price = price
#             self.color = color
#             self.image = image
#
#         # yaratilgan class obyektlarimiz(user larni) bazada saqlash uchun classga save() metodini qoshamiz:
#         def save(self):
#             insert_product_obj = '''insert into product (name,price,color,image) values (%s,%s,%s,%s);'''
#             data = (self.name, self.price, self.color, self.image)
#             cur.execute(insert_product_obj, data)
#             conn.commit()
#
# product1 = Product('chery',10000,'red','www.olcha.uz')
# product1.save()

# 6-masala
# class DbConnect:
#     def __init__(self, dbname, user, password, host='localhost', port=5432):
#         self.dbname = dbname
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             dbname=self.dbname,
#             user=self.user,
#             password=self.password,
#             host=self.host,
#             port=self.port
#         )
#         self.cur = self.conn.cursor()
#         return self.conn, self.cur
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.cur.close()
#         self.conn.close()
#         if exc_type:
#             raise
#
# # Context Managerdan foydalanish misoli:
# if __name__ == "__main__":
#     conn_params = {
#         'dbname': 'n47',
#         'user': 'postgres',
#         'password': '123',
#         'host': 'localhost',
#         'port': 5432
#     }
#
#     with DbConnect(**conn_params) as (conn, cur):
#         cur.execute("SELECT version();")
#         print(cur.fetchone())
# 7-masala
from contextlib import contextmanager

# DbConnect Context Manager'ni yaratish
# class DbConnect:
#     def init(self, dbname, user, password, host='localhost', port=5432):
#         self.dbname = dbname
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#
#     def enter(self):
#         self.conn = psycopg2.connect(
#             dbname=self.dbname,
#             user=self.user,
#             password=self.password,
#             host=self.host,
#             port=self.port
#         )
#         self.cur = self.conn.cursor()
#         return self.conn, self.cur
#
#     def exit(self, exc_type, exc_val, exc_tb):
#         self.cur.close()
#         self.conn.close()
#         if exc_type:
#             raise
#
# # DummyJSON API'dan ma'lumotlarni olish
# def fetch_products():
#     response = requests.get("https://dummyjson.com/products/")
#     response.raise_for_status()  # Agar so'rov muvaffaqiyatsiz bo'lsa, xatoni ko'taradi
#     return response.json()['products']
#
# # Ma'lumotlar bazasida Product jadvalini yaratish va ma'lumotlarni saqlash
# def create_and_insert_products(conn, cur, products):
#     create_table_query = '''
#     CREATE TABLE IF NOT EXISTS Product (
#         id SERIAL PRIMARY KEY,
#         title TEXT NOT NULL,
#         description TEXT,
#         price NUMERIC,
#         discountPercentage NUMERIC,
#         rating NUMERIC,
#         stock INTEGER,
#         brand TEXT,
#         category TEXT,
#         thumbnail TEXT
#     );
#     '''
#     cur.execute(create_table_query)
#     insert_query = '''
#     INSERT INTO Product (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
#     '''
#     for product in products:
#         cur.execute(insert_query, (
#             product['title'],
#             product['description'],
#             product['price'],
#             product['discountPercentage'],
#             product['rating'],
#             product['stock'],
#             product['brand'],
#             product['category'],
#             product['thumbnail']
#         ))
#     conn.commit()
#
# # Asosiy kod
# if __name__ == "__main__":
#     conn_params = {
#         'dbname': 'n47',
#         'user': 'postgres',
#         'password': '123',
#         'host': 'localhost',
#         'port': 5432
#     }
#
#     products = fetch_products()
#
#     with DbConnect(**conn_params) as (conn, cur):
#         create_and_insert_products(conn, cur, products)
#         print("Products have been successfully inserted into the database.")