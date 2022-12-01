"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

<<<<<<< HEAD
=======
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
>>>>>>> 4dd85b5d82ff12a4a1465683fa2477e72b83243c
