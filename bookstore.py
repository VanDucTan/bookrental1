from pymongo import MongoClient

# Kết nối tới MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["book_rental"]
collection = db["books"]

# Dữ liệu sách
books_data = [
    {"name": "Harry Potter", "author": "J.K. Rowling", "rented": False},
    {"name": "The Lord of the Rings", "author": "J.R.R. Tolkien", "rented": False},
    {"name": "To Kill a Mockingbird", "author": "Harper Lee", "rented": False},
    {"name": "Đắc Nhân Tâm", "author": "Dale Carnegie", "rented": False},
    {"name": "Không bằng đại học", "author": "NhiLe", "rented": False},
    {"name": "Độc thân & Kết hôn?", "author": "NhiLe", "rented": False},
    {"name": "Quẳng gánh lo đi và vui sống", "author": "Dale Carnegie", "rented": False},
]

# Thêm dữ liệu sách vào cơ sở dữ liệu
collection.insert_many(books_data)

print("Dữ liệu sách đã được thêm vào cơ sở dữ liệu.")


