# Takagi-Sugeno controller

Using the FSet class, we developed a tool to simplify the creation of basic Takagi-Sugeno (TS) controllers.

A TS controller uses rules of the form:

R: if $x_1$ is $\mu_R^{(1)}$ and ... and $x_n$ is $\mu_R^{(1)}$, then 
y = $f_R(x_1, ..., x_n)$

Each rule defines a function where the input variables serve as arguments.

The basic idea is that the corresponding function is a good local control function for the fuzzy region that is described
by the antecedent of the rule.

At the boundaries between single fuzzy regions, we have to interpolate
in a suitable way between the corresponding local models. This is done by

$$
    y = \dfrac{\sum_{R}\mu_{R, a_1, ..., a_n} \cdot f_R(x_1, ..., x_n)}
    {\sum_R\mu_{R, a_1, ..., a_n}}
$$

where $a_1, . . . , a_n$ are the measured input values of the input variables $x_1 , . . ., x_n$,
and $μ_{R,a_1 ,...,a_n}$ denotes the firing strength of rule R which results given these input
values.

--- 

We represented the concepts of Rule and Controller by using two classes:
- Rule
- TSControl

# Rule

The Rule class represents a single rule within a controller. Each rule has the following form:

R: if $x_1$ is $\mu_R^{(1)}$ and ... and $x_n$ is $\mu_R^{(1)}$, then
y = $f_R(x_1, ..., x_n)$

Given an instance of `Rule` and an input, we can compute:
+ The firing strength of the rule
+ The output y of the rule’s function

## Creating a Rule

To create a `Rule` we pass the constructor requires:
+ a list of rule items in the form
  $$x_n \in \mu_n$$
  where $x_n$ is a variable and $\mu_n$ is a fuzzy described by a `FSet` instance
+ an output function
 a unary function that that takes a dictionary containing 
 the input values for the variables in the rule and returns the output of the rule.

For example:

```python
water_f_set_low = FSet({
    "very_high": 0,
    "high": 0.2,
    "medium": 0.5,
    "low": 0.8,
    "very_low": 1,
})

water_f_set_high = FSet({
    "very_high": 1,
    "high": 0.8,
    "medium": 0.5,
    "low": 0.2,
    "very_low": 0,
})

rule = Rule( [ ("wl_1", water_f_set_low), ("wl_2", water_f_set_high) ], low_level )
```

## Calculate the firing strength

After the creation of a `Rule` we can, given an input, calculate the firing strength of the rule.
We can do that by using the firing_strength method.
This operator accept a dict that contains the inputs of the rule. 

How does the dictionary connect to the rule?

```python
rule = Rule( [ ("wl_1", water_f_set_low), ("wl_2", water_f_set_high) ], low_level )
```

Given the previous example the rule input must be a dictionary with two keys:
+ "wl_1"
+ "wl_2"

The values of the elements will be used in the rule element to calculate:
$$x_n \in \mu_n$$

So for example if we provide:
```text
{ "wl_1": "low", "wl_2": "medium" }
```
The method will calculate:
$$'low'  \in water\_f\_set\_low$$
$$'medium' \in water\_f\_set\_high$$

The user can also choose how to calculate $μ_{R,a_1 ,...,a_n}$, there are currently 2 option:
+  $min \{x_n \in \mu_n\}$
+ $ \prod x_n \in \mu_n$

In the example we will have:

```python
firing_strength_min = rule.firing_strength({
    "wl_1": "alto",
    "wl_2": "medio"
}, "min")
```

# TS Control

The `TSControl` class leverages the `Rule` class to implement a Takagi-Sugeno (TS) controller.

Once created, the controller is reusable: it can be used multiple times to compute the output for different input values. 
Given a specific input, the controller evaluates all the rules and returns the aggregated output.

## Creating a TS Control

Creating a `TSControl` instance is straightforward: you simply provide a list of `Rule` instances.

This reflects the nature of a Takagi-Sugeno controller, which is fundamentally a combination of multiple rules.

```python
ts_control = TSControl([
    Rule( [ ("wl", water_f_set_low) ], low_level ),
    Rule( [ ("wl", water_f_set_high) ], high_level )
])
```

## Calculate the output of a controller

As we said before the output of a TS controller is defined by:

$$
y = \dfrac{\sum_{R}\mu_{R, a_1, ..., a_n} \cdot f_R(x_1, ..., x_n)}
{\sum_R\mu_{R, a_1, ..., a_n}}
$$

The output is given by the operator `calculate`. This operator accepts a dictionary that must contain
the keys used in the rules. It also accepts the method to calculate the rule's firing strength, there are 2 methods:
+ min
+ product

So, in the other example we can calculate the output of a fuzzy controller:
```python
ts_control = TSControl([
    Rule( [ ("wl", water_f_set_low) ], low_level ),
    Rule( [ ("wl", water_f_set_high) ], high_level )
])

result_a = ts_control.calculate({ "wl": "medium" })
```