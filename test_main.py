import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_palindrome_number(self):
        result = self.solution.isPalindrome(121)
        self.assertEqual(result, True, f"Expected True, but got {result}")
        
        result = self.solution.isPalindrome(-121)
        self.assertEqual(result, False, f"Expected False, but got {result}")

        result = self.solution.isPalindrome(10)
        self.assertEqual(result, False, f"Expected True, but got {result}")

        result = self.solution.isPalindrome(9876556789)
        self.assertEqual(result, True, f"Expected False, but got {result}")

if __name__ == '__main__':
    # Test loader and runner
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    result = unittest.TextTestRunner(failfast=False).run(suite)
    
    # Yalnızca testlerin tamamlanmasını ve hata mesajlarını yazdırıyoruz
    if not result.wasSuccessful():
        print("Some tests failed. Here are the details:")
        for failure in result.failures:
            print(failure)
        for error in result.errors:
            print(error)
