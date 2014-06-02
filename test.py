import unittest

from unit import joule2calorie, calorie2joule

class TestEnergy(unittest.TestCase):
    def test_circular(self):
        self.assertEquals(10, joule2calorie(calorie2joule(10)))

    def test_equals(self):
        c = 120
        j = 505
        self.assertEquals(c, joule2calorie(j))
        self.assertEquals(j, calorie2joule(c))

if __name__ == '__main__':
    unittest.main()
