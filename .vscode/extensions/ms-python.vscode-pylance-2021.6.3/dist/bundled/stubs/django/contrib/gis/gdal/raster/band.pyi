from django.contrib.gis.gdal.raster.base import GDALRasterBase as GDALRasterBase
from typing import Any, Optional

class GDALBand(GDALRasterBase):
    source: Any = ...
    def __init__(self, source: Any, index: Any) -> None: ...
    @property
    def description(self): ...
    @property
    def width(self): ...
    @property
    def height(self): ...
    @property
    def pixel_count(self): ...
    def statistics(self, refresh: bool = ..., approximate: bool = ...): ...
    @property
    def min(self): ...
    @property
    def max(self): ...
    @property
    def mean(self): ...
    @property
    def std(self): ...
    @property
    def nodata_value(self): ...
    @nodata_value.setter
    def nodata_value(self, value: Any) -> None: ...
    def datatype(self, as_string: bool = ...): ...
    def color_interp(self, as_string: bool = ...): ...
    def data(
        self,
        data: Optional[Any] = ...,
        offset: Optional[Any] = ...,
        size: Optional[Any] = ...,
        shape: Optional[Any] = ...,
        as_memoryview: bool = ...,
    ): ...

class BandList(list):
    source: Any = ...
    def __init__(self, source: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def __getitem__(self, index: Any): ...
