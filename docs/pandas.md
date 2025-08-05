# Fuzzy extension of Pandas Library

Using the tools offered by pandas library we created a new library that manages fuzzy sets with old operators.

In particular the goal of this library is to create a representation of
+ Fuzzy sets
+ Fuzzy series
+ Fuzzy relation

Currently, only fuzzy sets are implemented but in the future iterations there will be more features.

---

# FSet

The class used to represents fuzzy set is called FSet, it's an extension to the Pandas' Series class.
Using Series's data representation we created a container that will keep track of a fuzzy set's elements and their
membership degree.

Pandas' Series we can store elements by using an index and a value.
Users can store multiple data with the same value and can store different kind of values.

In the FSet class we limited the Series operators to replicate the behavior and the operators of fuzzy set.

## Store fuzzy set using FSet

To represent a fuzzy set we must create a function $\mu$:
$$\mu : X \rightarrow [0, 1] $$
To do that, we store the function using the Series representation by having:
$$(x, \mu(x))$$
as the element of our set. To do that we will store elements in the index and after that connect
every ef them to a membership degree.

To do that we impose some limitation on the indexes and the values:
+ In an FSet the indexes are unique. This ensures the existence of unique elements inside the fuzzy set.
+ Only float number between [0, 1] will be accepted as values

To map other elements outside the current scope we can set a default value for every other element not 
currently defined in the fuzzy set.

--- 
For example, we want to store a fuzzy set that represent the concept of a hot thing:
```python
temperature_f_set = FSet({
    "medium": 0.5,
    "warm": 0.8,
    "hot": 0.9,
    "boiling": 1
})
```

By defining the elements and their membership degrees we created a fuzzy set; the elements that are not defined will 
have the membership degree of 0.
```textwrap
medium     0.5
warm       0.8
hot        0.9
boiling    1.0
Name: mu, dtype: float64
Default value: 0
```

# Overview

Let's take a look at the main features of the library.

## Creation of fuzzy set

With FSet the user can create a fuzzy set using different ways:
### List
You can specify the indexes and the membership degree by using two separate lists. You can use normal python array or
numpy arrays.

The n-th element of the fuzzy set will have:
+ the index equals to the n-th element of the indexes list
+ the membership degree equals to the n-th element of the mu list

```python
f_set = FSet(mu=[0.2, 0.1], index=[10, 20])
```

### Dict
You can specify the indexes and the membership degree by using a single dictionary. In this case there is no need to specify 
the indexes list in fact the keys of the dict will be used as indexes.

The n-th element of the fuzzy set will have:
+ the index equals to the n-th key of the dictionary
+ the membership degree equals to the value associated to the n-th key

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

You can set all elements every element specify in the index to 0 or 1 by using passing a bool value.
+ If the user pass True every element will have a membership degree of 1
+ If the user pass False every element will have a membership degree of 0

```python
f_set_a = FSet(mu=True, index=[10, 20])
f_set_b = FSet(mu=False)
```

### Function

You can set generate the elements of the fuzzy set by using a function that accept a single parameter that represent the index of the element.
To define the elements the user must use an index list.

The n-th element of the fuzzy set will have:
+ the index equals to the n-th value of the index list of the dictionary
+ the membership degree equals to f(x) where x is the n-th element

```python
f_set_a = FSet(mu= lambda x: trapf(x, 1, 4, 5, 8), index=[1, 2.5, 4.5])
f_set_b = FSet(mu= lambda x: trimf(x, 1, 4, 5), index=[1, 5, 4, 10])
f_set_c = FSet(mu= lambda x: gauss(x, 1, 2), index=[1, 5, 2, 10])
f_set_d = FSet(mu= lambda x: bell(x, 1, 4), index=[1, 5, 2, 10])
```

In the library there are already some function to generate fuzzy sets such has:
+ ``trapf``- creates a trapezoidal fuzzy set
+ ``trimf``- creates a triangular fuzzy set
+ ``gauss``- creates a gaussian fuzzy set
+ ``bell``- creates a bell shaped fuzzy set

### Series
The user can create a fuzzy set by using a pre-created Series to create a fuzzy set. To do that we must ensure that the indexes are uniques
and that the values are between [0, 1].

```python
series = pd.Series([0.2, 0.3], index=[10, 20])
f_set_b = FSet(mu=series)
```

## Operators

Let's see the operators that can be done on fuzzy sets.

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

