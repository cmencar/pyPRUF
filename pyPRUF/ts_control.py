import math
from typing import Tuple, List, Literal, Callable
from pyPRUF.fset import FSet

class TSControl:
    """
    Takagi-Sugeno Fuzzy Controller.

    A reusable controller based on a set of fuzzy rules.
    """

    def __init__(self, rules: List["Rule"]):
        """
        Initialize the Takagi-Sugeno fuzzy controller.

        Parameters
        ----------
        rules : list of Rule
            A list of `Rule` objects that define the behavior of the controller.
        """
        self.rules = rules

    def calculate(
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

        Returns
        -------
        float
            The output of a TS control based off its input and rules
        """
        firing_strengths = list(rule.firing_strength(control_input, mode) for rule in self.rules)
        weighted_sum = 0

        for index, rule in enumerate(self.rules):
            row_weighted_sum = firing_strengths[index]
            weighted_sum = weighted_sum + (row_weighted_sum * rule.output(control_input))


        return weighted_sum / sum(firing_strengths)

class Rule:
    """
    Rule of a fuzzy controller
    """
    def __init__(
        self,
        rule_items: List[Tuple[str, FSet]] = (),
        rule_output: Callable = None
    ):
        """
        Initiate a single Rule
        Parameters
        ----------
        rule_output : callable
            A callable that will calculate the output of the rule
        rule_items : list of tuples (str, FSet)
            List of tuples that represents the single element of a rule.
            The single rule contains the name of the input (just like a variable) and a Fuzzy set
        """
        self.output = rule_output
        self.rule_items = list(rule_items)

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
        """
        try:
            mu_items = list(f_set.mu(control_input[elem]) for elem, f_set in self.rule_items)
        except:
            raise Exception("Cannot access to some element, check for missing keys")
        else:
            if mode == "prod":
                res = math.prod(mu_items)
            else:
                res = min(mu_items)

            return res if res != 0 else 0.01