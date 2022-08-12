import unittest
from util import test

from smart_lambda.core import SmartLambda
from smart_lambda.lexeme import Constant


class TestSmartLambdaConstant(unittest.TestCase):
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

    @test("SMART-LAMBDA CONSTANT INT")
    def testConstantInt(self):
        constants_expected = [Constant(1)]
        result_expected = 1

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: 1")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: 1)
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: 1")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT STR")
    def testConstantStr(self):
        constants_expected = [Constant('str')]
        result_expected = 'str'

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: 'str'")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: 'str')
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: 'str'")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT INTS-COMBINED")
    def testConstantIntsCombined(self):
        constants_expected = [Constant(3)]
        result_expected = 3

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: 1 + 2")
        print(f"\t \t Expected \t {constants_expected}")

        # Arithmetic on Int-Constants will be pre-evaluated
        s_lambda = SmartLambda(lambda: 1 + 2)
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: 1 + 2")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT INTS-SEPARATED")
    def testConstantIntsSeparated(self):
        constants_expected = [Constant(1), Constant(2)]
        result_expected = 3

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: 1 + 2 * x")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda x: 1 + 2 * x)
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

    @test("SMART-LAMBDA CONSTANT LIST")
    def testConstantList(self):
        constants_expected = [Constant([1, 2])]
        result_expected = [1, 2]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: [1, 2]")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: [1, 2])
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: [1, 2]")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT LIST-LONG")
    def testConstantListLong(self):
        constants_expected = [Constant([1, 2, 3])]
        result_expected = [1, 2, 3]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: [1, 2, 3]")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: [1, 2, 3])
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: [1, 2, 3]")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT LISTS")
    def testConstantLists(self):
        constants_expected = [Constant([1, 2]), Constant([3, 4])]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: [1, 2] + [3, 4]")
        print(f"\t \t Expected \t {constants_expected}")

        # Arithmetic on List-Constants will not be pre-evaluated
        s_lambda = SmartLambda(lambda: [1, 2] + [3, 4])
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

    @test("SMART-LAMBDA CONSTANT LISTS-LONG")
    def testConstantListsLong(self):
        constants_expected = [Constant([1, 2, 3]), Constant([4, 5, 6])]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: [1, 2, 3] + [4, 5, 6]")
        print(f"\t \t Expected \t {constants_expected}")

        # Arithmetic on List-Constants will not be pre-evaluated
        s_lambda = SmartLambda(lambda: [1, 2, 3] + [4, 5, 6])
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

    @test("SMART-LAMBDA CONSTANT TUPLE")
    def testConstantTuple(self):
        constants_expected = [Constant((1, 2))]
        result_expected = (1, 2)

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: (1, 2)")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: (1, 2))
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: (1, 2)")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT TUPLE-LONG")
    def testConstantTupleLong(self):
        constants_expected = [Constant((1, 2, 3))]
        result_expected = (1, 2, 3)

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: (1, 2, 3)")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: (1, 2, 3))
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: (1, 2, 3)")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT TUPLES-COMBINED")
    def testConstantTuplesCombined(self):
        constants_expected = [Constant((1, 2, 3, 4))]
        result_expected = (1, 2, 3, 4)

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: (1, 2) + (3, 4)")
        print(f"\t \t Expected \t {constants_expected}")

        # Arithmetic on Tuple-Constants will be pre-evaluated
        s_lambda = SmartLambda(lambda: (1, 2) + (3, 4))
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: (1, 2) + (3, 4)")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT TUPLES-SEPARATED")
    def testConstantTuplesSeparated(self):
        constants_expected = [Constant((1, 2)), Constant((3, 4))]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda x: (1, 2) + (3, 4) * 2")
        print(f"\t \t Expected \t {constants_expected}")

        # Arithmetic on Tuple-Constants will be pre-evaluated
        s_lambda = SmartLambda(lambda x: (1, 2) + (3, 4) * x)
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

    @test("SMART-LAMBDA CONSTANT SET")
    def testConstantSet(self):
        constants_expected = [Constant({1, 2})]
        result_expected = {1, 2}

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: {{1, 2}}")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: {1, 2})
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: {{1, 2}}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT SET-LONG")
    def testConstantSetLong(self):
        constants_expected = [Constant({1, 2, 3})]
        result_expected = {1, 2, 3}

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: {{1, 2, 3}}")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: {1, 2, 3})
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: {{1, 2, 3}}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT SETS")
    def testConstantSets(self):
        constants_expected = [Constant({1, 2}), Constant({3, 4})]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: {{*{{1, 2}}, *{{3, 4}}}}")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: {*{1, 2}, *{3, 4}})
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

    @test("SMART-LAMBDA CONSTANT SETS-LONG")
    def testConstantSetsLong(self):
        constants_expected = [Constant({1, 2, 3}), Constant({4, 5, 6})]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: {{*{{1, 2, 3}}, *{{4, 5, 6}}}}")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: {*{1, 2, 3}, *{4, 5, 6}})
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

    @test("SMART-LAMBDA CONSTANT DICT")
    def testConstantDict(self):
        constants_expected = [Constant({'1': 1, '2': 2})]
        result_expected = {'1': 1, '2': 2}

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: {{'1': 1, '2': 2}}")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: {'1': 1, '2': 2})
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: {{'1': 1, '2': 2}}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT DICT-LONG")
    def testConstantDictLong(self):
        constants_expected = [Constant({'1': 1, '2': 2, '3': 3})]
        result_expected = {'1': 1, '2': 2, '3': 3}

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: {{'1': 1, '2': 2, '3': 3}}")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: {'1': 1, '2': 2, '3': 3})
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

        print(f"\t Interpreting lambda ...")
        print(f"\t \t Input \t\t lambda: {{'1': 1, '2': 2, '3': 3}}")
        print(f"\t \t Expected \t {result_expected}")

        result_interpreted = s_lambda()

        self.assertEqual(result_expected, result_interpreted,
                         f"The interpreted result isn't matching the expectation! \n"
                         f"Expected \t {result_expected} \n"
                         f"Parsed \t \t {result_interpreted}")

    @test("SMART-LAMBDA CONSTANT DICTS")
    def testConstantDicts(self):
        constants_expected = [Constant({'1': 1, '2': 2}), Constant({'3': 3, '4': 4})]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: {{**{{'1': 1, '2': 2}}, **{{'3': 3, '4': 4}}}}")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: {**{'1': 1, '2': 2}, **{'3': 3, '4': 4}})
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")

    @test("SMART-LAMBDA CONSTANT DICTS-LONG")
    def testConstantDictsLong(self):
        constants_expected = [Constant({'1': 1, '2': 2, '3': 3}), Constant({'4': 4, '5': 5, '6': 6})]

        print(f"\t Parsing lambda ...")
        print(f"\t \t Input \t\t lambda: {{**{{'1': 1, '2': 2, '3': 3}}, **{{'4': 4, '5': 5, '6': 6}}}}")
        print(f"\t \t Expected \t {constants_expected}")

        s_lambda = SmartLambda(lambda: {**{'1': 1, '2': 2, '3': 3}, **{'4': 4, '5': 5, '6': 6}})
        constants_parsed = s_lambda.constants

        self.assertEqual(constants_expected, constants_parsed,
                         f"The parsed constants aren't matching the expectation! \n"
                         f"Expected \t {constants_expected} \n"
                         f"Parsed \t \t {constants_parsed}")
