class Player:
  def attack(self, enemy):
    print( "戦士は" + enemy + "を攻撃した")

player = Player()
player.attack("スライム")