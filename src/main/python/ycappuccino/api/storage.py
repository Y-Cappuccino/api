import dataclasses
from abc import ABC
import typing as t
from ycappuccino.api.core import YCappuccinoComponent
from ycappuccino.api.services import IService, Request


class Query:
    @staticmethod
    def from_parser(params: str) -> "Query": ...


class IStorage(YCappuccinoComponent, ABC):

    def upsert(self, type_id: str, key: str, value: t.Any) -> None: ...
    def get(self, type_id: str, key: str) -> t.Any: ...

    def delete(self, type_id: str, key: str) -> None: ...

    def exists(self, type_id: str, key: str) -> bool: ...


class IFilter(YCappuccinoComponent, ABC):
    """ """

    def get_filter(self, a_tenant: t.Optional[str] = None) -> t.Dict[str, t.Any]: ...


class ITrigger(YCappuccinoComponent, ABC):
    """ """

    def execute(self, a_action: str, a_model: t.Any) -> None: ...

    def is_synchronous(self) -> bool: ...

    def get_item(self) -> str: ...

    def get_actions(self) -> t.List[str]: ...

    def get_name(self) -> str: ...

    def is_post(self) -> bool: ...
    def is_pre(self) -> bool: ...


class ReadOneRequest(Request):
    item_id: str
    key: str
    tenant: t.List[str]


class ReadManyRequest(Request):
    item_id: str
    filter: t.Dict[str, t.Any]
    tenant: t.List[str]


class CreateRequest(Request):
    item_id: str
    data: t.Any


class DeleteManyRequest(Request):
    item_id: str
    filter: t.Dict[str, t.Any]


class DeleteOneRequest(Request):
    item_id: str
    key: str


class IManager(IService, ABC):
    def get(self, type_id: str, key: str) -> t.Any: ...

    def set(self, type_id: str, key: str, value: t.Any) -> None: ...

    def delete(self, type_id: str, key: str) -> None: ...

    def exists(self, type_id: str, key: str) -> bool: ...

    def keys(self, type_id: str) -> t.List[str]: ...

    def values(self, type_id: str) -> t.List[t.Any]: ...

    def aggregate(self, type_id: str, key: str, query: Query) -> None: ...

    def items(self, type_id: str) -> t.List[t.Tuple[str, t.Any]]: ...
