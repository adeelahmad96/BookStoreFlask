from app import app , render_template , request , redirect
from model import Book , db

@app.route("/")
def home():
	return render_template("home.html" , books = Book.query.all())

@app.route("/books")
def books():
	return render_template("books.html" , books = Book.query.all())

@app.route("/book/<int:id>")
def book(id):
	return render_template("book.html" , book = Book.query.filter_by(id = id).first())

@app.route("/add" , methods = ['GET' , 'POST'])
def add():
	if request.method == 'GET':
		return render_template("form.html")
	else:
		book = Book(request.form['id'] , request.form['name'], request.form['author'] , request.form['price'] , request.form['image'])
		db.session.add(book)
		db.session.commit()
		return redirect('/')