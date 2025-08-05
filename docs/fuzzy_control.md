# Takagi-Sugeno controller

Using FSet class we created a class to easily create basic Takagi-Sugeno controller.

A TS controller use rules of the form:

R: if $x_1$ is $\mu_R^{(1)}$ and ... and $x_n$ is $\mu_R^{(1)}$, then 
y = $f_R(x_1, ..., x_n)$

The single rule determines a function with the input variables as arguments.

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

Rule class represents a single rule of a controller, a single rule has the following shape:

R: if $x_1$ is $\mu_R^{(1)}$ and ... and $x_n$ is $\mu_R^{(1)}$, then
y = $f_R(x_1, ..., x_n)$

With a Rule instance, given an input, we can calculate:
+ the firing strength
+ the rule y output

## Creating a Rule

To create a rule we pass the constructor a list of rule items and an output function. A single rule item is:
$$x_n \in \mu_n$$

To represent the variable we use a string that will identify it, for the fuzzy set we use the FSet class.

The output function is a unary function that will take one dictionary containing the input of the single rule and will return the
output of the Rule.

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

After the creation of a rule we can, given an input, calculate the firing strength of the rule.
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

So for example if we pass:
```text
{ "wl_1": "low", "wl_2": "medium" }
```
The method will calculate:
$$'low'  \in water\_f\_set\_low$$
$$'medium' \in water\_f\_set\_high$$

After the user can choose how to calculate $μ_{R,a_1 ,...,a_n}$, there are currently 2 option:
+  $min \{x_n \in \mu_n\}$
+ $ \prod x_n \in \mu_n$

Using the previous example we have

```python
firing_strength_min = rule.firing_strength({
    "wl_1": "alto",
    "wl_2": "medio"
}, "min")
```

# TS Control

TS Control is a class that use Rule class to create a Takagi-Sugeno controller.
This controller is reusable: after its creation we can use it to calculate its output 
for a specific input.

## Creating a TS Control

The creation of a TS Control instance is pretty straight forward, you must only specify a list of Rule instances.
In fact a Takagi Sugeno controller is the combination of multiple rules.

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

The output is given by the operator calculate. This operator accepts a dictionary that must contain
the keys used in the rules. It also accepts the method to calculate the rule's firing strength, that are:
+ min
+ product

So, using the other example we can calculate the output of a fuzzy controller:
```python
ts_control = TSControl([
    Rule( [ ("wl", water_f_set_low) ], low_level ),
    Rule( [ ("wl", water_f_set_high) ], high_level )
])

result_a = ts_control.calculate({ "wl": "medium" })
```