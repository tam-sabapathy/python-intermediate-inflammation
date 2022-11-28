"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest, pytest_cov

@pytest.mark.parametrize( 
    "test, expected",
    [
        ([[0, 0],[0, 0],[0, 0]], [0,0]),
        ([[1, 2],[3, 4],[5, 6]], [3,4])
    ]
)
def test_daily_mean_integers(test, expected):
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test), expected)

@pytest.mark.parametrize( 
    "test, expected",
    [
        ([[4, 3, 5], [1, 6, 2],[4, 1, 9]], [4, 6, 9])
    ]
)
def test_daily_max(test, expected):
    """TEst that max function works for an array of positive integers."""
    from inflammation.models import daily_max

    npt.assert_array_equal(daily_max(test), expected)


@pytest.mark.parametrize( 
    "test, expected",
    [
        ([[4, -2, 5],[1, -6, 2],[-4, -1, 9]], [-4, -6, 2])
    ]
)
def test_daily_min(test, expected):
    """TEst that min function works for an array of positive and negative integers."""

    from inflammation.models import daily_min

    npt.assert_array_equal(daily_min(test), expected)


def test_daily_min_string():
    '''Test for TypeError when we a string'''
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min(['abd','ads'], ['asd', 'suhs'])

# @pytest.mark.parametrize(
#     'test, expected'
#     [
#         ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]])
#     ]
# )
# def test_patient_normalise(test, expected):

#     from inflammation.models import patient_normalise
#     npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)