import random

class Hero:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other: 'Hero'):
        rnd_attack = random.choice(('miss', 'half' , 'full'))
        if rnd_attack == 'miss':
            print(f'Герой {self.name} промахнулся. Урон не нанесён.')
            return other.health
        elif rnd_attack == 'half':
            other.health -= self.attack_power // 2
            print(f'Герой {self.name} ударил вполсилы. '
                  f'Урон: {self.attack_power // 2}.')
            return other.health
        elif rnd_attack == 'full':
            other.health -= self.attack_power
            print(f'Герой {self.name} ударил противника с силой: '
                  f'{self.attack_power}.')
            return other.health


    def is_alive(self):
        return self.health > 0



