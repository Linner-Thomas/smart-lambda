import unittest
from util import test

from smart_lambda.core import SmartLambda


class TestSmartLambdaBinaryOperation(unittest.TestCase):
    @test("SMART-LAMBDA PARSE-BINARY-OPERATION ADD_PARAMETER")
    def testParseAddParameter(self):
        expected = []

        print(f"\t Validate: (lambda x, y: x + y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x + y)
        operations = []

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")
