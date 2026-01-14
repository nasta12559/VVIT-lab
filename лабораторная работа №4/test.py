import unittest
import my_module
from mypackage import multiply, shout

class TestLab4(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_module.add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_shout(self):
        self.assertEqual(shout("hello"), "HELLO!")

if __name__ == "__main__":
    unittest.main()
