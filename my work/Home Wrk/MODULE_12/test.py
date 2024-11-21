from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Max')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Bob')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_chellenge(self):
        runner_1 = Runner('Ash')
        runner_2 = Runner('Mill')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
