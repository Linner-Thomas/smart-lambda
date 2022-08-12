import unittest
from util import test

from smart_lambda.lexeme import Constant, Parameter, BinaryOperation, BinaryOperations


class TestLexeme(unittest.TestCase):
    @test("LEXEME CONSTANT REPR-NONE")
    def testConstantReprNone(self):
        expected = f"Constant(None)"

        print(f"\t Validate: Constant(None) -> {expected}")

        constant = Constant(None)

        self.assertEqual(expected, constant.__repr__(),
                         f"Constant-Lexeme representation not matching: {expected} != {constant.__repr__()}")

    @test("LEXEME CONSTANT REPR-INT")
    def testConstantReprInt(self):
        expected = f"Constant(1)"

        print(f"\t Validate: Constant(1) -> {expected}")

        constant = Constant(1)

        self.assertEqual(expected, constant.__repr__(),
                         f"Constant-Lexeme representation not matching: {expected} != {constant.__repr__()}")

    @test("LEXEME CONSTANT REPR-STR")
    def testConstantReprStr(self):
        expected = f"Constant(str)"

        print(f"\t Validate: Constant('str') -> {expected}")

        constant = Constant('str')

        self.assertEqual(expected, constant.__repr__(),
                         f"Constant-Lexeme representation not matching: {expected} != {constant.__repr__()}")

    @test("LEXEME CONSTANT EQ-TRUE")
    def testConstantEqTrue(self):
        print(f"\t Validate: Constant(1) == Constant(1) -> {True}")

        result = Constant(1) == Constant(1)

        self.assertEqual(True, result,
                         f"Constant-Lexeme equality not matching: {True} != {result}")

    @test("LEXEME CONSTANT EQ-FALSE")
    def testConstantEqFalse(self):
        print(f"\t Validate: Constant(1) == Constant(2) -> {False}")

        result = Constant(1) == Constant(2)

        self.assertEqual(False, result,
                         f"Constant-Lexeme equality not matching: {True} != {result}")

    @test("LEXEME CONSTANT EQ-WRONG-TYPE")
    def testConstantEqWrongType(self):
        print(f"\t Validate: Constant('x') == Parameter('x') -> {False}")

        result = Constant('x') == Parameter('x')

        self.assertEqual(False, result,
                         f"Constant-Lexeme equality not matching: {True} != {result}")

    @test("LEXEME PARAMETER REPR")
    def testParameterRepr(self):
        expected = f"Parameter(x)"

        print(f"\t Validate: Parameter('x') -> {expected}")

        parameter = Parameter('x')

        self.assertEqual(expected, parameter.__repr__(),
                         f"Parameter-Lexeme representation not matching: {expected} != {parameter.__repr__()}")

    @test("LEXEME PARAMETER EQ-TRUE")
    def testParameterEqTrue(self):
        print(f"\t Validate: Parameter('x') == Parameter('x') -> {True}")

        result = Parameter('x') == Parameter('x')

        self.assertEqual(True, result,
                         f"Parameter-Lexeme equality not matching: {True} != {result}")

    @test("LEXEME PARAMETER EQ-FALSE")
    def testParameterEqFalse(self):
        print(f"\t Validate: Parameter('x') == Parameter('y') -> {False}")

        result = Parameter('x') == Parameter('y')

        self.assertEqual(False, result,
                         f"Parameter-Lexeme equality not matching: {True} != {result}")

    @test("LEXEME PARAMETER EQ-WRONG-TYPE")
    def testParameterEqWrongType(self):
        print(f"\t Validate: Parameter('x') == Constant('x') -> {False}")

        result = Parameter('x') == Constant('x')

        self.assertEqual(False, result,
                         f"Parameter-Lexeme equality not matching: {True} != {result}")

    @test("LEXEME BINARY-OPERATION REPR-CONST-PARAM")
    def testBinaryOperationReprConstParam(self):
        expected = f"Operation(Constant(1) + Parameter(x))"

        print(f"\t Validate: BinaryOperation(BinaryOperations.ADD, [Constant(1), Parameter('x')]) -> {expected}")

        operation = BinaryOperation(BinaryOperations.ADD, [Constant(1), Parameter('x')])

        self.assertEqual(expected, operation.__repr__(),
                         f"Binary-Operation-Lexeme representation not matching: {expected} != {operation.__repr__()}")

    @test("LEXEME BINARY-OPERATION REPR-PARAM-CONST")
    def testBinaryOperationReprParamConst(self):
        expected = f"Operation(Parameter(x) + Constant(1))"

        print(f"\t Validate: BinaryOperation(BinaryOperations.ADD, [Parameter('x'), Constant(1)]) -> {expected}")

        operation = BinaryOperation(BinaryOperations.ADD, [Parameter('x'), Constant(1)])

        self.assertEqual(expected, operation.__repr__(),
                         f"Binary-Operation-Lexeme representation not matching: {expected} != {operation.__repr__()}")

    @test("LEXEME BINARY-OPERATION EQ-TRUE")
    def testBinaryOperationEqTrue(self):
        print(f"\t Validate: Constant(1) + Constant(2) == Constant(1) + Constant(2) -> {True}")

        result = BinaryOperation(BinaryOperations.ADD, [Constant(1), Constant(2)]) == \
                 BinaryOperation(BinaryOperations.ADD, [Constant(1), Constant(2)])

        self.assertEqual(True, result,
                         f"Binary-Operation-Lexeme equality not matching: {True} != {result}")

    @test("LEXEME BINARY-OPERATION EQ-FALSE-OPERATION")
    def testBinaryOperationEqFalseOperation(self):
        print(f"\t Validate: Constant(1) + Constant(2) == Constant(1) - Constant(2) -> {False}")

        result = BinaryOperation(BinaryOperations.ADD, [Constant(1), Constant(2)]) == \
                 BinaryOperation(BinaryOperations.SUB, [Constant(1), Constant(2)])

        self.assertEqual(False, result,
                         f"Binary-Operation-Lexeme equality not matching: {False} != {result}")

    @test("LEXEME BINARY-OPERATION EQ-FALSE-OPERAND")
    def testBinaryOperationEqFalseOperand(self):
        print(f"\t Validate: Constant(1) + Constant(2) == Constant(1) + Constant(3) -> {False}")

        result = BinaryOperation(BinaryOperations.ADD, [Constant(1), Constant(2)]) == \
                 BinaryOperation(BinaryOperations.ADD, [Constant(1), Constant(3)])

        self.assertEqual(False, result,
                         f"Binary-Operation-Lexeme equality not matching: {False} != {result}")
