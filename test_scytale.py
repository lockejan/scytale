import unittest
from scytale import scytale_init

class scytaleTests(unittest.TestCase):
    def test_equal_io_encode(self):
        """the length of the character sequence shouldn't change during encoding"""
        self.assertEqual(
            len(scytale_init("hallo sipgate", 1, 0)),
            len("hallo sipgate")
        )
        self.assertEqual(
            len(scytale_init("hallo welt!", 6, 0)),
            len("hwaelllto! ")
        )

    def test_seq_encode_min(self):
        """sequence with diameter 1 should result in the same output"""
        self.assertEqual(
            (scytale_init("sipgate hacking talents!", 1, 0)),
            "sipgate hacking talents!"
        )
        self.assertEqual(
            (scytale_init("hallo welt!", 1, 0)),
            "hallo welt!"
        )

    def test_even_seq_encode(self):
        """sequence with diameter > 1 should decode seq"""
        self.assertEqual(
            (scytale_init("sipgate hacking talents!", 6, 0)),
            "seili nephgnga tactstka!"
        )
        self.assertEqual(
            (scytale_init("sipgate hacking talents!", 5, 0)),
            "stc niekttp iasghnl!aage"
        )

    def test_odd_seq_encode(self):
        """odd sequences shouldn't break the program and be unrelated to diameter"""
        self.assertEqual(
            (scytale_init("hallo welt!", 6, 0)),
            "hwaelllto! "
        )
        self.assertEqual(
            (scytale_init("hallo welt!", 5, 0)),
            "h !awlellot"
        )

    def test_null_seq_encode(self):
        """no input shouldn't break the program"""
        self.assertEqual(
            (scytale_init("", 6, 0)),
            ""
        )
    
    def test_numeric_input_encode(self):
        """numeric inputs should be treated as strings"""
        self.assertEqual(
            (scytale_init(2, 6, 0)),
            "2"
        )

    def test_equal_io_decode(self):
        """the length of the character sequence shouldn't change during decoding"""        
        self.assertEqual(
            len(scytale_init("hallo sipgate", 1, 1)),
            len("hallo sipgate")
        )
        self.assertEqual(
            len(scytale_init("hallo welt!", 6, 1)),
            len("hwaelllto! ")
        )

    def test_even_seq_decode_min(self):
        """sequence with diameter = 1 should result in the same output"""
        self.assertEqual(
            (scytale_init("sipgate hacking talents!", 1, 1)),
            "sipgate hacking talents!"
        )

    def test_even_seq_decode(self):
        """sequence with diameter > 1 should be decoded as expected"""
        self.assertEqual(
            (scytale_init("seili nephgnga tactstka!", 6, 1)),
            "sipgate hacking talents!"
        )

    def test_odd_seq_decode(self):
        """odd sequences shouldn't break the decoding"""
        self.assertEqual(
            (scytale_init("hwaelllto! ", 6, 1)),
            "hallo welt!"
        )
    
    def test_null_seq_decode(self):
        """no input shouldn't break the decoding"""
        self.assertEqual(
            (scytale_init("", 6, 1)),
            ""
        )
    
    def test_numeric_input_decode(self):
        """numeric inputs should be treated as strings"""
        self.assertEqual(
            (scytale_init(2, 6, 1)),
            "2"
        )

if __name__ == "__main__":
    unittest.main()