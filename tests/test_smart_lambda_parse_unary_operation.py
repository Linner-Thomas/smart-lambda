import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import UnaryOperation, UnaryOperations, Constant, Parameter


class TestSmartLambdaUnaryOperation(unittest.TestCase):
    @test("SMART-LAMBDA PARSE-BINARY-OPERATION ADD_PARAMETER")
    def testParseAddParameter(self):
        expected = [UnaryOperation(UnaryOperations.POS, Parameter('x'))]

        print(f"\t Validate: (lambda x: +x) -> {expected}")

        s_lambda = SmartLambda(lambda x: +x)
        operations = s_lambda.unary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")
