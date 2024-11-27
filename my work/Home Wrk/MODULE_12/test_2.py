from runner_2 import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            result = cls.all_results[key]
            results_names = {k: v.name for k, v in result.items()}
            print(results_names)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)  # Усэйн и Ник
        result = tournament.start()
        TournamentTest.all_results[1] = result
        last_runner = result[max(result.keys())]
        self.assertTrue(last_runner.name == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)  # Андрей и Ник
        result = tournament.start()
        TournamentTest.all_results[2] = result
        last_runner = result[max(result.keys())]
        self.assertTrue(last_runner.name == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)  # Усэйн, Андрей, Ник
        result = tournament.start()
        TournamentTest.all_results[3] = result
        last_runner = result[max(result.keys())]
        self.assertTrue(last_runner.name == 'Ник')


if __name__ == "__main__":
    unittest.main()
