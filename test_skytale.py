import unittest
from skytale import skytale_encode

class SkytaleTests(unittest.TestCase):
    def test_equal_io(self):
        """the length of the character sequence shouldn't change during operations"""
        self.assertEqual(
            len(skytale_encode("hallo sipgate", 1)),
            len("hallo sipgate")
        )

if __name__ == "__main__":
    unittest.main()