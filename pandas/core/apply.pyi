import abc
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.base import Index as Index
from pandas.core.series import Series as Series
#from pandas.core.construction import create_series_with_explicit_dtype as create_series_with_explicit_dtype
#from pandas.core.dtypes.common import is_dict_like as is_dict_like, is_extension_array_dtype as is_extension_array_dtype, is_list_like as is_list_like, is_sequence as is_sequence
#from pandas.core.dtypes.generic import ABCSeries as ABCSeries
#from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Any, Dict, Iterator, Tuple, Union

ResType = Dict[int, Any]

def frame_apply(obj: DataFrame, func: Any, axis: Any=..., raw: bool=..., result_type: Any=..., ignore_failures: bool=..., args: Any=..., kwds: Any=...) -> Any: ...

class FrameApply(metaclass=abc.ABCMeta):
    axis: int
    @property
    @abc.abstractmethod
    def result_index(self) -> Index: ...
    @property
    @abc.abstractmethod
    def result_columns(self) -> Index: ...
    @property
    @abc.abstractmethod
    def series_generator(self) -> Iterator[Series]: ...
    @abc.abstractmethod
    def wrap_results_for_axis(self, results: ResType, res_index: Index) -> Union[Series, DataFrame]: ...
    obj: Any = ...
    raw: Any = ...
    ignore_failures: Any = ...
    args: Any = ...
    kwds: Any = ...
    result_type: Any = ...
    f: Any = ...
    def __init__(self, obj: DataFrame, func: Any, raw: bool, result_type: Any, ignore_failures: bool, args: Any, kwds: Any): ...
    @property
    def res_columns(self) -> Index: ...
    @property
    def columns(self) -> Index: ...
    @property
    def index(self) -> Index: ...
    def values(self): ...
    def dtypes(self) -> Series: ...
    @property
    def agg_axis(self) -> Index: ...
    def get_result(self): ...
    def apply_empty_result(self): ...
    def apply_raw(self): ...
    def apply_broadcast(self, target: DataFrame) -> DataFrame: ...
    def apply_standard(self): ...
    def apply_series_generator(self) -> Tuple[ResType, Index]: ...
    def wrap_results(self, results: ResType, res_index: Index) -> Union[Series, DataFrame]: ...

class FrameRowApply(FrameApply):
    axis: int = ...
    def apply_broadcast(self, target: DataFrame) -> DataFrame: ...
    @property
    def series_generator(self): ...
    @property
    def result_index(self) -> Index: ...
    @property
    def result_columns(self) -> Index: ...
    def wrap_results_for_axis(self, results: ResType, res_index: Index) -> DataFrame: ...

class FrameColumnApply(FrameApply):
    axis: int = ...
    def apply_broadcast(self, target: DataFrame) -> DataFrame: ...
    @property
    def series_generator(self): ...
    @property
    def result_index(self) -> Index: ...
    @property
    def result_columns(self) -> Index: ...
    def wrap_results_for_axis(self, results: ResType, res_index: Index) -> Union[Series, DataFrame]: ...
    def infer_to_same_shape(self, results: ResType, res_index: Index) -> DataFrame: ...