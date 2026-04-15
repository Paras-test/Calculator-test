import unittest
from src.api.scientific import sin, cos, tan, log

class TestScientificOperations(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(30), math.sin(math.radians(30)))
        self.assertAlmostEqual(sin(60), math.sin(math.radians(60)))
        self.assertAlmostEqual(sin(90), 1)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(30), math.cos(math.radians(30)))
        self.assertAlmostEqual(cos(60), math.cos(math.radians(60)))
        self.assertAlmostEqual(cos(90), 0)

    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(30), math.tan(math.radians(30)))
        self.assertAlmostEqual(tan(60), math.tan(math.radians(60)))
        self.assertAlmostEqual(tan(90), float('inf'))

    def test_log(self):
        self.assertAlmostEqual(log(1), 0)
        self.assertAlmostEqual(log(2), math.log(2))
        self.assertAlmostEqual(log(10), math.log(10))