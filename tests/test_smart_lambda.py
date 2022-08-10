import unittest
from util import test

from core import SmartLambda


class TestSmartLambda(unittest.TestCase):
    @test("SMART-LAMBDA CALL NO-PARAMETER", parameter= range(0, 5))
    def testNoParameter(self, val):
        print(f"\t Validate: (lambda: {val}) -> {val}")
        s_lambda = SmartLambda(lambda: val)
        self.assertEqual(val, s_lambda(), "SmartLambda return value doesn't match!")

    @test("SMART-LAMBDA CALL POSITIONAL-PARAMETER", parameter= range(0, 5))
    def testPositionalParameter(self, val):
        print(f"\t Validate: (lambda x: x) -> {val} with x = {val}")
        s_lambda = SmartLambda(lambda x: x)
        self.assertEqual(val, s_lambda(val), "SmartLambda return value doesn't match!")

    @test("SMART-LAMBDA CALL KEYWORD-PARAMETER", parameter= range(0, 5))
    def testKeywordParameter(self, val):
        print(f"\t Validate: (lambda x = 0: x) -> {val} with x = {val}")
        s_lambda = SmartLambda(lambda x = 0: x)
        self.assertEqual(val, s_lambda(x = val), "")
