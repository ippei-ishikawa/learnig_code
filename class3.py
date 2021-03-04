class Box:
  def __init__(self, item):
    self.item = item

  def open(self):
    print("宝箱を開いた。" + self.item + "を手に入れた。")

# クラスの継承
class JewelryBox(Box):
  def look(self):
    print("宝箱はキラキラと輝いている。")
box = Box("覇者の剣")
box.open()

jewelry_box = JewelryBox("魔法の指輪")
jewelry_box.look()
jewelry_box.open()

print()

class Box2:
  def __init__(self, item):
    self.item = item

  def open(self):
    print("宝箱を開いた。" + self.item + "を手に入れた。")

# クラスの継承
class MagicBox(Box2):
  def look(self):
    print("宝箱は不気味に輝いている。")

# クラスのオーバーライド
  def open(self):
    print("宝箱を開いた。" + self.item + "に襲われた。")

magic_box = MagicBox("ミミック")
magic_box.look()
magic_box.open()

print()
class Player:
  def __init__(self, name):
    self.name = name

  def attack(self, enemy):
    print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
  def attack(self, enemy):
    print(self.name + "は" + enemy + "に炎を放った！")


print("=== パーティーでミミックと戦う ===")
hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard("魔法使い")

party = [hero, warrior, wizard]
for member in party:
    member.attack("ミミック")