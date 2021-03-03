# プライベートメソッド
class Player:
    def __init__(self, job, weapon):
        self.job = job
        self.__weapon = weapon

    def walk(self):
        print(self.job + "は荒野を歩いていた")
        self.__attack("スライム")

    def __attack(self, enemy):
        print(self.__weapon + "で" + enemy + "を攻撃")


player1 = Player("戦士", "剣")
player1.walk()
