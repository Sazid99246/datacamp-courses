import unittest


def is_prime(num):
    if num == 1:
        return False
    up_limit = int(math.sqrt(num)) + 1
    for i in range(2, up_limit):
        if num % i == 0:
            return False
    return True


class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(17), True)

    def test_is_prime(self):
        self.assertEqual(is_prime(6), False)

    def test_is_prime(self):
        self.assertEqual(is_prime(1), False)
