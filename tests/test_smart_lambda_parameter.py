import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import Parameter


class TestSmartLambdaParameter(unittest.TestCase):
    @test("SMART-LAMBDA PARAMETER NO")
    def testParameterNo(self):
        parameter_expected = []
        result_expected = None

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda: None")
        print(f"\t \t Expected \t {parameter_expected}")

        s_lambda = SmartLambda(lambda: None)
        parameter_parsed = s_lambda.parameter

        self.assertEqual(parameter_expected, parameter_parsed,
                         f"The parsed parameter aren't matching the expectation! \n"
                         f"Expected \t {parameter_expected} \n"
                         f"Parsed \t \t {parameter_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda: None")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA PARAMETER ONE", parameter = range(5))
    def testParameterOne(self, par):
        parameter_expected = [Parameter('x')]
        result_expected = par

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x: x")
        print(f"\t \t Expected \t {parameter_expected}")

        s_lambda = SmartLambda(lambda x: x)
        parameter_parsed = s_lambda.parameter

        self.assertEqual(parameter_expected, parameter_parsed,
                         f"The parsed parameter aren't matching the expectation! \n"
                         f"Expected \t {parameter_expected} \n"
                         f"Parsed \t \t {parameter_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x: x")
        print(f"\t \t \t \t \t x = {par}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA PARAMETER TWO")
    def testParameterTwo(self):
        parameter_expected = [Parameter('x'), Parameter('y')]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x + y")
        print(f"\t \t Expected \t {parameter_expected}")

        s_lambda = SmartLambda(lambda x, y: x + y)
        parameter_parsed = s_lambda.parameter

        self.assertEqual(parameter_expected, parameter_parsed,
                         f"The parsed parameter aren't matching the expectation! \n"
                         f"Expected \t {parameter_expected} \n"
                         f"Parsed \t \t {parameter_parsed}")

    @test("SMART-LAMBDA PARAMETER UNUSED", parameter = [[i, None] for i in range(5)])
    def testParseUnusedParameter(self, par_x, par_y):
        parameter_expected = [Parameter('x')]
        result_expected = par_x

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x")
        print(f"\t \t Expected \t {parameter_expected}")

        s_lambda = SmartLambda(lambda x, y: x)
        parameter_parsed = s_lambda.parameter

        self.assertEqual(parameter_expected, parameter_parsed,
                         f"The parsed parameter aren't matching the expectation! \n"
                         f"Expected \t {parameter_expected} \n"
                         f"Parsed \t \t {parameter_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")
