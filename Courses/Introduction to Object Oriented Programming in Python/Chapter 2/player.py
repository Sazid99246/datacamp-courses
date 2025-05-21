class Player:
    MAX_POSITION = 10

    def __init__(self, position):
        if position <= Player.MAX_POSITION:
            self.position = position
        else:
            self.position = Player.MAX_POSITION


p1 = Player(9)
p2 = Player(5)

print("MAX_POSITION of p1 and p2 before assignment:")
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

p1.MAX_POSITION = 7

print("MAX_POSITION of p1 and p2 after assignment:")
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)
