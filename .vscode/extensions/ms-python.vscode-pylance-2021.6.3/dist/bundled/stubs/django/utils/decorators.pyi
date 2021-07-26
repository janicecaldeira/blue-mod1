from typing import Any, Callable, Iterable, Optional, Type, Union, TypeVar

from django.utils.deprecation import MiddlewareMixin
from django.views.generic.base import View

from django.utils.functional import classproperty as classproperty

_T = TypeVar("_T", bound=Union[View, Callable])  # Any callable
_CallableType = TypeVar("_CallableType", bound=Callable)

class classonlymethod(classmethod): ...

def method_decorator(decorator: Union[Callable, Iterable[Callable]], name: str = ...) -> Callable[[_T], _T]: ...
def decorator_from_middleware_with_args(middleware_class: type) -> Callable: ...
def decorator_from_middleware(middleware_class: type) -> Callable: ...
def make_middleware_decorator(middleware_class: Type[MiddlewareMixin]) -> Callable: ...
def sync_and_async_middleware(func: _CallableType) -> _CallableType: ...
def sync_only_middleware(func: _CallableType) -> _CallableType: ...
def async_only_middleware(func: _CallableType) -> _CallableType: ...
