import unittest

import numpy as np
import pandas as pd

from pyPRUF.fset import FSet
from pyPRUF.fuzzy_function import trap_mf, gauss_mf, tri_mf, bell_mf


class TestFSet(unittest.TestCase):
    def test_constructor_dict(self):
        f_set = FSet(
            mu={
                10: 0.2,
                11: 0.5,
                12: 0.1
            }
        )

        self.assertEqual(f_set[10], 0.2)

        with self.assertRaises(Exception):
            FSet(mu={ 10: 0.2, 11: 10, 12: 0.1})

    def test_constructor_bool(self):
        f_set_a = FSet(mu=True, index=[10, 20])
        f_set_b = FSet(mu=False)

        self.assertEqual(f_set_a.default_value, 1)
        self.assertEqual(f_set_b.default_value, 0)

    def test_constructor_series(self):
        series = pd.Series([0.2, 0.3], index=[10, 20])
        f_set_a = FSet(mu=series)

        self.assertEqual(f_set_a[10], 0.2)

        with self.assertRaises(Exception):
            series_b = pd.Series([0.2, 0.3], index=[10, 10])
            FSet(mu=series_b)
            series_c = pd.Series([0.2, 12], index=[10, 2])
            FSet(mu=series_c)

    def test_constructor_list(self):
        f_set = FSet(mu=[0.2, 0.1], index=[10, 20])
        self.assertEqual(f_set[10], 0.2)

        with self.assertRaises(Exception):
            FSet(mu=[0.2, 0.1], index=[10, 10])
            FSet(mu=[0.2, 12], index=[10, 10])

    def test_constructor_np_array(self):
        f_set = FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 2]))
        self.assertEqual(f_set[1], 0.5)

        with self.assertRaises(Exception):
            FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 1]))
            FSet(mu=np.array([0.5, 8]), index=np.array([1, 2]))

    def test_constructor_missing_index(self):
        with self.assertRaises(Exception):
            FSet(mu=np.array([0.5, 0.2]), default_value=10)

    def test_constructor_invalid_mu(self):
        with self.assertRaises(Exception):
            FSet(mu=10)

    def test_constructor_default_value(self):
        with self.assertRaises(Exception):
            FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 2]), default_value=10)

        f_set = FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 2]))
        self.assertEqual(f_set[1], 0.5)

    def test_constructor_func(self):
        f_set_a = FSet(mu= lambda x: trap_mf(x, 1, 4, 5, 8), index=[1, 2.5, 4.5])
        f_set_b = FSet(mu= lambda x: tri_mf(x, 1, 4, 5), index=[1, 5, 4, 10])
        f_set_c = FSet(mu= lambda x: gauss_mf(x, 1, 2), index=[1, 5, 2, 10])
        f_set_d = FSet(mu= lambda x: bell_mf(x, 1, 4), index=[1, 5, 2, 10])

        self.assertEqual(f_set_a[1], 0)
        self.assertEqual(f_set_a[2.5], 0.5)

        self.assertEqual(f_set_b[5], 0)
        self.assertEqual(f_set_b[4], 1)

        self.assertAlmostEqual(f_set_c[1], 0.199, 3)
        self.assertAlmostEqual(f_set_c[2], 0.176, 3)

        self.assertAlmostEqual(f_set_d[1], 1)
        self.assertAlmostEqual(f_set_d[10], 0.006, 3)

    def test_set_item(self):
        f_set = FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 2]))

        f_set[1] = 0.9
        self.assertEqual(f_set[1], 0.9)

        with self.assertRaises(Exception):
            f_set[2] = 1.9

    def test_intersection(self):
        f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.5)
        f_set_b = FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 2]), default_value=0.2)

        intersection = f_set_a.intersection(f_set_b)

        self.assertEqual(intersection[1], 0.5)
        self.assertEqual(intersection[3], 0.2)
        self.assertEqual(intersection.default_value, 0.2)

    def test_union(self):
        f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.5)
        f_set_b = FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 2]), default_value=0.2)

        union = f_set_a.union(f_set_b)

        self.assertEqual(union[1], 0.8)
        self.assertEqual(union[3], 1)
        self.assertEqual(union.default_value, 0.5)

    def test_complement(self):
        f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)
        complement = f_set_a.complement()

        self.assertAlmostEqual(complement[1], 0.2)
        self.assertAlmostEqual(complement[3], 0)
        self.assertAlmostEqual(complement.default_value, 0.8)

    def test_mu(self):
        f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)

        self.assertEqual(f_set_a.mu(1), 0.8)
        self.assertEqual(f_set_a.mu(80), 0.2)

    def test_get_item(self):
        f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)

        self.assertEqual(f_set_a.mu(1), 0.8)
        self.assertEqual(f_set_a.mu(80), 0.2)

    def test_is_included(self):
        f_set_a = FSet(mu=np.array([0.1, 0.1, 0.1]), index=np.array([1, 2, 3]), default_value=0.1)
        f_set_b = FSet(mu=np.array([0.2, 0.2, 0.3]), index=np.array([1, 2, 3]), default_value=0.2)
        f_set_c = FSet(mu=np.array([0.1, 0.2, 0.05]), index=np.array([1, 2, 3]), default_value=0.5)
        f_set_d = FSet(mu=np.array([0.1, 0.1, 0.1]), index=np.array([1, 2, 3]), default_value=0.05)

        self.assertTrue(f_set_a.is_included(f_set_b))
        self.assertFalse(f_set_a.is_included(f_set_c))
        self.assertFalse(f_set_a.is_included(f_set_d))

    def test_to_numpy(self):
        f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)
        numpy_list = f_set_a.to_numpy()
        print(numpy_list)

        self.assertEqual(numpy_list[0][0], 1)
        self.assertEqual(numpy_list[0][1], 0.8)


    def test_to_list(self):
        f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)
        fuzzy_list = f_set_a.to_numpy()

        self.assertEqual(fuzzy_list[0][0], 1)
        self.assertEqual(fuzzy_list[0][1], 0.8)

    def test_equals_identical_sets(self):
        f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)
        f_set_b = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)

        f_set_c = FSet(mu=np.array([0.8, 1, 0.1]), index=np.array([1, 2, 4]), default_value=0.2)
        f_set_d = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.3)

        f_set_e = FSet(mu=np.array([0.8]), index=np.array([1]), default_value=0.3)
        f_set_f = FSet(mu=np.array([0.8, 0.4]), index=np.array([1, 2]), default_value=0.3)

        self.assertTrue(f_set_a.equals(f_set_b))
        self.assertFalse(f_set_a.equals(f_set_c))
        self.assertFalse(f_set_a.equals(f_set_d))
        self.assertTrue(f_set_e.equals(f_set_f))