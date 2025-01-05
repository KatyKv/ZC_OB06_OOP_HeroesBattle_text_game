from hero import Hero

class Game:
    def __init__(self, player: Hero, comp: Hero):
        self.player = player
        self.comp = comp

    def start(self):
        print(f'Да начнётся битва! {self.player.name} и {self.comp.name}!\n')
        while self.player.is_alive() and self.comp.is_alive():
            health = self.player.attack(self.comp)
            print(f'У компьютера {self.comp.name} осталось {health} жизней.')
            if self.comp.is_alive():
                health = self.comp.attack(self.player)
                print(f'У героя {self.player.name} осталось {health} жизней.')
        if self.player.is_alive():
            print(f'\nИгрок {self.player.name} победил! С победой!!!')
        if self.comp.is_alive():
            print(f'\nСегодня победа на стороне компьютера {self.comp.name}.')

if __name__ == '__main__':
    hero = Hero('Иван')
    computer = Hero('Комп')
    game = Game(hero, computer)
    game.start()