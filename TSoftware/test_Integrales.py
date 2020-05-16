from unittest import TestCase
from Integrales import derivative_Integral
from Integrales import Integration_Method_trapezoidal
from Integrales import Integration_Method_trapezoidal_vectorized
import numpy as np
import math


class Test(TestCase):
    def test_DERIVATIVE_Default_Value(self):
        f = np.cos
        a = 0
        h = 0.01
        actual = derivative_Integral(f, a, method='central', h=0.01)
        expected = (f(a + h) - f(a - h)) / (2 * h)
        self.assertEqual(actual, expected)

    #def test_DERIVATIVE_Constant_f(self):
        #with self.assertRaises(TypeError):
            #derivative_Integral(f=0, a=0, method='central', h=0.01)

    # class Test(TestCase):
    def test_DERIVATIVE_Error_Method_STRING(self):
        with self.assertRaises(ValueError):
            derivative_Integral(f=np.cos, a=0, method=' hjshsfghshdsh')

    # class Test(TestCase):
    def test_DERIVATIVE_backward_Method(self):
        f = np.exp
        a = 0
        method = 'backward'
        h = 0.0001
        actual = derivative_Integral(f, a, method, h)
        expected = (f(a) - f(a - h)) / h
        self.assertEqual(actual, expected)

    # class Test(TestCase):
    def test_DERIVATIVE_Forward_Method(self):
        f = np.sin
        a = 0
        method = 'forward'
        h = 0.0003
        actual = derivative_Integral(f, a, method, h)
        expected = (f(a) - f(a - h)) / h
        self.assertEqual(actual, expected)

    def test_INTEGRATION_Success_trapezoidal_For_linear_function(self):
        f = lambda x: 6 * x - 5
        F = lambda x: 3 * x ** 2 - 5 * x  # Anti-derivative
        a = 1.8
        b = 4.4
        expected = F(b) - F(a)
        tol = 1E-14
        for n in 2, 20, 21:
            actual = Integration_Method_trapezoidal(f, a, b, n)
            error = abs(expected - actual)
            success = error < tol
            msg = '(n = %d, err = %g)' % (n, error)
            assert success, msg

    def test_INTEGRATION_Unsuccess_method_trapezoidal_vectorized(self):

        f = lambda x: 6 * x - 5
        F = lambda x: 3 * x ** 2 - 5 * x  # Anti-derivative
        a = 1.8
        b = 4.4
        expected = F(b) - F(a)
        tol = 1E-15
        for n in 2, 20, 21:
            actual = Integration_Method_trapezoidal_vectorized(f, a, b, n)
            error = abs(expected - actual)
            unsuccess = error > tol
            msg = '(n = %d, err = %g, tol =%g)' % (n, error, tol)
            assert unsuccess, msg

    def test_INTEGRATION_Compare_SPEED_trapezoidal_vectorized_And_trapezoidal(self):
        f = lambda x: 6 * x - 5
        F = lambda x: 3 * x ** 2 - 5 * x  # Anti-derivative
        a = 1.8
        b = 4.4
        for n in 2, 20, 21:
            compare = Integration_Method_trapezoidal(f, a, b, n) < Integration_Method_trapezoidal_vectorized(f, a, b, n)
        self.assertTrue(compare)
