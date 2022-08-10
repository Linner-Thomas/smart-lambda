import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import BinaryOperation, BinaryOperations, Parameter


class TestSmartLambdaBinaryOperation(unittest.TestCase):
    @test("SMART-LAMBDA PARSE-BINARY-OPERATION ADD_PARAMETER")
    def testParseAddParameter(self):
        expected = [BinaryOperation(BinaryOperations.ADD, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x + y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x + y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")
