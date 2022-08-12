import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import UnaryOperation, UnaryOperations, Parameter, BinaryOperation, BinaryOperations


class TestSmartLambdaUnaryOperation(unittest.TestCase):
    @test("SMART-LAMBDA UNARY-OPERATION POS", parameter = [[+i, i] for i in range(5)])
    def testPos(self, res, par):
        operations_expected = [UnaryOperation(UnaryOperations.POS, Parameter('x'))]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x: +x")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x: +x)
        operations_parsed = s_lambda.unary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x: +x")
        print(f"\t \t \t \t \t x = {par}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA UNARY-OPERATION NEG", parameter = [[-i, i] for i in range(5)])
    def testNeg(self, res, par):
        operations_expected = [UnaryOperation(UnaryOperations.NEG, Parameter('x'))]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x: -x")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x: -x)
        operations_parsed = s_lambda.unary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x: -x")
        print(f"\t \t \t \t \t x = {par}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA UNARY-OPERATION INV", parameter = [[~i, i] for i in range(5)])
    def testInv(self, res, par):
        operations_expected = [UnaryOperation(UnaryOperations.INV, Parameter('x'))]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x: ~x")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x: ~x)
        operations_parsed = s_lambda.unary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x: ~x")
        print(f"\t \t \t \t \t x = {par}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA UNARY-OPERATION INV-COMPLEX-1")
    def testInvComplex1(self):
        operations_expected = [UnaryOperation(UnaryOperations.INV,
                                              BinaryOperation(BinaryOperations.ADD, [Parameter('x'), Parameter('y')]))]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: ~(x + y)")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: ~(x + y))
        operations_parsed = s_lambda.unary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")
