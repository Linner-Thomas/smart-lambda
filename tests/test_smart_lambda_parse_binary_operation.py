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

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION SUB_PARAMETER")
    def testParseSubParameter(self):
        expected = [BinaryOperation(BinaryOperations.SUB, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x - y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x - y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION MUL_PARAMETER")
    def testParseMulParameter(self):
        expected = [BinaryOperation(BinaryOperations.MUL, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x * y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x * y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION DIV_TRUE_PARAMETER")
    def testParseDivTrueParameter(self):
        expected = [BinaryOperation(BinaryOperations.DIV_TRUE, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x / y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x / y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION DIV_FLOOR_PARAMETER")
    def testParseDivFloorParameter(self):
        expected = [BinaryOperation(BinaryOperations.DIV_FLOOR, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x // y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x // y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION MOD_PARAMETER")
    def testParseModParameter(self):
        expected = [BinaryOperation(BinaryOperations.MOD, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x % y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x % y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")
