import unittest

from core import SmartLambda


class TestSmartLambda(unittest.TestCase):
    def testNoParameter(self):
        s_lambda = SmartLambda(lambda: 1)
        self.assertEqual(1, s_lambda(), "SmartLambda return value doesn't match!")

    def testPositionalParameter(self):
        s_lambda = SmartLambda(lambda x: x)
        self.assertEqual(1, s_lambda(1), "SmartLambda return value doesn't match!")

    def testKeywordParameter(self):
        s_lambda = SmartLambda(lambda x = 0: x)
        self.assertEqual(1, s_lambda(x = 1), "")
