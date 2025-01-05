from game import Game
from hero import Hero

print('Добро пожаловать в игру "Битва героев"!')
name = input('Введи своё имя, герой! ')
hero = Hero(name or 'Безымянный герой')
print(f'Благодарю, {name}!')
name = input('Тебе противостоять будет компьютер. Как его назвать? ')
computer = Hero(name or 'Комп')
game = Game(hero, computer)
game.start()