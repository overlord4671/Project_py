import unittest
from test import RunnerTest
from test_2 import TournamentTest

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    runner.run(suite)
