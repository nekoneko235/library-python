# test_sample.py テストをする側のコード
import unittest
import sample

"""
メソッド 用途 メソッドの種類
setUpClass()    テストクラス全体の前処理 クラスメソッド
tearDownClass() テストクラス全体の後処理 クラスメソッド
setUp()         個別のテストメソッドの前処理 インスタンスメソッド
tearDown()      個別のテストメソッドの後処理 インスタンスメソッド
"""


class TestNumberFuncs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('全体前処理')

    @classmethod
    def tearDownClass(cls):
        print('全体後処理')

    def setUp(self):
        print('テスト前処理')

    def tearDown(self):
        print('テスト後処理')

    def test_add_num(self):
        """
        add_numの単体テスト
        """
        self.assertEqual(7, sample.add_num(3, 4))

    def test_is_positive(self):
        """
        is_numの単体テスト
        """
        self.assertTrue(sample.is_positive(3))
        self.assertFalse(sample.is_positive(0))
        self.assertFalse(sample.is_positive(-1))
