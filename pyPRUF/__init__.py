"""
A Python library for PRUF proposed by Zadeh.
"""

__version__ = "0.1.0"
__author__ = 'Nicolò Resta'
__credits__ = 'CILAB - Università degli Studi di Bari Aldo Moro'

from .fset import FSet
from .fuzzy_function import tri_mf, trap_mf, bell_mf, gauss_mf
from .ts_control import TSControl, TSRule