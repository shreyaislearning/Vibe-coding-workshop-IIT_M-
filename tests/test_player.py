# tests/test_player.py
import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        player = Player()
        self.assertEqual(player.name, "")
        self.assertEqual(player.personality_seeds, [])
        self.assertEqual(player.trauma_load, "")
        self.assertEqual(player.energy_levels, "")
        self.assertEqual(player.clarity, 0)
        self.assertEqual(player.confidence, 10)
        self.assertEqual(player.energy, 20)
        self.assertEqual(player.hope, 10)
        self.assertEqual(player.emotional_stability, 5)
        self.assertEqual(player.willpower, 10)
        self.assertEqual(player.self_compassion, 5)

if __name__ == '__main__':
    unittest.main()
