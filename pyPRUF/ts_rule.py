import math
from numbers import Number
from typing import Tuple, List, Callable, Literal

from pyPRUF import FSet


class TSRule:
    """
    Class that represents a Takagi Sugeno controller's rule of a fuzzy controller
    """

    def __init__(
            self,
            rule_items: List[Tuple[str, FSet]] = (),
            rule_output: Callable[[dict], Number] = None
    ):
        """
        Initiate a single TSRule
        Parameters
        ----------
        rule_items : list of tuple of (str, FSet), optional
            A list of tuples representing the rule's input conditions.
            Each tuple consists of:
                - str: the name of the input variable
                - FSet: the fuzzy set associated with that variable

            Defaults to an empty list.

        rule_output : callable, optional
            A function or lambda that calculates the rule’s output
            based on the inputs. It can return a crisp value or another
            fuzzy set, depending on the application.

        Examples
        --------
        >>> def out_temp(a, b, c, ee, e):
        ...     return a * e + b * ee + c

        >>> def rule_1_out(input_c):
        ...     return out_temp(20, 18, 15, input_c["ee"], input_c["e"])

        >>> bg_negative_fs = FSet(
        ...     mu=lambda x: trap_mf(x, -10, -10, -7.5, -5),
        ...     index=np.arange(-10, -4, 0.5)
        ... )
        >>> rule = TSRule( [ ("e", bg_negative_fs), ("ee", bg_negative_fs) ], rule_1_out )

        """
        self.output = rule_output
        self.rule_items = list(rule_items)

    def __str__(self):
        return (f'If { " ⋀ ".join(f"{var} ∈ {f_set.name}" for var, f_set in self.rule_items) }'
                f' then o = {self.output.__name__}(...input)')

    def firing_strength(
            self,
            control_input: dict = None,
            mode: Literal["prod", "min"] = "prod"
    ):
        """
        Get the firing strength of the rule based off an input. It is possible to calculate the firing strength wth different methods

        Parameters
        ----------
        control_input: dict, optional
            Dictionary containing the input of the rule, if the rule has an element with "a" the rule must contain a value with "a" key
        mode: ['prod', 'min'], optional
            The method used to compute the rule's firing strength:

            - 'prod': the firing strength is the product of the single rule elements.
            - 'min' : the firing strength is the minimum of the single rule elements.

        Returns
        -------
        float
            The rule's firing strength  based off of the input and the mode

        Examples
        --------
        >>> rule = TSRule( [ ("e", bg_negative_fs), ("ee", bg_negative_fs) ], rule_1_out )
        >>> rule.firing_strength({ "e": 0.2, "ee": -0.2 })
        >>> rule.firing_strength({ "e": 0.2, "ee": -0.2 }, mode="min")
        """
        if mode == "prod":
            try:
                mu_items = list(f_set.mu(control_input[elem]) for elem, f_set in self.rule_items)
                res = math.prod(mu_items)
            except:
                raise Exception("Cannot access to some element, check for missing keys")
        else:
            intersection = FSet(mu={})
            for _elem, f_set in self.rule_items:
                intersection = intersection.intersection(f_set)

            res = min(list(intersection.mu(elem) for elem, f_set in self.rule_items))

        return res
