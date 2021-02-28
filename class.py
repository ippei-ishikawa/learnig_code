class Player:
  def __init__(self, job):
    self.job = job

  def attack(self, enemy):
    print( self.job + "は" + enemy + "を攻撃した")

player = Player("勇者")
player.attack("スライム")