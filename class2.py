class Item:
  tax = 1.08

  def __init__(self, price, quantity):
    self.price = price
    self.quantity = quantity

  def total(self):
    return int(self.price * self.quantity * Item.tax)

potion = Item(50, 6)
total = potion.total()
print("合計金額は" + str(total) + "です")