"""
class User:

  def __init__(self, username: str, age: int):
    self.username = username
    self.age = age

  def __repr__(self):
    return f"User: {self.username}, {self.age} years old"

"""
class Game:
    pass

"""
class User:

  def __init__(self, username: str, age: int, favorite_game: Game):
      self.username = username
      self.age = age
      self.favorite_game = favorite_game

  def __repr__(self):
      return f"User: {self.username}, {self.age} years old, favorite game: {self.favorite_game}"

"""
"""
class User:

  def __init__(self, username: str, age: int):
      self.username = username
      self.age = age

  def __repr__(self):
      return f"User: {self.username}, {self.age} years old"


class Gamer(User):

  def __init__(self, username: str, age: int, favorite_game: Game):
      super().__init__(username, age)
      self.favorite_game = favorite_game
      
  def __repr__(self):
    return f"User: {self.username}, {self.age} years old, favorite game: {self.favorite_game}"
"""