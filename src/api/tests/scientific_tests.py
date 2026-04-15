import unittest
from src.api.scientific import sine, cosine, tangent, logarithm

class TestScientificOperations(unittest.TestCase):
    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(sine(math.pi/2), 1)
        self.assertAlmostEqual(sine(math.pi), 0)
        self.assertAlmostEqual(sine(3*math.pi/2), -1)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1)
        self.assertAlmostEqual(cosine(math.pi/2), 0)
        self.assertAlmostEqual(cosine(math.pi), -1)
        self.assertAlmostEqual(cosine(3*math.pi/2), 0)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(0), 0)
        self.assertAlmostEqual(tangent(math.pi/4), 1)
        self.assertAlmostEqual(tangent(math.pi/2), math.inf)
        self.assertAlmostEqual(tangent(3*math.pi/4), -1)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(1), 0)
        self.assertAlmostEqual(logarithm(10), 1)
        self.assertAlmostEqual(logarithm(math.e), 1)