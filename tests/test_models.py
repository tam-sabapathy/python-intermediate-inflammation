"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

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


