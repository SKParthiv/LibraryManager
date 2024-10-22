class Book:

  def __init__(self, title, author, genre, pages, price, synopsis, id):
    self.title = title
    self.author = author
    self.genre = genre
    self.pages = pages
    self.price = price
    self.synopsis = synopsis
    self.id = id
    self.issuer = ''
    self.issue_date = ''
    self.due_date = ''
    self.status = ''
    self.due_amount = ''
