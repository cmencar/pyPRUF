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

---
# Metodi ereditati da Series

## Metodi di conversione

- [`Series.astype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html#pandas.Series.astype)  
  Cast dei valori ad un tipo specificato.  
  **Non utilizzabile, verrà lancia eccezione**

- [`Series.convert_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes)  
  Converte i valori ad un tipo specificato.  
  **Non utilizzabile, verrà lancia eccezione**

- [`Series.infer_objects`](https://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html#pandas.Series.infer_objects)  
  Inferenza del tipo.  
  **Non utilizzabile, verrà lancia eccezione**

- [`Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy)  
  Ritorna un array numpy.  
  Può essere usato per ottenere un array numpy con coppie del tipo:

  $$
  (x, \mu(x))
  $$

  Il parametro `dtype` viene ignorato.

- [`Series.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html#pandas.Series.to_period)  
  Converte in `PeriodIndex`.  
  **Non utilizzabile, verrà lancia eccezione**

- [`Series.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html#pandas.Series.to_timestamp)  
  Converte in `Timestamp`.  
  **Non utile al caso di studio → lancia eccezione**

- [`Series.to_list`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html#pandas.Series.to_list)  
  Ritorna una lista dalla `Series`.  
  Può essere usato per ottenere una lista con coppie del tipo:

  $$
  (x, \mu(x))
  $$

---

## Accesso ai valori

- [`Series.get`](https://pandas.pydata.org/docs/reference/api/pandas.Series.get.html#pandas.Series.get)  
  Accede al valore di $\mu$ dato l'identificativo di un elemento.

- [`Series.at`](https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html#pandas.Series.at)
- [`Series.iat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html#pandas.Series.iat)
- [`Series.loc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html#pandas.Series.loc)
- [`Series.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas.Series.iloc)

Metodi utilizzabili per accedere alle membership value di un singolo valore.

---

## Iterazione e accesso a chiavi/valori

- [`Series.__iter__`](https://pandas.pydata.org/docs/reference/api/pandas.Series.__iter__.html#pandas.Series.__iter__)
- [`Series.items`](https://pandas.pydata.org/docs/reference/api/pandas.Series.items.html#pandas.Series.items)
- [`Series.keys`](https://pandas.pydata.org/docs/reference/api/pandas.Series.keys.html#pandas.Series.keys)
- [`Series.pop`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pop.html#pandas.Series.pop)
- [`Series.item`](https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html#pandas.Series.item)
- [`Series.xs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.xs.html#pandas.Series.xs)

Metodi utilizzabili per accedere alle membership value dei vari valori.

---

## Operazioni aritmetiche

- [`Series.add`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add.html#pandas.Series.add)
- [`Series.sub`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sub.html#pandas.Series.sub)
- [`Series.mul`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mul.html#pandas.Series.mul)
- [`Series.div`](https://pandas.pydata.org/docs/reference/api/pandas.Series.div.html#pandas.Series.div)
- [`Series.truediv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.truediv.html#pandas.Series.truediv)

Consentite **solo con valori scalari**.  
I valori devono sempre rimanere nel range `[0, 1]`.

- [`Series.floordiv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.floordiv.html#pandas.Series.floordiv)
- [`Series.mod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mod.html#pandas.Series.mod)  
  **Non utilizzabili → lancia eccezione**

- [`Series.pow`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pow.html#pandas.Series.pow)  
  Utile per rafforzare valori nel fuzzy set.  
  Ammessi solo valori scalari.

---

## Confronti logici

- [`Series.lt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.lt.html#pandas.Series.lt)
- [`Series.gt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html#pandas.Series.gt)
- [`Series.le`](https://pandas.pydata.org/docs/reference/api/pandas.Series.le.html#pandas.Series.le)
- [`Series.ge`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ge.html#pandas.Series.ge)
- [`Series.ne`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ne.html#pandas.Series.ne)
- [`Series.eq`](https://pandas.pydata.org/docs/reference/api/pandas.Series.eq.html#pandas.Series.eq)

Utilizzati per ottenere una `Series` booleana.

---

## Altri metodi (selezione)

- [`Series.apply`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply)  
  Permette di applicare una funzione sull FSet, **controllando che i valori restino in [0,1]**.

- [`Series.clip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html#pandas.Series.clip)  
  Utile per forzare i valori entro `[0,1]`.

- [`Series.max`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max)
- [`Series.min`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min)
- [`Series.mean`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean)
- [`Series.median`](https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html#pandas.Series.median)
- [`Series.mode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#pandas.Series.mode)
- [`Series.nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html#pandas.Series.nlargest)
- [`Series.nsmallest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html#pandas.Series.nsmallest)

Statistiche utili per analisi del fuzzy set.

- [`Series.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique)
- [`Series.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nunique.html#pandas.Series.nunique)
- [`Series.is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_unique.html#pandas.Series.is_unique)

Statistiche di supporto.

- [`Series.filter`](https://pandas.pydata.org/docs/reference/api/pandas.Series.filter.html#pandas.Series.filter)
- [`Series.where`](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html#pandas.Series.where)

Consentiti per filtrare elementi del fuzzy set.

---

## Gruppi di metodi invariati

- Plotting
- Serializzazione (lettura/scrittura)

---

## Gruppi di metodi disabilitati
- Gestione dati mancanti (`isna`, `fillna`, ecc.)
- Metodi statistici avanzati (`std`, `var`, `sem`, `skew`, ecc.)
- TimeSeries
- String accessor
- Categorical accessor
- Sparse accessor
- Timedelta
- Datetime
- Alcune funzioni di aggregazione (`agg`, `groupby`, `rolling`, ecc.)
- Operazioni non coerenti con fuzzy set (`dot`, `product`, ecc.)

