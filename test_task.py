import sys
import unittest
from io import StringIO

from task import solver


class TestTask(unittest.TestCase):
    def test_sample_input_1(self):
        input = """2"""
        expected = """4"""
        self.assertIO(input, expected)

    def test_sample_input_2(self):
        input = """10"""
        expected = """100"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        solver()
        sys.stdout.seek(0)
        output = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(output.strip(), expected)


if __name__ == "__main__":
    unittest.main()
