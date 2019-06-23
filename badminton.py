import os
import random

SET_POINTS = 3  # Number of points to won the set
MATCH_POINTS = 2  # Number of sets to won the match

game_continues = True


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.sets_won = 0
        self.field_side = None

    def add_point(self):
        self.points += 1

    def change_field_side(self):
        if self.field_side == 'Left':
            self.field_side = 'Right'
        else:
            self.field_side = 'Left'


class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.sets = []
        self.actual_set = 1

    def check_set(self, set_points, match_points):
        if self.player_1.points == set_points:
            self.player_1.sets_won += 1
            set_won = True
            winner = self.player_1.name
        elif self.player_2.points == set_points:
            self.player_2.sets_won += 1
            set_won = True
            winner = self.player_2.name
        else:
            set_won = False
            winner = None

        if set_won:
            self.player_1.change_field_side()
            self.player_2.change_field_side()
            self.sets.append({
                'set': self.actual_set,
                'player_1': self.player_1.points,
                'player_2': self.player_2.points,
                'winner': winner
            })
            self.player_1.points = 0
            self.player_2.points = 0
            self.actual_set += 1
            self.check_match(match_points)
        else:
            self.get_score()

    def check_match(self, match_points):
        if self.player_1.sets_won == match_points:
            self.finish(self.player_1)
        elif self.player_2.sets_won == match_points:
            self.finish(self.player_2)
        else:
            self.get_sets()

    def finish(self, player):
        self.get_sets()
        print('****************************************')
        print('        ¡MATCH %s won the game! ' % player.name)
        print('****************************************')
        global game_continues
        game_continues = False

    def get_score(self):
        print('****************************************')
        print('              SCORE SET #%i            ' % self.actual_set)
        print('                  %i - %i              ' % (self.player_1.points, self.player_2.points))
        print('****************************************')

    def get_sets(self):
        if self.sets:
            print('****************************************')
            for game_set in self.sets:
                print("       SET #%i: %i - %i (Won %s)" % (
                    game_set['set'],
                    game_set['player_1'],
                    game_set['player_2'],
                    game_set['winner'],
                ))
            print('****************************************')
        else:
            print('****************************************')
            print('              No Sets Won               ')
            print('****************************************')

    def start(self):
        field_sides = ['Left', 'Right']
        choice = random.choice(field_sides)
        field_sides.remove(choice)
        self.player_1.field_side = choice
        self.player_2.field_side = field_sides[0]


def main():
    print('****************************************')
    print('*                                      *')
    print('*         WELCOME TO THE GAME          *')
    print('*                                      *')
    print('****************************************')
    name_1 = input('Name of Player 1: ')
    name_2 = input('Name of Player 2: ')
    player_1 = Player(name_1)
    player_2 = Player(name_2)
    game = Game(player_1, player_2)
    game.start()
    while game_continues:
        print('Which player marked a point?')
        print('Press 1 for %s (%s side)' % (player_1.name, player_1.field_side))
        print('Press 2 for %s (%s side)' % (player_2.name, player_2.field_side))
        print('Press 3 to check the actual score')
        print('Press another key to check global score')
        choice = input('Choice: ')
        os.system('clear')
        if choice == '1':
            player_1.add_point()
            game.check_set(SET_POINTS, MATCH_POINTS)
        elif choice == '2':
            player_2.add_point()
            game.check_set(SET_POINTS, MATCH_POINTS)
        elif choice == '3':
            game.get_score()
        else:
            game.get_sets()


if __name__ == '__main__':
    main()
