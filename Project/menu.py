from flet import *
import flet

class Option(Card):
  def __init__(self, title : str):
    super().__init__()
    self.title = title

class Menu(UserControl):
  def __init__(self):
    super().__init__()

  def build(self):
    return None

