from main.hello import hello
import unittest


class TestHello(unittest.TestCase):
    def test_hello(self) -> None:
        self.assertEqual("Hello World!", hello())


if __name__ == "__main__":
    unittest.main()
