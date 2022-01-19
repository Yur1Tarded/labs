class enemy_mobs:

    def agreccion(self):
        print('ahrrrr')

class creeper(enemy_mobs):

    def __init__(self):
        self.hp = 20
        self.damage = 25

    def attacc(self, other):
        print('shhh... BOOM!')
        other.hp -= 20
        self.hp -= 20
        if other.hp > 0:
            print('creeper dead \nplayer still alive')
        else:
            print('creeper dead \nplayer dead')

class skeleton(enemy_mobs):

    def __init__(self):
        self.hp = 20
        self.damage = 5

    def attacc(self, other):
        print('*sound on arrow*')
        if self.damage > other.damage and self.hp >= other.hp:
            print('player killed by a skeleton')

class zombie(enemy_mobs):

    def __init__(self):
        self.hp = 25
        self.damage = 4

    def attacc(self, other):
        if self.damage > other.damage and self.hp >= other.hp:
            print('arhhh! *happily*')
        else:
            print('arhhh! *sadly*')
    def attaccvil(self, other):
        print('ahhhr... vilagerrrrr \n*villager becomes zombie*')

class ifrit(enemy_mobs):

    def __init__(self):
        self.hp = 30
        self. damage = 7

    def fireball(self, other):
        other.hp -= self.damage
        print('Fireball!!!', 'player hp now ->', other.hp)

class peaceful:

    def lifestyle(self):
        print('I do not attack, I only defend!')

class steve(peaceful):

    def __init__(self):
        self.hp = 20
        self.damage = 1

class steve_pro(peaceful):

    def __init__(self):
        self.hp = 50
        self. damage = 40

class villager(peaceful):

    def __init__(self):
        self.hp = 10
        self.damage = 0

enemy1 = creeper()
enemy2 = skeleton()
enemy3 = zombie()
enemy4 = ifrit()
player = steve()
player2 = steve_pro()
peaceful_mob = villager()

print(enemy1.attacc(player2))
print(enemy4.fireball(player2))
print(enemy4.agreccion())
print(enemy3.attaccvil(peaceful_mob))
print(enemy2.attacc(player))
print(player.lifestyle())