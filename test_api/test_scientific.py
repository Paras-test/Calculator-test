import unittest
from src.api.scientific import sine, cosine, tangent, log

class TestScientificOperations(unittest.TestCase):
    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(sine(90), 1)
        self.assertAlmostEqual(sine(180), 0)
        self.assertAlmostEqual(sine(270), -1)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1)
        self.assertAlmostEqual(cosine(90), 0)
        self.assertAlmostEqual(cosine(180), -1)
        self.assertAlmostEqual(cosine(270), 0)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(0), 0)
        self.assertAlmostEqual(tangent(45), 1)
        self.assertAlmostEqual(tangent(90), math.inf)
        self.assertAlmostEqual(tangent(180), 0)
        self.assertAlmostEqual(tangent(270), -math.inf)

    def test_log(self):
        self.assertAlmostEqual(log(1), 0)
        self.assertAlmostEqual(log(10), 1)
        self.assertAlmostEqual(log(100), 2)
