import unittest
from util import test

from itertools import product

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import BinaryOperation, BinaryOperations, Constant, Parameter, UnaryOperation, UnaryOperations


class TestSmartLambdaBinaryOperation(unittest.TestCase):
    @test("SMART-LAMBDA BINARY-OPERATION ADD",
          parameter = [[x + y, x, y] for x, y in product(range(5), range(5))])
    def testAdd(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.ADD, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x + y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x + y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x + y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION SUB",
          parameter = [[x - y, x, y] for x, y in product(range(5), range(5))])
    def testSub(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.SUB, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x - y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x - y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x - y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION MUL",
          parameter = [[x * y, x, y] for x, y in product(range(5), range(5))])
    def testMul(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.MUL, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x * y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x * y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x * y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION DIV-TRUE",
          parameter = [[x / y, x, y] for x, y in product(range(5), range(1, 5))])
    def testDivTrue(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.DIV_TRUE, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x / y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x / y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x / y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION DIV-FLOOR",
          parameter = [[x // y, x, y] for x, y in product(range(5), range(1, 5))])
    def testDivFloor(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.DIV_FLOOR, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x // y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x // y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x // y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION MOD",
          parameter = [[x % y, x, y] for x, y in product(range(5), range(1, 5))])
    def testMod(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.MOD, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x % y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x % y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x % y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION AND",
          parameter = [[x & y, x, y] for x, y in product(range(5), range(5))])
    def testAnd(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.AND, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x & y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x & y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x & y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION OR",
          parameter = [[x | y, x, y] for x, y in product(range(5), range(5))])
    def testOr(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.OR, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x | y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x | y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x | y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION XOR",
          parameter = [[x ^ y, x, y] for x, y in product(range(5), range(5))])
    def testXor(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.XOR, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x ^ y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x ^ y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x ^ y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION SHIFT-LEFT",
          parameter = [[x << y, x, y] for x, y in product(range(5), range(5))])
    def testShiftLeft(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.SHIFT_L, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x << y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x << y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x << y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION SHIFT-RIGHT",
          parameter = [[x >> y, x, y] for x, y in product(range(5), range(5))])
    def testShiftRight(self, res, par_x, par_y):
        operations_expected = [BinaryOperation(BinaryOperations.SHIFT_R, [Parameter('x'), Parameter('y')])]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x >> y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x >> y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x >> y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION COMPLEX-1",
          parameter = [[x + y + z, x, y, z] for x, y, z in product(range(3), range(3), range(3))])
    def testComplex1(self, res, par_x, par_y, par_z):
        operation_inner = BinaryOperation(BinaryOperations.ADD, [Parameter('x'), Parameter('y')])
        operation_outer = BinaryOperation(BinaryOperations.ADD, [operation_inner, Parameter('z')])
        operations_expected = [operation_inner, operation_outer]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x + y + z")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y, z: x + y + z)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x + y + z")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t \t \t \t z = {par_z}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y, z = par_z)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION COMPLEX-2",
          parameter = [[x * y + z, x, y, z] for x, y, z in product(range(3), range(3), range(3))])
    def testComplex2(self, res, par_x, par_y, par_z):
        operation_inner = BinaryOperation(BinaryOperations.MUL, [Parameter('x'), Parameter('y')])
        operation_outer = BinaryOperation(BinaryOperations.ADD, [operation_inner, Parameter('z')])
        operations_expected = [operation_inner, operation_outer]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x * y + z")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y, z: x * y + z)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x * y + z")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t \t \t \t z = {par_z}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y, z = par_z)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION COMPLEX-3",
          parameter = [[x + y * z, x, y, z] for x, y, z in product(range(3), range(3), range(3))])
    def testComplex3(self, res, par_x, par_y, par_z):
        operation_inner = BinaryOperation(BinaryOperations.MUL, [Parameter('y'), Parameter('z')])
        operation_outer = BinaryOperation(BinaryOperations.ADD, [Parameter('x'), operation_inner])
        operations_expected = [operation_inner, operation_outer]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x + y * z")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y, z: x + y * z)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x + y * z")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t \t \t \t z = {par_z}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y, z = par_z)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION COMPLEX-4",
          parameter = [[(x + y) * z, x, y, z] for x, y, z in product(range(3), range(3), range(3))])
    def testComplex4(self, res, par_x, par_y, par_z):
        operation_inner = BinaryOperation(BinaryOperations.ADD, [Parameter('x'), Parameter('y')])
        operation_outer = BinaryOperation(BinaryOperations.MUL, [operation_inner, Parameter('z')])
        operations_expected = [operation_inner, operation_outer]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: (x + y) * z")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y, z: (x + y) * z)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: (x + y) * z")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t \t \t \t z = {par_z}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y, z = par_z)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION COMPLEX-5",
          parameter = [[x * (y + z), x, y, z] for x, y, z in product(range(3), range(3), range(3))])
    def testComplex5(self, res, par_x, par_y, par_z):
        operation_inner = BinaryOperation(BinaryOperations.ADD, [Parameter('y'), Parameter('z')])
        operation_outer = BinaryOperation(BinaryOperations.MUL, [Parameter('x'), operation_inner])
        operations_expected = [operation_inner, operation_outer]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x * (y + z)")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y, z: x * (y + z))
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x * (y + z)")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t \t \t \t z = {par_z}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y, z = par_z)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION COMPLEX-6",
          parameter = [[x * y + x * z, x, y, z] for x, y, z in product(range(3), range(3), range(3))])
    def testComplex6(self, res, par_x, par_y, par_z):
        operation_l = BinaryOperation(BinaryOperations.MUL, [Parameter('x'), Parameter('y')])
        operation_r = BinaryOperation(BinaryOperations.MUL, [Parameter('x'), Parameter('z')])
        operation_add = BinaryOperation(BinaryOperations.ADD, [operation_l, operation_r])
        operations_expected = [operation_l, operation_r, operation_add]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x * y + x * z")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y, z: x * y + x * z)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y, z: x * y + x * z")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t \t \t \t z = {par_z}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y, z = par_z)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA BINARY-OPERATION UNARY-OPERATION",
          parameter = [[x + ~y, x, y] for x, y in product(range(5), range(5))])
    def testUnaryOperation(self, res, par_x, par_y):
        operation_inv = UnaryOperation(UnaryOperations.INV, Parameter('y'))
        operation_add = BinaryOperation(BinaryOperations.ADD, [Parameter('x'), operation_inv])
        operations_expected = [operation_add]
        result_expected = res

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x + ~y")
        print(f"\t \t Expected \t {operations_expected}")

        s_lambda = SmartLambda(lambda x, y: x + ~y)
        operations_parsed = s_lambda.binary_operations

        self.assertEqual(operations_expected, operations_parsed,
                         f"The parsed operations aren't matching the expectation! \n"
                         f"Expected \t {operations_expected} \n"
                         f"Parsed \t \t {operations_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t \t lambda x, y: x + ~y")
        print(f"\t \t \t \t \t x = {par_x}")
        print(f"\t \t \t \t \t y = {par_y}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda(x = par_x, y = par_y)

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA PARSE-BINARY-OPERATION UNARY-OPERATION")
    def testParseUnaryOperation(self):
        operation_inv = UnaryOperation(UnaryOperations.INV, Parameter('y'))
        operation_add = BinaryOperation(BinaryOperations.ADD, [Parameter('x'), operation_inv])

        expected = [operation_add]

        print(f"\t Validate: (lambda x, y: x + ~y) -> {expected}")

        s_lambda = SmartLambda(lambda x, y: x + ~y)
        operations = s_lambda.binary_operations

        self.assertEqual(expected, operations, f"Smart-Lambda operations not matching: {expected} != {operations}")
