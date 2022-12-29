from tinydb import Query, TinyDB

db = TinyDB("contact-book.json")
db.default_table_name = "contact-book"
ContactQuery = Query()
