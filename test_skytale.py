import unittest
from skytale import skytale_encode, skytale_decode

class SkytaleTests(unittest.TestCase):
    def test_equal_io(self):
        """the length of the character sequence shouldn't change during operations"""
        self.assertEqual(
            len(skytale_encode("hallo sipgate", 1)),
            len("hallo sipgate")
        )
        self.assertEqual(
            len(skytale_encode("hallo welt!", 6)),
            len("hwaelllto! ")
        )
        self.assertEqual(
            len(skytale_decode("hallo sipgate", 1)),
            len("hallo sipgate")
        )
        self.assertEqual(
            len(skytale_decode("hallo welt!", 6)),
            len("hwaelllto! ")
        )

    def test_even_seq_encode(self):
        """sequence with diameter 1 should result in the same output"""
        self.assertEqual(
            (skytale_encode("sipgate hacking talents!", 1)),
            "sipgate hacking talents!"
        )
        self.assertEqual(
            (skytale_encode("sipgate hacking talents!", 6)),
            "seili nephgnga tactstka!"
        )

    def test_odd_seq_encode(self):
        """odd sequences shouldn't break the program"""
        self.assertEqual(
            (skytale_encode("hallo welt!", 6)),
            "hwaelllto! "
        )
    
    def test_null_seq_encode(self):
        """no input shouldn't break the program"""
        self.assertEqual(
            (skytale_encode("", 6)),
            ""
        )
    
    def test_numeric_input_encode(self):
        """numeric inputs should be treated as strings"""
        self.assertEqual(
            (skytale_encode(2, 6)),
            "2"
        )

    def test_even_seq_decode(self):
        """sequence with diameter 1 should result in the same output"""
        self.assertEqual(
            (skytale_decode("sipgate hacking talents!", 1)),
            "sipgate hacking talents!"
        )
        self.assertEqual(
            (skytale_decode("seili nephgnga tactstka!", 6)),
            "sipgate hacking talents!"
        )

    def test_odd_seq_decode(self):
        """odd sequences shouldn't break the decoding"""
        self.assertEqual(
            (skytale_decode("hwaelllto! ", 6)),
            "hallo welt!"
        )
    
    def test_null_seq_decode(self):
        """no input shouldn't break the decoding"""
        self.assertEqual(
            (skytale_decode("", 6)),
            ""
        )
    
    def test_numeric_input_decode(self):
        """numeric inputs should be treated as strings"""
        self.assertEqual(
            (skytale_decode(2, 6)),
            "2"
        )

if __name__ == "__main__":
    unittest.main()