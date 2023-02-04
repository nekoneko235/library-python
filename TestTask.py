import sys
import task
import unittest
from io import StringIO

class TestClass(unittest.TestCase):
    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        task.solver()
        sys.stdout.seek(0)
        output = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(output.strip(), expected)

    def test_Sample_Input_1(self):
        input = """2"""
        expected = """14"""
        self.assertIO(input, expected)

    def test_Sample_Input_2(self):
        input = """10"""
        expected = """1110"""
        self.assertIO(input, expected)

if __name__ == "__main__":
    unittest.main()
