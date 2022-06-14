from demo.ten_thousand.game_logic import GameLogic

class Game:
    def __init__(self):
        pass

    def play(self, roller=GameLogic.roll_dice):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_answer = input('> ')
        if user_answer == 'n':
            print('OK. Maybe another time')
        else:
            print('Starting round 1')
            print('Rolling 6 dice...')
            new_roller = roller(6)
            formatted_roller = ' '.join([str(i) for i in new_roller])
            print(f'*** {formatted_roller} ***')
            print('Enter dice to keep, or (q)uit:')
            user_answer = input('> ')
            print('Thanks for playing. You earned 0 points')


if __name__ == '__main__':
    game = Game()
    game.play()