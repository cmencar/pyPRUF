from numbers import Number
import numpy as np

def is_list_out_of_range(x: list[Number], inf: Number, sup: Number):
    """
    Check if one element of a list is not in a range

    Parameters
    ----------
    x: list
        input list that will be checked to check
    inf: Number
        upper range bound
    sup: Number
        lower range bound

    Returns
    -------
    bool
        True if one element of x is out of range
        False otherwise

    Examples
    --------
    >>> is_list_out_of_range([ 10, 20, 30 ], 0, 50)
    False

    >>> is_list_out_of_range([ 10, 20, 30 ], 0, 40)
    True
    """
    return any(is_out_of_range(elem, inf, sup) for elem in x)

def is_out_of_range(x: Number, inf: Number, sup: Number) -> bool:
    """
    Check if element is not in a range

    Parameters
    ----------
    x: Number
        element to check
    inf: Number
        upper range bound
    sup: Number
        lower range bound

    Returns
    -------
    bool
        True if x is out of range
        False otherwise

    Examples
    --------
    >>> is_out_of_range(45, 0, 50)
    False

    >>> is_out_of_range(45, 0, 40)
    True
    """
    return inf > x or x > sup

def is_list_not_unique(x: list[Number]) -> bool:
    """
    Check if list contains duplicates

    Parameters
    ----------
    x: list
        Input list that contains elements

    Returns
    -------
    bool
        True if list contains duplicate
        False otherwise

    Examples
    --------
    >>> is_list_not_unique([ 10, 40, 10 ])
    True

    >>> is_list_not_unique([ 10, 20, 30 ])
    False
    """
    return np.unique(x).size != len(x)
