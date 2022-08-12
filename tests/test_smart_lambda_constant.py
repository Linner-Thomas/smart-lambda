import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import Constant


class TestSmartLambdaParseConstant(unittest.TestCase):
    @test("SMART-LAMBDA CONSTANT NONE")
    def testConstantNone(self):
        constants_expected = [Constant(None)]
        result_expected = None

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: None")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: None)
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: None")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA PARSE-CONSTANT INT-CONSTANT")
    def testParseIntConstant(self):
        expected = [Constant(1)]

        print(f"\t Validate: (lambda: 1) -> {expected}")

        s_lambda = SmartLambda(lambda: 1)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT STR-CONSTANT")
    def testParseStrConstant(self):
        expected = [Constant('str')]

        print(f"\t Validate: (lambda: 'str') -> {expected}")

        s_lambda = SmartLambda(lambda: 'str')
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT INT-CONSTANTS-COMBINED")
    def testParseIntConstantsCombined(self):
        expected = [Constant(3)]

        # Arithmetic on Int-Constants will be pre-evaluated
        print(f"\t Validate: (lambda: 1 + 2) -> {expected}")

        s_lambda = SmartLambda(lambda: 1 + 2)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT INT-CONSTANTS-SEPARATED")
    def testParseIntConstantsSeparated(self):
        expected = [Constant(1), Constant(2)]

        print(f"\t Validate: (lambda x: 1 + 2 * x) -> {expected}")

        s_lambda = SmartLambda(lambda x: 1 + 2 * x)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT LIST-CONSTANT")
    def testParseListConstant(self):
        expected = [Constant([1, 2])]

        print(f"\t Validate: (lambda: [1, 2]) -> {expected}")

        s_lambda = SmartLambda(lambda: [1, 2])
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT LIST-CONSTANTS")
    def testParseListConstants(self):
        expected = [Constant([1, 2]), Constant([3, 4])]

        # Arithmetic on List-Constants will not be pre-evaluated
        print(f"\t Validate: (lambda: [1, 2] + [3, 4]) -> {expected}")

        s_lambda = SmartLambda(lambda: [1, 2] + [3, 4])
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT LIST-CONSTANT-LONG")
    def testParseListConstantLong(self):
        expected = [Constant([1, 2, 3])]

        print(f"\t Validate: (lambda: [1, 2, 3]) -> {expected}")

        s_lambda = SmartLambda(lambda: [1, 2, 3])
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT LIST-CONSTANTS-LONG")
    def testParseListConstantsLong(self):
        expected = [Constant([1, 2, 3]), Constant([4, 5, 6])]

        # Arithmetic on List-Constants will not be pre-evaluated
        print(f"\t Validate: (lambda: [1, 2, 3] + [4, 5, 6]) -> {expected}")

        s_lambda = SmartLambda(lambda: [1, 2, 3] + [4, 5, 6])
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT TUPLE-CONSTANT")
    def testParseTupleConstant(self):
        expected = [Constant((1, 2))]

        print(f"\t Validate: (lambda: (1, 2)) -> {expected}")

        s_lambda = SmartLambda(lambda: (1, 2))
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT TUPLE-CONSTANT-LONG")
    def testParseTupleConstantLong(self):
        expected = [Constant((1, 2, 3))]

        print(f"\t Validate: (lambda: (1, 2, 3)) -> {expected}")

        s_lambda = SmartLambda(lambda: (1, 2, 3))
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT TUPLE-CONSTANTS-COMBINED")
    def testParseTupleConstantsCombined(self):
        expected = [Constant((1, 2, 3, 4))]

        # Arithmetic on Tuple-Constants will be pre-evaluated
        print(f"\t Validate: (lambda: (1, 2) + (3, 4)) -> {expected}")

        s_lambda = SmartLambda(lambda: (1, 2) + (3, 4))
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT TUPLE-CONSTANTS-SEPARATED")
    def testParseTupleConstantsSeparated(self):
        expected = [Constant((1, 2)), Constant((3, 4))]

        print(f"\t Validate: (lambda x: (1, 2) + (3, 4) * x) -> {expected}")

        s_lambda = SmartLambda(lambda x: (1, 2) + (3, 4) * x)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT SET-CONSTANT")
    def testParseSetConstant(self):
        expected = [Constant({1, 2})]

        print(f"\t Validate: (lambda: {{1, 2}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {1, 2})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT SET-CONSTANTS")
    def testParseSetConstants(self):
        expected = [Constant({1, 2}), Constant({3, 4})]

        print(f"\t Validate: (lambda: {{*{{1, 2}}, *{{3, 4}}}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {*{1, 2}, *{3, 4}})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT SET-CONSTANT-LONG")
    def testParseSetConstantLong(self):
        expected = [Constant({1, 2, 3})]

        print(f"\t Validate: (lambda: {{1, 2, 3}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {1, 2, 3})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT SET-CONSTANTS-LONG")
    def testParseSetConstantsLong(self):
        expected = [Constant({1, 2, 3}), Constant({4, 5, 6})]

        print(f"\t Validate: (lambda: {{*{{1, 2, 3}}, *{{4, 5, 6}}}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {*{1, 2, 3}, *{4, 5, 6}})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT DICT-CONSTANT")
    def testParseDictConstant(self):
        expected = [Constant({'1': 1, '2': 2})]

        print(f"\t Validate: (lambda: {{'1': 1, '2': 2}} -> {expected}")

        s_lambda = SmartLambda(lambda: {'1': 1, '2': 2})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT DICT-CONSTANTS")
    def testParseDictConstants(self):
        expected = [Constant({'1': 1, '2': 2}), Constant({'3': 3, '4': 4})]

        print(f"\t Validate: (lambda: {{**{{'1': 1, '2': 2}}, **{{'3': 3, '4': 4}}}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {**{'1': 1, '2': 2}, **{'3': 3, '4': 4}})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT DICT-CONSTANT-LONG")
    def testParseDictConstantLong(self):
        expected = [Constant({'1': 1, '2': 2, '3': 3})]

        print(f"\t Validate: (lambda: {{'1': 1, '2': 2, '3': 3}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {'1': 1, '2': 2, '3': 3})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE-CONSTANT DICT-CONSTANTS-LONG")
    def testParseDictConstantsLong(self):
        expected = [Constant({'1': 1, '2': 2, '3': 3}), Constant({'4': 4, '5': 5, '6': 6})]

        print(f"\t Validate: (lambda: {{**{{'1': 1, '2': 2, '3': 3}}, **{{'4': 4, '5': 5, '6': 6}}}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {**{'1': 1, '2': 2, '3': 3}, **{'4': 4, '5': 5, '6': 6}})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")
