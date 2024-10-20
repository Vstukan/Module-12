class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Ходок")
        for _ in range(10):
            runner.walk()
        # Специально меняем на 40 (правильно 50)
        self.assertEqual(runner.distance, 40)

    def test_run(self):
        runner = Runner("Бегун")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Бегун 1")
        runner2 = Runner("Бегун 2")
        # Вызываем у первого run, а у второго walk 10 раз
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Проверяем, что дистанции не равны (100 != 50)
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()