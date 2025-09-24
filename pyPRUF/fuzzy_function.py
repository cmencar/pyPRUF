import math

def trap_mf(
        x: float = 0,
        a: float = 0,
        b: float = 0,
        c: float = 0,
        d: float = 0
):
    """
    Function that calculate the output of a trapezoidal function

    Parameters
    ----------
    x: float
        Input of the trapezoidal function. Default is 0.
    a: float
        Left lower boundary of trapezoidal function. Default is 0.
    b: float
        Left upper boundary of trapezoidal function. Default is 0.
    c: float
        Right upper boundary of trapezoidal function. Default is 0.
    d: float
        Right lower boundary of trapezoidal function. Default is 0.

    a, b, c and d must be sequential
    Returns
    -------
    float
        f(x) of the trapezoidal function

    Raises
    ------
        ValueError: If a, b, c and d are not sequential.

    Examples
    --------
    >>> trap_mf(0, 1, 2, 4, 5)
    0

    >>> trap_mf(1.5, 1, 2, 4, 5)
    0.5

    >>> trap_mf(3, 1, 2, 4, 5)
    1
    """
    if not (a <= b <= c <= d):
        raise ValueError("a, b, c and d are not sequential")

    if a == b == c == d:
        return 1 if x == a else 0.0

    # Handle out-of-range
    if x < a or x > d:
        return 0.0

    if a <= x <= b:
        return (x - a) / (b - a) if b != a else 1.0
    elif b <= x <= c:
        return 0 if b == c else 1
    elif c <= x <= d:
        return (d - x) / (d - c) if c != d else 1.0
    else:
        return 0

def tri_mf(
        x: float = 0,
        a: float = 0,
        b: float = 0,
        c: float = 0,
):
    """
    Function that calculate the output of a triangular function

    Parameters
    ----------
    x: float
        The input value.
    a: float
        Left lower boundary of triangular function. Default is 0.
    b: float
        Left upper boundary of triangular function. Default is 0.
    c: float
        Right upper boundary of triangular function. Default is 0.

    a, b and c must be sequential
    Returns
    -------
    float
        f(x) of the triangular function

    Raises
    ------
        ValueError: If a, b, c and d are not sequential.

    Examples
    --------
    >>> tri_mf(0, 1, 2, 3)
    0

    >>> tri_mf(2, 1, 2, 3)
    1

    >>> tri_mf(1.5, 1, 2, 3)
    0.5
    """
    return trap_mf(x, a, b, b, c)


def bell_mf(
        x: float = 0,
        m: float = 0,
        s: float = 0,
) -> float:
    """
    Calculates the value of a bell-shaped function.

    It returns a value based on the distance of `x` from `m` scaled by `s`.

    Parameters
    ----------

    x: float
        The input value. Default is 0.
    m: float
        The mean or center of the bell curve. Default is 0.
    s: float
        The width (spread) of the bell curve. Default is 0.

    Returns
    -------
    float:
        f(x) of the bell function

    Raises
    ------
    ZeroDivisionError
    If `s` is 0, since division by zero occurs.

    Notes
    -----
    This function does not include a normalization constant.

    Examples
    --------
    >>> bell_mf(x=1, m=0, s=1)
    0.36787944117144233

    >>> bell_mf(x=0, m=0, s=1)
    1.0

    >>> bell_mf(x=2, m=0, s=2)
    0.6065306597126334
    """
    return math.exp((-1 * pow(x - m, 2)) / pow(s, 2))

def gauss_mf(x: float = 0, m: float = 1, sigma: float = 1) -> float:
    """
    Calculates the value of the normalized Gaussian function.

    Parameters
    ----------
    x: float
        The input value for which the Gaussian is computed. Default is 0.
    m: float
        The mean (center) of the distribution. Default is 1.
    sigma: float
        The standard deviation (spread) of the distribution. Default is 1.

    Returns
    -------
    float
        f(x) of the Gaussian distribution

    Raises
    ------
    ValueError
        If `sigma` is 0, since division by zero would occur.

    Examples
    --------
    >>> gauss_mf(x=1, m=1, sigma=1)
    0.3989422804014337

    >>> gauss_mf(x=0, m=0, sigma=1)
    0.3989422804014337

    >>> gauss_mf(x=2, m=1, sigma=1)
    0.24197072451914337
    """
    if sigma == 0:
        raise ValueError("sigma must be non-zero")
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - m) ** 2) / (2 * sigma ** 2))
