from __future__ import annotations

import builtins
import datetime
from numbers import Number
from typing import Callable, Literal, Sequence, Hashable, Mapping, Any

import numpy as np
import pandas as pd
from pandas import Series, Index, DataFrame
from pandas._libs import lib
from pandas._libs.tslibs import BaseOffset
from pandas._typing import IgnoreRaise, Self, DtypeBackend, Frequency, Axis, AnyArrayLike, AggFuncType, IndexLabel, \
    IntervalClosedType, TimedeltaConvertibleTypes, T, CorrelationMethod, QuantileInterpolation, NDFrameT, \
    AlignJoin, Level, FillnaOptions, Scalar, DropKeep, Suffixes, \
    TimestampConvertibleTypes, TimeAmbiguous, TimeNonexistent, SortKind, NaPosition, IndexKeyFunc, ValueKeyFunc, AxisInt
from pandas.core.generic import bool_t
from pandas.core.groupby import SeriesGroupBy
from pandas.core.indexers.objects import BaseIndexer
from pandas.core.resample import Resampler
from pandas.core.window import Rolling, Window, Expanding, ExponentialMovingWindow

from pyPRUF.config import fuzzy_sets_parameters
from pyPRUF.utils import is_list_not_unique, is_out_of_range, is_list_out_of_range


class FSet(Series):
    """
    Class that implements a Fuzzy Set using a Pandas Series and its operators.
    """
    @property
    def dt(self):
        raise AttributeError("The '.dt' accessor is not allowed in FSet.")

    @property
    def str(self):
        raise AttributeError("The '.str' accessor is not allowed in FSet.")

    @property
    def cat(self):
        raise AttributeError("The '.cat' accessor is not allowed in FSet.")

    @property
    def sparse(self):
        raise AttributeError("The '.cat' accessor is not allowed in FSet.")

    @property
    def sparse(self):
        raise AttributeError("The '.cat' accessor is not allowed in FSet.")

    @property
    def iloc(self):
        return FuzzyIndexer(super().iloc, self)

    @property
    def loc(self):
        return FuzzyIndexer(super().loc, self)

    @property
    def at(self):
        return FuzzyIndexer(super().at, self)

    @property
    def iat(self):
        return FuzzyIndexer(super().iat, self)

    def __init__(
            self,
            mu: None | list | np.ndarray | dict | Series | Callable[[float], float] | bool = None,
            index: None | list | Index | np.ndarray = None,
            default_value: float = 0,
    ):
        """
        Constructor of the class, it implements different ways to create a FSet depending on the parameters types:
        - list: there must be a list of index and a list of values, the length of index list must be ge than the value list
        - np.ndarray: same as list
        - dict: create a fuzzy set where the keys are the index of the value
        - Series: copy values of a series to create a fuzzy set
        - Callable: given a series on index create a fuzzy set where the element x ha mu equals to f(x)
        - bool: given a set of values set them all to zero or one in the fuzzy set

        For every other element in fuzzy set the mb is defined by a default value

        Parameters
        ----------
        mu: list | np.ndarray | dict | Series | Callable[[float], float] | bool
            Used to specify the values of the elements of the fuzzy set.
            If the type is dict or Series it contains also the indexes of the values
        index: None | list | Index | np.ndarray
            Used to specify the indexes of the element of the fuzzy set.
            If mu is a dict or a Series this parameter must be empty
        default_value: float
            Default membership for the value that are not in the index

        Raises
        ------
        ValueError:
            - If default_value is outside [0, 1] range
            - If index is None and mu is not dict, Series or bool
            - If mu is not in the accepted types
            - If the indexes in mu Series are not unique
            - If the index list/np.array contains duplicated elements
            - If the membership values are outside the [0, 1] range
        """

        if not (0 <= default_value <= 1):
            raise ValueError("default_value must be between  0 and 1")

        if index is None and (not isinstance(mu, (dict, Series, bool))):
            raise ValueError("index must be one of these type: Index, list, np.ndarray")

        if not isinstance(mu, (dict, list, np.ndarray, Series, bool)) and (not callable(mu)):
            raise ValueError("mu must be one of these type: dict, list, np array or callable")

        index_list = index
        if isinstance(mu, dict):
            index_list = mu.keys()
        elif isinstance(mu, Series):
            if is_list_not_unique(mu.index.array):
                raise Exception("Index must contain unique values")
            index_list = mu.index.array
        elif isinstance(mu, bool) and index is None:
            index_list = []
        elif isinstance(index, (list, np.ndarray)) and is_list_not_unique(index):
            raise ValueError("Index must contain unique values")
        elif isinstance(index, Index) and (not index.is_unique):
            raise ValueError("Index must contain unique values")

        data_list = None
        if callable(mu):
            data_list = []
            for el in index_list:
                data_list.append(mu(el))
        elif isinstance(mu, dict):
            data_list = list(mu.values())
        elif isinstance(mu, Series):
            data_list = mu.to_numpy()
        elif isinstance(mu, dict):
            data_list = list(mu.values())
        elif isinstance(mu, (list, np.ndarray)):
            data_list = mu
        elif isinstance(mu, bool):
            data_list = list(int(mu) for _ in index_list)

        if is_list_out_of_range(data_list, 0, 1):
            raise ValueError("All mu values must be between 0 and 1")

        z  = zip(index_list, data_list[:len(index_list)])
        indexes, values = zip(*((x, y) for x, y in z)) if len(index_list) > 0 else [[], []]

        super().__init__(data=values, index=indexes, name="mu")

        if isinstance(mu, bool):
            self.default_value = int(mu)
        else:
            self.default_value = default_value

    def __setitem__(self, key: float, value: float):
        """
        Set the membership value of a single element to a value between [0, 1]

        Parameters
        ----------
        key: float
            Index of the element
        value: float
            New membership value of the element

        Raises
        ------
        ValueError:
            - If value is outside [0, 1] range
        """
        if is_out_of_range(value, 0, 1):
            raise ValueError("Invalid value for an item, the value must be between 0 and 1")

        super().__setitem__(key, value)

    def __repr__(self):
        return f'{super().__repr__()}\nDefault value: {self.default_value}'

    def __getitem__(self, index):
        if self.index.__contains__(index):
            return super().__getitem__(index)
        return self.default_value

    def intersection(
            self,
            f_set = None,
            t_norm: Callable[[float, float], float] | None = None
    ) -> FSet:
        """
        Get the intersection of two fuzzy sets using a t_norm, if the t_norm is not specified the min function will be used.

        Parameters----------

        f_set: FSet
            FSet that will be intersected
        t_norm: Callable[[float, float], float]
            Callable that will be used to create the intersection of the two fuzzy sets

        Returns
        -------
        FSet
            Represent the intersection between the current fuzzy set and f_set

        Raises
        ------
        ValueError:
            - If t_norm is not callable
        """
        if t_norm is None:
            t_norm = fuzzy_sets_parameters.t_norm

        if not callable(t_norm):
            raise ValueError("Invalid t_norm, it's not callable")

        if f_set is None:
            return FSet.copy(self)

        return apply_binary_func(set_a=self, set_b=f_set, func=t_norm)

    def union(
            self,
            f_set: FSet= None,
            s_norm: Callable[[float, float], float] | None = None
    ) -> FSet:
        """
        Get the union of two fuzzy sets using an s_norm, if the s_norm is not specified the max function will be used.

        Parameters----------

        f_set: FSet
            FSet that will be united with the current one
        s_norm: Callable[[float, float], float]
            Callable that will be used to create the union of the two fuzzy sets

        Returns
        -------
        FSet
            FSet that represent the s_norm between the current fuzzy set and f_set

        Raises
        ------
        ValueError:
            - If s_norm is not callable
        """
        if s_norm is None:
            s_norm = fuzzy_sets_parameters.s_norm

        if not callable(s_norm):
            raise Exception("Invalid s_norm, it's not callable")

        if f_set is None:
            return FSet.copy(self)

        return apply_binary_func(set_a=self, set_b=f_set, func=s_norm)

    def complement(
            self,
            complement: Callable[[float], float] | None = None
    ) -> FSet:
        """
        Get the complement of the current fuzzy set using a complement, if the complement is not specified the 1 complement function will be used.

        Parameters
        ----------

        complement: Callable[[float], float]
            Callable that will be used to create the complement of the current fuzzy set

        Returns
        -------
        FSet
            Fuzzy set that represent the complement of the fuzzy set

        Raises
        ------
        ValueError:
            - If complement is not callable
        """
        if complement is None:
            complement = fuzzy_sets_parameters.complement

        if not callable(complement):
            raise ValueError("Invalid complement, it's not callable")

        return FSet(Series(self.to_dict()).apply(lambda x: complement(x)), default_value=complement(self.default_value))

    def is_included(self, f_set: FSet = None) -> bool:
        """
        Check if the current fuzzy set is included in f_set by checking every item's membership value

        Parameters
        ----------

        f_set: FSet
            Fuzzy set that will be compared to the current one

        Returns
        -------
        bool
            True if every x in the fuzzy sets mu(x) <= mu'(x)
            False otherwise
        """
        if f_set is None:
            raise Exception("There must be an f_set")

        df = pd.DataFrame({ "col_1": self, "col_2": f_set }).fillna({ "col_1": self.default_value, "col_2": f_set.default_value })

        return df.apply(lambda x: x["col_1"] <= x["col_2"], axis=1).all() and self.default_value <= f_set.default_value

    def mu(self, index) -> float:
        """
        Get the membership value of the element represented by the index

        Parameters
        ----------
        index
            Value used as index of the element

        Returns
        -------

        float
            Membership value of the element

        Raises
        ------
        ValueError:
            - If index is None
        """
        if index is None:
            raise Exception("There must be an index")
        elif self.index.__contains__(index):
            return self[index]
        else:
            return self.default_value

    def to_numpy(
            self,
            dtype = None,
            copy: bool = True,
            na_value: object = lib.no_default,
            **kwargs,
    ) -> np.ndarray:
        return np.array(self.to_list(), dtype="float", copy=copy)

    def to_list(self):
        return list(zip(self.index, self.values))

    def validate_base_operators(other, level=None, fill_value=None, axis: Axis = 0):
        if axis != 0:
            raise Exception("Cannot apply this operator on 0 axis")

        if not isinstance(other, Number):
            raise Exception("Cannot apply this operator with non scalar value")

    def add(self, other, level=None, fill_value=None, axis: Axis = 0):
        FSet.validate_base_operators(other, level=None, fill_value=None, axis = 0)

        return FSet(Series.add(self, other))

    def sub(self, other, level=None, fill_value=None, axis: Axis = 0):
        FSet.validate_base_operators(other, level=None, fill_value=None, axis = 0)

        return FSet(Series.sub(self, other))

    def mul(self, other, level=None, fill_value=None, axis: Axis = 0):
        FSet.validate_base_operators(other, level=None, fill_value=None, axis = 0)

        return FSet(Series.mul(self, other))

    def div(self, other, level=None, fill_value=None, axis: Axis = 0):
        FSet.validate_base_operators(other, level=None, fill_value=None, axis = 0)

        return FSet(Series.div(self, other))

    def truediv(self, other, level=None, fill_value=None, axis: Axis = 0):
        FSet.validate_base_operators(other, level=None, fill_value=None, axis = 0)

        return FSet(Series.truediv(self, other))

    def floordiv(self, other, level=None, fill_value=None, axis: Axis = 0):
        raise Exception("Cannot apply this operator with non scalar value")

    def pow(self, other, level=None, fill_value=None, axis: Axis = 0):
        FSet.validate_base_operators(other, level=None, fill_value=None, axis = 0)

        return FSet(Series.pow(self, other))

    def apply(
            self,
            func: AggFuncType,
            convert_dtype: bool | lib.NoDefault = lib.no_default,
            args: tuple[Any, ...] = (),
            *,
            by_row: Literal[False, "compat"] = "compat",
            **kwargs,
    ) -> DataFrame | Series:
        return FSet(Series.apply(self, func, convert_dtype, args))

    def astype(
            self, dtype, copy: bool_t | None = None, errors: IgnoreRaise = "raise"
    ) -> Self:
        raise NotImplementedError("You cannot create a FSet with a different type")

    def convert_dtypes(
            self,
            infer_objects: bool_t = True,
            convert_string: bool_t = True,
            convert_integer: bool_t = True,
            convert_boolean: bool_t = True,
            convert_floating: bool_t = True,
            dtype_backend: DtypeBackend = "numpy_nullable",
    ) -> Self:
        raise NotImplementedError("You cannot convert the types of a FSet")

    def infer_objects(self, copy: bool_t | None = None) -> Self:
        raise NotImplementedError("You cannot apply inference on an FSet")

    def to_timestamp(
            self,
            freq: Frequency | None = None,
            how: Literal["s", "e", "start", "end"] = "start",
            copy: bool | None = None,
    ) -> Series:
        raise NotImplementedError("You cannot convert the type of a FSet")

    def to_period(self, freq: builtins.str | None = None, copy: bool | None = None) -> Series:
        raise NotImplementedError("You cannot convert the type of a FSet")

    def prod(
            self,
            axis: Axis | None = None,
            skipna: bool = True,
            numeric_only: bool = False,
            min_count: int = 0,
            **kwargs,
    ):
        raise NotImplementedError("Cannot apply this operator")

    def dot(self, other: AnyArrayLike) -> Series | np.ndarray:
        raise NotImplementedError("Cannot apply this operator")

    def aggregate(self, func=None, axis: Axis = 0, *args, **kwargs):
        raise NotImplementedError("Cannot apply this operator")

    def transform(
            self, func: AggFuncType, axis: Axis = 0, *args, **kwargs
    ) -> DataFrame | Series:
        raise NotImplementedError("Cannot apply this operator")

    def map(
            self,
            arg: Callable | Mapping | Series,
            na_action: Literal["ignore"] | None = None,
    ) -> Series:
        raise NotImplementedError("Cannot apply this operator")

    def groupby(
            self,
            by=None,
            axis: Axis = 0,
            level: IndexLabel | None = None,
            as_index: bool = True,
            sort: bool = True,
            group_keys: bool = True,
            observed: bool | lib.NoDefault = lib.no_default,
            dropna: bool = True,
    ) -> SeriesGroupBy:
        raise NotImplementedError("Cannot apply this operator")

    def rolling(
            self,
            window: int | datetime.timedelta | builtins.str | BaseOffset | BaseIndexer,
            min_periods: int | None = None,
            center: bool_t = False,
            win_type: builtins.str | None = None,
            on: builtins.str | None = None,
            axis: Axis | lib.NoDefault = lib.no_default,
            closed: IntervalClosedType | None = None,
            step: int | None = None,
            method: builtins.str = "single",
    ) -> Window | Rolling:
        raise NotImplementedError("Cannot apply this operator")

    def expanding(
            self,
            min_periods: int = 1,
            axis: Axis | lib.NoDefault = lib.no_default,
            method: Literal["single", "table"] = "single",
    ) -> Expanding:
        raise NotImplementedError("Cannot apply this operator")

    def ewm(
            self,
            com: float | None = None,
            span: float | None = None,
            halflife: float | TimedeltaConvertibleTypes | None = None,
            alpha: float | None = None,
            min_periods: int | None = 0,
            adjust: bool_t = True,
            ignore_na: bool_t = False,
            axis: Axis | lib.NoDefault = lib.no_default,
            times: np.ndarray | DataFrame | Series | None = None,
            method: Literal["single", "table"] = "single",
    ) -> ExponentialMovingWindow:
        raise NotImplementedError("Cannot apply this operator")

    def pipe(
            self,
            func: Callable[..., T] | tuple[Callable[..., T], str],
            *args,
            **kwargs,
    ) -> T:
        raise NotImplementedError("Cannot apply this operator")

    def all(
            self,
            axis: Axis = 0,
            bool_only: bool = False,
            skipna: bool = True,
            **kwargs,
    ) -> bool:
        raise NotImplementedError("Cannot apply this operator")

    def any(  # type: ignore[override]
            self,
            *,
            axis: Axis = 0,
            bool_only: bool = False,
            skipna: bool = True,
            **kwargs,
    ) -> bool:
        raise NotImplementedError("Cannot apply this operator")

    def corr(
            self,
            other: Series,
            method: CorrelationMethod = "pearson",
            min_periods: int | None = None,
    ) -> float:
        raise NotImplementedError("Cannot apply this operator")

    def count(self) -> int:
        raise NotImplementedError("Cannot apply this operator")

    def diff(self, periods: int = 1) -> Series:
        raise NotImplementedError("Cannot apply this operator")

    def factorize(
            self,
            sort: bool = False,
            use_na_sentinel: bool = True,
    ):
        raise NotImplementedError("Cannot apply this operator")

    def kurt(
            self,
            axis: Axis | None = 0,
            skipna: bool = True,
            numeric_only: bool = False,
            **kwargs,
    ):
        raise NotImplementedError("Cannot apply this operator")

    def quantile(
            self,
            q: float | Sequence[float] | AnyArrayLike = 0.5,
            interpolation: QuantileInterpolation = "linear",
    ) -> float | Series:
        raise NotImplementedError("Cannot apply this operator")

    def rank(
            self,
            axis: Axis = 0,
            method: Literal["average", "min", "max", "first", "dense"] = "average",
            numeric_only: bool_t = False,
            na_option: Literal["keep", "top", "bottom"] = "keep",
            ascending: bool_t = True,
            pct: bool_t = False,
    ) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def sem(
            self,
            axis: Axis | None = None,
            skipna: bool = True,
            ddof: int = 1,
            numeric_only: bool = False,
            **kwargs,
    ):
        raise NotImplementedError("Cannot apply this operator")

    def skew(
            self,
            axis: Axis | None = 0,
            skipna: bool = True,
            numeric_only: bool = False,
            **kwargs,
    ):
        raise NotImplementedError("Cannot apply this operator")

    def std(
            self,
            axis: Axis | None = None,
            skipna: bool = True,
            ddof: int = 1,
            numeric_only: bool = False,
            **kwargs,
    ):
        raise NotImplementedError("Cannot apply this operator")

    def align(
            self,
            other: NDFrameT,
            join: AlignJoin = "outer",
            axis: Axis | None = None,
            level: Level | None = None,
            copy: bool_t | None = None,
            fill_value: Hashable | None = None,
            method: FillnaOptions | None | lib.NoDefault = lib.no_default,
            limit: int | None | lib.NoDefault = lib.no_default,
            fill_axis: Axis | lib.NoDefault = lib.no_default,
            broadcast_axis: Axis | None | lib.NoDefault = lib.no_default,
    ) -> tuple[Self, NDFrameT]:
        raise NotImplementedError("Cannot apply this operator")

    def case_when(
            self,
            caselist: list[
                tuple[
                    Callable[[Series], Series | np.ndarray | Sequence[bool]],
                    Scalar | Callable[[Series], Series | np.ndarray],
                ],
            ],
    ) -> Series:
        raise NotImplementedError("Cannot apply this operator")

    def drop(
            self,
            labels: IndexLabel | None = None,
            *,
            axis: Axis = 0,
            index: IndexLabel | None = None,
            columns: IndexLabel | None = None,
            level: Level | None = None,
            inplace: bool = False,
            errors: IgnoreRaise = "raise",
    ) -> Series | None:
        raise NotImplementedError("Cannot apply this operator")

    def droplevel(self, level: IndexLabel, axis: Axis = 0) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def duplicated(self, keep: DropKeep = "first") -> Series:
        raise NotImplementedError("Cannot apply this operator")

    def reindex_like(
            self,
            other,
            method: Literal["backfill", "bfill", "pad", "ffill", "nearest"] | None = None,
            copy: bool_t | None = None,
            limit: int | None = None,
            tolerance=None,
    ) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def reset_index(
            self,
            level: IndexLabel | None = None,
            *,
            drop: bool = False,
            name: Level = lib.no_default,
            inplace: bool = False,
            allow_duplicates: bool = False,
    ) -> DataFrame | Series | None:
        raise NotImplementedError("Cannot apply this operator")

    def add_prefix(self, prefix: str, axis: Axis | None = None) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def add_suffix(self, suffix: str, axis: Axis | None = None) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def swaplevel(
            self, i: Level = -2, j: Level = -1, copy: bool | None = None
    ) -> Series:
        raise NotImplementedError("Cannot apply this operator")

    def reorder_levels(self, order: Sequence[Level]) -> Series:
        raise NotImplementedError("Cannot apply this operator")

    def explode(self, ignore_index: bool = False) -> Series:
        raise NotImplementedError("Cannot apply this operator")

    def repeat(self, repeats: int | Sequence[int], axis: None = None) -> Series:
        raise NotImplementedError("Cannot apply this operator")

    def squeeze(self, axis: Axis | None = None):
        raise NotImplementedError("Cannot apply this operator")

    def compare(
            self,
            other: Series,
            align_axis: Axis = 1,
            keep_shape: bool = False,
            keep_equal: bool = False,
            result_names: Suffixes = ("self", "other"),
    ) -> DataFrame | Series:
        raise NotImplementedError("Cannot apply this operator")

    def update(self, other: Series | Sequence | Mapping) -> None:
        raise NotImplementedError("Cannot apply this operator")

    def asfreq(
            self,
            freq: Frequency,
            method: FillnaOptions | None = None,
            how: Literal["start", "end"] | None = None,
            normalize: bool_t = False,
            fill_value: Hashable | None = None,
    ) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def asof(self, where, subset=None):
        raise NotImplementedError("Cannot apply this operator")

    def shift(
            self,
            periods: int | Sequence[int] = 1,
            freq=None,
            axis: Axis = 0,
            fill_value: Hashable = lib.no_default,
            suffix: builtins.str | None = None,
    ) -> Self | DataFrame:
        raise NotImplementedError("Cannot apply this operator")

    def first_valid_index(self) -> Hashable | None:
        raise NotImplementedError("Cannot apply this operator")

    def last_valid_index(self) -> Hashable | None:
        raise NotImplementedError("Cannot apply this operator")

    def resample(
            self,
            rule,
            axis: Axis | lib.NoDefault = lib.no_default,
            closed: Literal["right", "left"] | None = None,
            label: Literal["right", "left"] | None = None,
            convention: Literal["start", "end", "s", "e"] | lib.NoDefault = lib.no_default,
            kind: Literal["timestamp", "period"] | None | lib.NoDefault = lib.no_default,
            on: Level | None = None,
            level: Level | None = None,
            origin: builtins.str | TimestampConvertibleTypes = "start_day",
            offset: TimedeltaConvertibleTypes | None = None,
            group_keys: bool_t = False,
    ) -> Resampler:
        raise NotImplementedError("Cannot apply this operator")

    def tz_convert(
            self, tz, axis: Axis = 0, level=None, copy: bool_t | None = None
    ) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def tz_localize(
            self,
            tz,
            axis: Axis = 0,
            level=None,
            copy: bool_t | None = None,
            ambiguous: TimeAmbiguous = "raise",
            nonexistent: TimeNonexistent = "raise",
    ) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def at_time(self, time, asof: bool_t = False, axis: Axis | None = None) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def between_time(
            self,
            start_time,
            end_time,
            inclusive: IntervalClosedType = "both",
            axis: Axis | None = None,
    ) -> Self:
        raise NotImplementedError("Cannot apply this operator")

    def where(self, cond, other=None, *args, **kwargs) -> "FSet":
        result = super().where(cond, other=other, *args, **kwargs)
        return FSet(result.dropna())

    def filter(
            self,
            items=None,
            like: builtins.str | None = None,
            regex: builtins.str | None = None,
            axis: Axis | None = None,
    )  -> "FSet":
        result = super().filter(items, like, regex, axis)
        return FSet(result.dropna())

    def argsort(
            self,
            axis: Axis = 0,
            kind: SortKind = "quicksort",
            order: None = None,
            stable: None = None,
    ) -> "FSet":
        return FSet(super().argsort(axis, kind, order, stable))

    def sort_index(
            self,
            *args,
            axis: Axis = 0,
            level: IndexLabel | None = None,
            ascending: bool | Sequence[bool] = True,
            inplace: bool = False,
            kind: SortKind = "quicksort",
            na_position: NaPosition = "last",
            sort_remaining: bool = True,
            ignore_index: bool = False,
            key: IndexKeyFunc | None = None,
    ) -> "FSet" | None:
        res = super().sort_index(
            axis=axis,
            level=level,
            ascending=ascending,
            inplace=inplace,
            kind=kind,
            na_position=na_position,
            sort_remaining=sort_remaining,
            ignore_index=ignore_index,
            key=key,
        )

        if res is None:
            return None

        return FSet(res)

    def sort_values(
            self,
            *,
            axis: Axis = 0,
            ascending: bool | Sequence[bool] = True,
            inplace: bool = False,
            kind: SortKind = "quicksort",
            na_position: NaPosition = "last",
            ignore_index: bool = False,
            key: ValueKeyFunc | None = None,
    ) ->  "FSet" | None:
        res = super().sort_values(
            axis=axis,
            ascending=ascending,
            inplace=inplace,
            kind=kind,
            na_position=na_position,
            ignore_index=ignore_index,
            key=key,
        )

        if res is None:
            return None

        return FSet(res)


class FuzzyIndexer:
    """
    Class used for setter and getter of a fuzzy set
    """
    def __init__(self, base, f_set: FSet):
        self._base = base
        self._series = f_set

    def __getitem__(self, key):
        return self._base[key]

    def __setitem__(self, key, value: Number):
        """
        Set the membership value of an item in a fuzzy set

        Parameter
        ---------
        key
            Index of the element in the fuzzy set
        value: Number
            New value for the element

        Raise
        -----
        TypeError:
            - If value is not numerical
        ValueError:
            - If value is out of [0, 1] range
        TypeError:
            If value is not numeric
        """
        if not isinstance(value, Number):
            raise TypeError("Value must be numerical")

        if is_out_of_range(value, 0, 1):
            raise ValueError("Value must be between 0 and 1")

        self._base[key] = value


def apply_binary_func(
    set_a: FSet = None,
    set_b: FSet = None,
    func: Callable = None
) -> FSet:
    """
    Apply a binary function to the elements of two fuzzy creating a new one based off the result

    Parameters
    ----------

    set_a: FSet
        First FSet
    set_b: FSet
        Second FSet
    func: Callable
        Callable that will produce the result of every couple of set_a and set_b merge

    Returns
    -------
    FSet
        FSet containing the elements of func using the values in set_a and set_b
    """
    df = pd.DataFrame({ "col_1": set_a, "col_2": set_b}).fillna({
        "col_1": set_a.default_value,
        "col_2": set_b.default_value,
    })

    return FSet(df.apply(lambda row: func(row["col_1"], row["col_2"]), axis=1), default_value=func(set_a.default_value, set_b.default_value))
