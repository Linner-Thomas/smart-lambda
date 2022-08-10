import unittest
from util import test

from core import SmartLambda


class TestSmartLambda(unittest.TestCase):
    @test("SMART-LAMBDA CALL NO-PARAMETER", parameter= range(0, 5))
    def testNoParameter(self, val):
        print(f"\t Validate: (lambda: {val}) -> {val}")

        s_lambda = SmartLambda(lambda: val)
        return_value = s_lambda()

        self.assertEqual(val, return_value, f"Smart-Lambda return-value not matching: {val} != {return_value}")

    @test("SMART-LAMBDA CALL POSITIONAL-PARAMETER", parameter= range(0, 5))
    def testPositionalParameter(self, val):
        print(f"\t Validate: (lambda x: x) -> {val} with x = {val}")

        s_lambda = SmartLambda(lambda x: x)
        return_value = s_lambda(val)

        self.assertEqual(val, return_value, f"Smart-Lambda return-value not matching: {val} != {return_value}")

    @test("SMART-LAMBDA CALL KEYWORD-PARAMETER", parameter= range(0, 5))
    def testKeywordParameter(self, val):
        print(f"\t Validate: (lambda x = 0: x) -> {val} with x = {val}")

        s_lambda = SmartLambda(lambda x = 0: x)
        return_value = s_lambda(x = val)

        self.assertEqual(val, return_value, f"Smart-Lambda return-value not matching: {val} != {return_value}")
