class Book:

	def __init__(self,title,author,pages):
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):
		return f"Книга: {title}; {author}; {pages}"