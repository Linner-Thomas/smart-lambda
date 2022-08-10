import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import Constant


class TestSmartLambda(unittest.TestCase):
    @test("SMART-LAMBDA CALL NO-PARAMETER", parameter = range(0, 5))
    def testCallNoParameter(self, val):
        print(f"\t Validate: (lambda: {val}) -> {val}")

        s_lambda = SmartLambda(lambda: val)
        return_value = s_lambda()

        self.assertEqual(val, return_value, f"Smart-Lambda return-value not matching: {val} != {return_value}")

    @test("SMART-LAMBDA CALL POSITIONAL-PARAMETER", parameter = range(0, 5))
    def testCallPositionalParameter(self, val):
        print(f"\t Validate: (lambda x: x) -> {val} with x = {val}")

        s_lambda = SmartLambda(lambda x: x)
        return_value = s_lambda(val)

        self.assertEqual(val, return_value, f"Smart-Lambda return-value not matching: {val} != {return_value}")

    @test("SMART-LAMBDA CALL KEYWORD-PARAMETER", parameter = range(0, 5))
    def testCallKeywordParameter(self, val):
        print(f"\t Validate: (lambda x = 0: x) -> {val} with x = {val}")

        s_lambda = SmartLambda(lambda x = 0: x)
        return_value = s_lambda(x = val)

        self.assertEqual(val, return_value, f"Smart-Lambda return-value not matching: {val} != {return_value}")

    @test("SMART-LAMBDA PARSE NO-CONSTANT")
    def testParseNoConstant(self):
        expected = []

        print(f"\t Validate: (lambda x: x) -> {expected}")

        s_lambda = SmartLambda(lambda x: x)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE NONE-CONSTANT")
    def testParseNoneConstant(self):
        expected = [Constant(None)]

        print(f"\t Validate: (lambda: None) -> {expected}")

        s_lambda = SmartLambda(lambda: None)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE INT-CONSTANT")
    def testParseIntConstant(self):
        expected = [Constant(1)]

        print(f"\t Validate: (lambda: 1) -> {expected}")

        s_lambda = SmartLambda(lambda: 1)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE STR-CONSTANT")
    def testParseStrConstant(self):
        expected = [Constant('str')]

        print(f"\t Validate: (lambda: 'str') -> {expected}")

        s_lambda = SmartLambda(lambda: 'str')
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE INT-CONSTANTS-COMBINED")
    def testParseIntConstantsCombined(self):
        expected = [Constant(3)]

        # Arithmetic on Int-Constants will be pre-evaluated
        print(f"\t Validate: (lambda: 1 + 2) -> {expected}")

        s_lambda = SmartLambda(lambda: 1 + 2)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE INT-CONSTANTS-SEPARATED")
    def testParseIntConstantsSeparated(self):
        expected = [Constant(1), Constant(2)]

        print(f"\t Validate: (lambda x: 1 + 2 * x) -> {expected}")

        s_lambda = SmartLambda(lambda x: 1 + 2 * x)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE LIST-CONSTANT")
    def testParseListConstant(self):
        expected = [Constant([1, 2])]

        print(f"\t Validate: (lambda: [1, 2]) -> {expected}")

        s_lambda = SmartLambda(lambda: [1, 2])
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE LIST-CONSTANTS")
    def testParseListConstants(self):
        expected = [Constant([1, 2]), Constant([3, 4])]

        # Arithmetic on List-Constants will not be pre-evaluated
        print(f"\t Validate: (lambda: [1, 2] + [3, 4]) -> {expected}")

        s_lambda = SmartLambda(lambda: [1, 2] + [3, 4])
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE LIST-CONSTANT-LONG")
    def testParseListConstantLong(self):
        expected = [Constant([1, 2, 3])]

        print(f"\t Validate: (lambda: [1, 2, 3]) -> {expected}")

        s_lambda = SmartLambda(lambda: [1, 2, 3])
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE LIST-CONSTANTS-LONG")
    def testParseListConstantsLong(self):
        expected = [Constant([1, 2, 3]), Constant([4, 5, 6])]

        # Arithmetic on List-Constants will not be pre-evaluated
        print(f"\t Validate: (lambda: [1, 2, 3] + [4, 5, 6]) -> {expected}")

        s_lambda = SmartLambda(lambda: [1, 2, 3] + [4, 5, 6])
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE TUPLE-CONSTANT")
    def testParseTupleConstant(self):
        expected = [Constant((1, 2))]

        print(f"\t Validate: (lambda: (1, 2)) -> {expected}")

        s_lambda = SmartLambda(lambda: (1, 2))
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE TUPLE-CONSTANT-LONG")
    def testParseTupleConstantLong(self):
        expected = [Constant((1, 2, 3))]

        print(f"\t Validate: (lambda: (1, 2, 3)) -> {expected}")

        s_lambda = SmartLambda(lambda: (1, 2, 3))
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE TUPLE-CONSTANTS-COMBINED")
    def testParseTupleConstantsCombined(self):
        expected = [Constant((1, 2, 3, 4))]

        # Arithmetic on Tuple-Constants will be pre-evaluated
        print(f"\t Validate: (lambda: (1, 2) + (3, 4)) -> {expected}")

        s_lambda = SmartLambda(lambda: (1, 2) + (3, 4))
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE TUPLE-CONSTANTS-SEPARATED")
    def testParseTupleConstantsSeparated(self):
        expected = [Constant((1, 2)), Constant((3, 4))]

        print(f"\t Validate: (lambda x: (1, 2) + (3, 4) * x) -> {expected}")

        s_lambda = SmartLambda(lambda x: (1, 2) + (3, 4) * x)
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE SET-CONSTANT")
    def testParseSetConstant(self):
        expected = [Constant({1, 2})]

        print(f"\t Validate: (lambda: {{1, 2}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {1, 2})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE SET-CONSTANTS")
    def testParseSetConstants(self):
        expected = [Constant({1, 2}), Constant({3, 4})]

        print(f"\t Validate: (lambda: {{*{{1, 2}}, *{{3, 4}}}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {*{1, 2}, *{3, 4}})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE SET-CONSTANT-LONG")
    def testParseSetConstantLong(self):
        expected = [Constant({1, 2, 3})]

        print(f"\t Validate: (lambda: {{1, 2, 3}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {1, 2, 3})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE SET-CONSTANTS-LONG")
    def testParseSetConstantsLong(self):
        expected = [Constant({1, 2, 3}), Constant({4, 5, 6})]

        print(f"\t Validate: (lambda: {{*{{1, 2, 3}}, *{{4, 5, 6}}}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {*{1, 2, 3}, *{4, 5, 6}})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE DICT-CONSTANT")
    def testParseDictConstant(self):
        expected = [Constant({'1': 1, '2': 2})]

        print(f"\t Validate: (lambda: {{'1': 1, '2': 2}} -> {expected}")

        s_lambda = SmartLambda(lambda: {'1': 1, '2': 2})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE DICT-CONSTANTS")
    def testParseDictConstants(self):
        expected = [Constant({'1': 1, '2': 2}), Constant({'3': 3, '4': 4})]

        print(f"\t Validate: (lambda: {{**{{'1': 1, '2': 2}}, **{{'3': 3, '4': 4}}}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {**{'1': 1, '2': 2}, **{'3': 3, '4': 4}})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE DICT-CONSTANT-LONG")
    def testParseDictConstantLong(self):
        expected = [Constant({'1': 1, '2': 2, '3': 3})]

        print(f"\t Validate: (lambda: {{'1': 1, '2': 2, '3': 3}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {'1': 1, '2': 2, '3': 3})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")

    @test("SMART-LAMBDA PARSE DICT-CONSTANTS-LONG")
    def testParseDictConstantsLong(self):
        expected = [Constant({'1': 1, '2': 2, '3': 3}), Constant({'4': 4, '5': 5, '6': 6})]

        print(f"\t Validate: (lambda: {{**{{'1': 1, '2': 2, '3': 3}}, **{{'4': 4, '5': 5, '6': 6}}}}) -> {expected}")

        s_lambda = SmartLambda(lambda: {**{'1': 1, '2': 2, '3': 3}, **{'4': 4, '5': 5, '6': 6}})
        constants = s_lambda.constants

        self.assertEqual(expected, constants, f"Smart-Lambda parsed constants not matching: "
                                              f"{expected} != {constants}")
