from typing import List, Literal
from pyPRUF.fset import FSet
from pyPRUF.ts_rule import TSRule

class TSControl:
    """
    Takagi-Sugeno Fuzzy Controller.

    A reusable controller based on a set of fuzzy rules.
    """

    def __init__(self, rules: List["TSRule"]):
        """
        Initialize the Takagi-Sugeno fuzzy controller.

        Parameters
        ----------
        rules : list of TSRule
            A list of `Rule` objects that define the behavior of the controller.

        Examples
        --------
        >>> from pyPRUF import trap_mf        >>> bg_negative_fs = FSet(
        ...     mu=lambda x: trap_mf(x, -10, -10, -7.5, -5),
        ...    index=np.arange(-10, -4, 0.5)
        >>> )

        >>> sm_negative_fs = FSet(
        ...    mu=lambda x: trap_mf(x, -7.5, -5, -2, 0),
        ...    index=np.arange(-7.5, 0, 0.5)
        >>> )

        >>> from pyPRUF import tri_mf        >>> zero_fs = FSet(
        ...    mu=lambda x: tri_mf(x, -2, 0, 2),
        ...    index=np.arange(-2, 2, 0.5)
        >>> )
        >>>
        >>> ts_control = TSControl([
        ...    TSRule( [ ("e", bg_negative_fs), ("ee", bg_negative_fs) ], rule_1_out ),
        ...    TSRule( [ ("e", sm_negative_fs), ("ee", zero_fs) ], rule_2_out )
        >>> ]
        """
        self.rules = rules

    def __str__(self):
        return "Controller rules:\n" + f"\n".join( f"Rule {i + 1}: {str(rule)}" for i, rule in enumerate(self.rules))

    def inference(
        self,
        control_input: dict = None,
        mode: Literal["prod", "min"] = "prod"
    ):
        """
        Calculate the controller output based on the provided input and fuzzy rules.

        Parameters
        ----------
        control_input : dict, optional
            A dictionary containing input variable names and their corresponding values.
            These values are used to evaluate the fuzzy rules.
        mode : ['prod', 'min'], optional
            The method used to compute the firing strength of each rule:

            - 'prod': the firing strength is the product of the input membership degrees.
            - 'min' : the firing strength is the minimum of the input membership degrees.

            Default is 'prod'.

        Raises
        ------
        Exception:
            - If the sum of firing strenghts is 0

        Returns
        -------
        float
            The output of a TS control based off its input and rules

        Examples
        --------

        >>> ts_control = TSControl([
        ...    TSRule( [ ("e", bg_negative_fs), ("ee", bg_negative_fs) ], rule_1_out ),
        ...    TSRule( [ ("e", sm_negative_fs), ("ee", zero_fs) ], rule_2_out )
        >>> ]

        >>> ts_control.inference({ "e": 0.1, "ee": 0.5 }, mode="min")

        """
        firing_strengths = list(rule.firing_strength(control_input, mode) for rule in self.rules)
        tot_firing_strength = sum(firing_strengths)

        if tot_firing_strength == 0:
            raise Exception("The sum of firing strengths is 0!")

        weighted_sum = 0

        for index, rule in enumerate(self.rules):
            row_weighted_sum = firing_strengths[index]
            weighted_sum = weighted_sum + (row_weighted_sum * rule.output(control_input))

        return weighted_sum / sum(firing_strengths)