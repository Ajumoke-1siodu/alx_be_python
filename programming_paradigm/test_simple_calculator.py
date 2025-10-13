import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)

                                                                def test_subtraction(self):
                                                                    self.assertEqual(self.calc.subtract(5, 3), 2)
                                                                    self.assertEqual(self.calc.subtract(3, 5), -2)
                                                                    self.assertEqual(self.calc.subtract(0, 0), 0)
                                                                    self.assertEqual(self.calc.subtract(-3, -3), 0)

                                                                def test_multiply(self):
                                                                                                
        self.assertEqual(self.calc.multiply(2, 3), 6)
                                                                                                                                self.assertEqual(self.calc.multiply(-1, 3), -3)
                                                                                                                                self.assertEqual(self.calc.multiply(0, 10), 0)
                                                                                                                                self.assertEqual(self.calc.multiply(-2, -4), 8)

                                                                                                                            def test_divide(self):
                                                                                                                                self.assertEqual(self.calc.divide(10, 2), 5)
                                                                                                                                self.assertEqual(self.calc.divide(-12, 3), -4)
                                                                                                                                self.assertEqual(self.calc.divide(0, 5), 0)
                                                                                                                                                                                    # Division by zero should return None
                                                                                                                                                                                            self.assertIsNone(self.calc.divide(5, 0))
                                                                                                                                self.assertIsNone(self.calc.divide(0, 0))

                                                                                                                        if __name__ == "__main__":
                                                                unittest.main()
