import unittest
from age import categorize_by_age

class TestIsChild(unittest.TestCase):
    def test_child_age(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")
                print("\n", age, "is considered as a child.")

class TestIsAdolescent(unittest.TestCase):
    def test_adolescent_age(self):
        for age in range(10, 19):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adolescent")
                print("\n", age, "is considered as an adolescent.")

class TestIsAdult(unittest.TestCase):
    def test_adult_age(self):
        for age in range(19, 66):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")
                print("\n", age, "is considered as an adult.")

if __name__ == "__main__":
    unittest.main(verbosity=2)