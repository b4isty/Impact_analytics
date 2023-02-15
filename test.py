import unittest
from main import calculate_attend_and_miss


class TestGraduationCeremony(unittest.TestCase):
    def test_calculate_attend_and_miss(self):
        self.assertEqual(calculate_attend_and_miss(5), "14/29")
        self.assertEqual(calculate_attend_and_miss(10), "372/773")


if __name__ == '__main__':
    unittest.main()
