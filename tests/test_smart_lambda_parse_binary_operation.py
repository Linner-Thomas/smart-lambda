import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import BinaryOperation, BinaryOperations, Constant, Parameter


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

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION AND_PARAMETER")
    def testParseAndParameter(self):
        expected = [BinaryOperation(BinaryOperations.AND, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x & y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x & y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION OR_PARAMETER")
    def testParseOrParameter(self):
        expected = [BinaryOperation(BinaryOperations.OR, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x | y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x | y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION XOR_PARAMETER")
    def testParseXorParameter(self):
        expected = [BinaryOperation(BinaryOperations.XOR, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x ^ y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x ^ y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION SHIFT_LEFT_PARAMETER")
    def testParseShiftLeftParameter(self):
        expected = [BinaryOperation(BinaryOperations.SHIFT_L, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x << y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x << y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION SHIFT_RIGHT_PARAMETER")
    def testParseShiftRightParameter(self):
        expected = [BinaryOperation(BinaryOperations.SHIFT_R, [Parameter('x'), Parameter('y')])]

        print(f"\t Validate: (lambda x, y: x >> y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x >> y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    # The following test-cases are only executed for one parameter
    # These are designed to test different combinations of operands (parameter and constant)

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION MIX-PARAM-CONST")
    def testParseMixParamConst(self):
        expected = [BinaryOperation(BinaryOperations.ADD, [Parameter('x'), Constant(1)])]

        print(f"\t Validate: (lambda x: x + 1) -> {expected}")

        s_lambda = SmartLambda(lambda x: x + 1)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION MIX-CONST-PARAM")
    def testParseMixConstParam(self):
        expected = [BinaryOperation(BinaryOperations.ADD, [Constant(1), Parameter('x')])]

        print(f"\t Validate: (lambda x: 1 + x) -> {expected}")

        s_lambda = SmartLambda(lambda x: 1 + x)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")
