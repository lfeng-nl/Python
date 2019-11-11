import unittest


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownclass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_upper(self):
        print('test_upper')
        self.assertEqual('foo'.upper(), "FOO")

    def test_split(self):
        print('test_split')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])


if __name__ == "__main__":
    unittest.main()
