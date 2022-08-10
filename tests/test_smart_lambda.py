import unittest
from util import test

from smart_lambda.core import SmartLambda


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
        print(f"\t Validate: (lambda x: x) -> []")

        s_lambda = SmartLambda(lambda x: x)
        constants = s_lambda.constants

        self.assertEqual([], constants, f"Smart-Lambda parsed constants not matching: {[]} != {constants}")

    @test("SMART-LAMBDA PARSE NONE-CONSTANT")
    def testParseNoneConstant(self):
        print(f"\t Validate: (lambda: None) -> [None]")

        s_lambda = SmartLambda(lambda: None)
        constants = s_lambda.constants

        self.assertEqual([None], constants, f"Smart-Lambda parsed constants not matching: {[None]} != {constants}")

    @test("SMART-LAMBDA PARSE INT-CONSTANT")
    def testParseIntConstant(self):
        print(f"\t Validate: (lambda: 1) -> [1]")

        s_lambda = SmartLambda(lambda: 1)
        constants = s_lambda.constants

        self.assertEqual([1], constants, f"Smart-Lambda parsed constants not matching: {[1]} != {constants}")

    @test("SMART-LAMBDA PARSE STR-CONSTANT")
    def testParseStrConstant(self):
        print(f"\t Validate: (lambda: 'str') -> ['str']")

        s_lambda = SmartLambda(lambda: 'str')
        constants = s_lambda.constants

        self.assertEqual(['str'], constants, f"Smart-Lambda parsed constants not matching: {['str']} != {constants}")

    @test("SMART-LAMBDA PARSE INT-CONSTANTS-COMBINED")
    def testParseIntConstantsCombined(self):
        # Arithmetic on Int-Constants will be pre-evaluated
        print(f"\t Validate: (lambda: 1 + 2) -> [3]")

        s_lambda = SmartLambda(lambda: 1 + 2)
        constants = s_lambda.constants

        self.assertEqual([3], constants, f"Smart-Lambda parsed constants not matching: {[3]} != {constants}")

    @test("SMART-LAMBDA PARSE INT-CONSTANTS-SEPARATED")
    def testParseIntConstantsSeparated(self):
        print(f"\t Validate: (lambda x: 1 + 2 * x) -> [1, 2]")

        s_lambda = SmartLambda(lambda x: 1 + 2 * x)
        constants = s_lambda.constants

        self.assertEqual([1, 2], constants, f"Smart-Lambda parsed constants not matching: {[1, 2]} != {constants}")

    @test("SMART-LAMBDA PARSE LIST-CONSTANT")
    def testParseListConstant(self):
        print(f"\t Validate: (lambda: [1, 2]) -> [[1, 2]]")

        s_lambda = SmartLambda(lambda: [1, 2])
        constants = s_lambda.constants

        self.assertEqual([[1, 2]], constants, f"Smart-Lambda parsed constants not matching: {[[1, 2]]} != {constants}")

    @test("SMART-LAMBDA PARSE LIST-CONSTANTS")
    def testParseListConstants(self):
        # Arithmetic on List-Constants will not be pre-evaluated
        print(f"\t Validate: (lambda: [1, 2] + [3, 4]) -> [[1, 2], [3, 4]]")

        s_lambda = SmartLambda(lambda: [1, 2] + [3, 4])
        constants = s_lambda.constants

        self.assertEqual([[1, 2], [3, 4]], constants, f"Smart-Lambda parsed constants not matching: "
                                                      f"{[[1, 2], [3, 4]]} != {constants}")

    @test("SMART-LAMBDA PARSE LIST-CONSTANT-LONG")
    def testParseListConstantLong(self):
        print(f"\t Validate: (lambda: [1, 2, 3]) -> [[1, 2, 3]]")

        s_lambda = SmartLambda(lambda: [1, 2, 3])
        constants = s_lambda.constants

        self.assertEqual([[1, 2, 3]], constants, f"Smart-Lambda parsed constants not matching: "
                                                 f"{[[1, 2, 3]]} != {constants}")

    @test("SMART-LAMBDA PARSE LIST-CONSTANTS-LONG")
    def testParseListConstantsLong(self):
        print(f"\t Validate: (lambda: [1, 2, 3] + [4, 5, 6]) -> [[1, 2, 3], [4, 5, 6]]")

        s_lambda = SmartLambda(lambda: [1, 2, 3] + [4, 5, 6])
        constants = s_lambda.constants

        self.assertEqual([[1, 2, 3], [4, 5, 6]], constants, f"Smart-Lambda parsed constants not matching: "
                                                            f"{[[1, 2, 3], [4, 5, 6]]} != {constants}")
