import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import UnaryOperation, UnaryOperations, Parameter


class TestSmartLambdaUnaryOperation(unittest.TestCase):
    @test("SMART-LAMBDA PARSE-UNARY-OPERATION POS-PARAMETER")
    def testParsePosParameter(self):
        expected = [UnaryOperation(UnaryOperations.POS, Parameter('x'))]

        print(f"\t Validate: (lambda x: +x) -> {expected}")

        s_lambda = SmartLambda(lambda x: +x)
        operations = s_lambda.unary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-UNARY-OPERATION NEG-PARAMETER")
    def testParseNegParameter(self):
        expected = [UnaryOperation(UnaryOperations.NEG, Parameter('x'))]

        print(f"\t Validate: (lambda x: -x) -> {expected}")

        s_lambda = SmartLambda(lambda x: -x)
        operations = s_lambda.unary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-UNARY-OPERATION INV-PARAMETER")
    def testParseInvParameter(self):
        expected = [UnaryOperation(UnaryOperations.INV, Parameter('x'))]

        print(f"\t Validate: (lambda x: ~x) -> {expected}")

        s_lambda = SmartLambda(lambda x: ~x)
        operations = s_lambda.unary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")
