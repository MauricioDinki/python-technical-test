import unittest
from badminton import Player, Game


class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.player = Player('Test Player')

    def test_init_player(self):
        """Test that the player score starts at 0 and field side at None"""
        player = self.player
        self.assertEqual(player.points, 0)
        self.assertEqual(player.sets_won, 0)
        self.assertEqual(player.field_side, None)

    def test_player_name(self):
        """Test that the given name saves correctly"""
        player_name = 'Michael'
        player = Player(player_name)
        self.assertEqual(player.name, player_name)

    def test_add_point(self):
        """Test that the method add point add just 1 point to the player score"""
        actual_points = self.player.points
        self.player.add_point()
        self.assertEqual(self.player.points, actual_points + 1)

    def test_change_field_side_right(self):
        """Test that the field side change from right to left"""
        self.player.field_side = 'Right'
        self.player.change_field_side()
        self.assertEqual(self.player.field_side, 'Left')

    def test_change_field_side_left(self):
        """Test that the field side change from left to right"""
        self.player.field_side = 'Left'
        self.player.change_field_side()
        self.assertEqual(self.player.field_side, 'Right')


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game(
            player_1=Player('Player 1'),
            player_2=Player('Player 2'),
        )
        self.game.start()

    def test_game_start(self):
        """Test at the game starts both player have a different field side"""
        game = Game(
            player_1=Player('Player 1'),
            player_2=Player('Player 2'),
        )
        game.start()
        self.assertNotEqual(game.player_1.field_side, game.player_2.field_side)

    def test_check_set(self):
        """Test that when a player reaches the set points, the set information is saved"""
        # Game variables
        set_points = 3
        match_points = 2
        game = self.game
        # Assign Scores
        game.player_1.points = 3  # Player 1 Won the game
        game.player_2.points = 2
        game.check_set(set_points, match_points)
        self.assertEqual(len(game.sets), 1)


if __name__ == '__main__':
    unittest.main()
