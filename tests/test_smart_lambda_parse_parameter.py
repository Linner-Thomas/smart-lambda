import unittest
from util import test

from smart_lambda.core import SmartLambda


class TestSmartLambdaParseParameter(unittest.TestCase):
    @test("SMART-LAMBDA PARSE-PARAMETER NO-PARAMETER")
    def testParseNoParameter(self):
        expected = []

        print(f"\t Validate: (lambda: 1) -> {expected}")

        s_lambda = SmartLambda(lambda: 1)
        parameter = []

        self.assertEqual(expected, parameter, f"Smart-Lambda parameter not matching: {expected} != {parameter}")
