import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import Parameter


class TestSmartLambdaParseParameter(unittest.TestCase):
    @test("SMART-LAMBDA PARSE-PARAMETER NO-PARAMETER")
    def testParseNoParameter(self):
        expected = []

        print(f"\t Validate: (lambda: 1) -> {expected}")

        s_lambda = SmartLambda(lambda: 1)
        parameter = s_lambda.parameter

        self.assertEqual(expected, parameter, f"Smart-Lambda parameter not matching: {expected} != {parameter}")

    @test("SMART-LAMBDA PARSE-PARAMETER ONE-PARAMETER")
    def testParseOneParameter(self):
        expected = [Parameter('x')]

        print(f"\t Validate: (lambda x: x) -> {expected}")

        s_lambda = SmartLambda(lambda x: x)
        parameter = s_lambda.parameter

        self.assertEqual(expected, parameter, f"Smart-Lambda parameter not matching: {expected} != {parameter}")

    @test("SMART-LAMBDA PARSE-PARAMETER TWO-PARAMETER")
    def testParseTwoParameter(self):
        expected = [Parameter('x'), Parameter('y')]

        print(f"\t Validate: (lambda x, y: x * y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x * y)
        parameter = s_lambda.parameter

        self.assertEqual(expected, parameter, f"Smart-Lambda parameter not matching: {expected} != {parameter}")

    @test("SMART-LAMBDA PARSE-PARAMETER UNUSED-PARAMETER")
    def testParseTwoParameter(self):
        # Unused parameter aren't loaded
        expected = [Parameter('x')]

        print(f"\t Validate: (lambda x, y: x) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x)
        parameter = s_lambda.parameter

        self.assertEqual(expected, parameter, f"Smart-Lambda parameter not matching: {expected} != {parameter}")
