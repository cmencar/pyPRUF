# Pruf Pandas - Fuzzy Extension of the Pandas Library

This project extends the capabilities of the **pandas** library to support fuzzy set operations. The objective is to provide tools for representing and working with:

- Fuzzy Sets
- Fuzzy Series *(planned)*
- Fuzzy Relations *(planned)*

Currently, only fuzzy sets are implemented. Future iterations will introduce additional features and support for fuzzy series and relations.

---

## `FSet` Fuzzy Set Representation

The core class used to represent fuzzy sets is called `FSet`. It is a subclass of `pandas.Series`, adapted to behave according to fuzzy set theory.

By leveraging the structure of `Series`, `FSet` stores each fuzzy set element and its corresponding membership degree.

In a standard `Series`, data is stored as `(index, value)` pairs. In our case:

- **Index**: the element of the set
- **Value**: the degree of membership μ(x), where μ: X → [0, 1]

---

## `FSet` Defining a Fuzzy Set

To define a fuzzy set, we use a membership function:

$$ \mu : X \rightarrow [0, 1]$$


This is stored as a collection of pairs:
$$(x, \mu(x))$$

In `FSet`, this corresponds to storing `x` as the index and `μ(x)` as the associated value.

---

## `FSet` Constraint

To ensure consistency with fuzzy set theory, the following constraints are enforced:

- **Unique indexes**: Each element in the index list in the fuzzy set must be unique.
- **Valid values**: All values must be floating-point numbers in the interval [0, 1].

These constraints ensure that the fuzzy set behaves as expected mathematically.

---

## `FSet` Default value

For elements not explicitly defined in the fuzzy set, a **default membership value** can be specified. This allows the fuzzy set to implicitly define membership degrees for elements outside the current index.

--- 

## `FSet` Example: Concept of 'hot'

For example, suppose we want to define a fuzzy set that represents the concept of something being hot. In this case, we can define
a fuzzy set that assigns a degree of "hotness" to different words using out FSet class:
```python
temperature_f_set = FSet({
    "medium": 0.5,
    "warm": 0.8,
    "hot": 0.9,
    "boiling": 1
})
```
By defining the elements and their membership degrees, we create a fuzzy set.
Elements that are not explicitly defined will have a membership degree of 0 (the default value).

```textwrap
medium     0.5
warm       0.8
hot        0.9
boiling    1.0
Name: mu, dtype: float64
Default value: 0
```

# Overview

This section provides an overview of the main features of `FSet` class.

## Creating a Fuzzy Set

The `FSet` class allows users to create fuzzy sets in multiple ways, let's take a look of them.

### List

You can create a fuzzy set by providing two separate lists:

- One for the **elements** (used as indices)
- One for the corresponding **membership degrees**

Both standard Python lists and NumPy arrays are supported.

Each element in the fuzzy set is defined as follows:

- The index of the element is taken from the *n*-th position of the `elements` list.
- The membership degree is taken from the *n*-th position of the `mu` (membership) list.


```python
f_set = FSet(mu=[0.2, 0.1], index=[10, 20])
```

### Dict
You can create a fuzzy set by providing a dictionary. 

In this case there is no need to specify the indexes as they're represented by the keys in the dictionary.

Each element in the fuzzy set is defined as follows:
- The index of the element is taken from the *n*-th key of the dictionary.
+ the membership degree equals to the value associated to the *n*-th key in the dictionary

```python
f_set = FSet(
    mu={
        10: 0.2,
        11: 0.5,
        12: 0.1
    }
)
```

### Bool

You can create a fuzzy set by providing a boolean value and an optional list of indexes.

You can set all elements every element specify in the index to 0 or 1 by using passing a bool value.
+ If the user pass True every element will have a membership degree of 1
+ If the user pass False every element will have a membership degree of 0
This also effects the default value.

```python
f_set_a = FSet(mu=True, index=[10, 20])
f_set_b = FSet(mu=False)
```

### Function

You can generate the elements of a fuzzy set by providing a function that accepts a single parameter representing the index of each element.

To define the fuzzy set in this way, you must also provide a list of indexes over which the function will be applied.

For each element in the fuzzy set:

- The index is taken from the *n*-th value of the provided index list.
- The membership degree is computed as `f(x)`, where `x` is the corresponding index.

This approach is useful when the membership degrees follow a mathematical or logical pattern.

```python
f_set_a = FSet(mu= lambda x: trapf(x, 1, 4, 5, 8), index=[1, 2.5, 4.5])
f_set_b = FSet(mu= lambda x: trimf(x, 1, 4, 5), index=[1, 5, 4, 10])
f_set_c = FSet(mu= lambda x: gauss(x, 1, 2), index=[1, 5, 2, 10])
f_set_d = FSet(mu= lambda x: bell(x, 1, 4), index=[1, 5, 2, 10])
```

In the library there are already some function to generate fuzzy sets such has:

| Function | Description                    |  
|----------|--------------------------------|
| `trapf`  | Generates a trapezoidal fuzzy set |
| `trimf`  | Generates a triangular fuzzy set  |
| `gauss`  | Generates a Gaussian fuzzy set    |
| `bell`   | Generates a bell-shaped fuzzy set |    

### Series

You can generate the elements of a fuzzy set by providing a `Series` object.

In order to do so you must ensure that the indexes are uniques and that all the values are between [0, 1].

```python
series = pd.Series([0.2, 0.3], index=[10, 20])
f_set_b = FSet(mu=series)
```

## Operators

This section provides an overview of the main operators of `FSet` class.

### Union

The union of a fuzzy set A and B is the fuzzy set $A \cup B$:
$$ x \in A \cup B = s\_norm(\mu_A(x), \mu_B(x)) $$

Given two FSet we can use the union operator to generate a new FSet that is the union of the previous ones:

```python
f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.5)
f_set_b = FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 2]), default_value=0.2)

union = f_set_a.union(f_set_b)
```

The user can specify an s_norm to use in function itself, the s_norm must be a binary function that accepts one float and returns a float between [0, 1]. 
By default, the method will use the s_norm stored in the configurations.

### Intersection
The intersection of a fuzzy set A and B is the fuzzy set $A \cup B$:
$$ x \in A \cup B = t\_norm(\mu_A(x), \mu_B(x)) $$

Given two FSet we can use the intersection operator to generate a new FSet that is the intersection of the previous ones:

```python
f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.5)
f_set_b = FSet(mu=np.array([0.5, 0.2]), index=np.array([1, 2]), default_value=0.2)

intersection = f_set_a.intersection(f_set_b)
```

The user can specify a t_norm to use in function itself, the t_norm must be a binary function that accepts one float and returns a float between [0, 1].
By default, the method will use the t_norm stored in the configurations.

### Complement
The complement of a fuzzy set is the fuzzy set $ \neg A$:
$$ \neg A \in x  = complement(\mu_A(x)) $$

Given a FSet we can use the complement operator to generate a new FSet that is its complement:

```python
f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)

complement = f_set_a.complement()
```

The user can specify a complement to use in function itself, the complement must be a unary function that accepts one float and returns a float between [0, 1].
By default, the method will use the t_norm stored in the configurations.

### mu
The mu operator allows the user to pick the membership degree of an element in the fuzzy set. If the membership degree is not
specified the default value will be picked.

```python
f_set_a = FSet(mu=np.array([0.8, 1, 1]), index=np.array([1, 2, 3]), default_value=0.2)

f_set_a.mu(1)
```

### is_included

The fuzzy set A is included in a fuzzy set B if:
$$ \forall x  \ \ \ \mu_A(x) \le\mu_B(x)$$

The operator ``is_included`` checks if a FSet is included in another one.

```python
f_set_a = FSet(mu=np.array([0.1, 0.1, 0.1]), index=np.array([1, 2, 3]), default_value=0.1)
f_set_b = FSet(mu=np.array([0.2, 0.2, 0.3]), index=np.array([1, 2, 3]), default_value=0.2)

f_set_a.is_included(f_set_b)
```


