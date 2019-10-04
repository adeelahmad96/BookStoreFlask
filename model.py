from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    author = db.Column(db.String(20))
    price = db.Column(db.Integer)
    image = db.Column(db.String(100))

    def __init__(self, id, name, author, price , image):
        self.id = id
        self.name = name
        self.author = author
        self.price = price
        self.image = image