print("Hello Library")
class Library:
  def __init__(self, no_of_books, no_of_shelves, no_of_floors):
    self.no_of_books = no_of_books
    self.no_of_shelves = no_of_shelves
    self.no_of_floors = no_of_shelves
    if no_of_floors >= 3 and no_of_shelves > 10000:
      self.scale = "Large"
    elif no_of_floors > 1 and no_of_shelves > 1000:
      self.scale = "Medium"
    elif no_of_floors == 1 and no_of_shelves > 100:
      self.scale = "Small"
    else:
      self.scale = "Not a Library"