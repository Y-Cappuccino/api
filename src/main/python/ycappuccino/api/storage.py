import dataclasses
from abc import ABC, abstractmethod
import typing as t
from ycappuccino.api.core import YCappuccinoComponent
from ycappuccino.api.services import IService, Request


@dataclasses.dataclass
class Query:
    offset: int
    limit: int
    sort: str

    @staticmethod
    def from_parser(params: str) -> "Query": ...


@dataclasses.dataclass
class FilterTenant:

    tenant: t.List[str] = None

    @staticmethod
    def from_parser(params: str) -> "FilterTenant": ...


class IStorage(YCappuccinoComponent, ABC):
    """ """

    @abstractmethod
    async def aggregate(
        self,
        a_collection: str,
        a_filter: FilterTenant,
        a_pipeline: t.List[t.Dict[str, t.Any]],
    ):
        """aggegate data regarding filter and pipeline"""
        ...

    @abstractmethod
    async def get_one(
        self,
        a_collection: str,
        a_id: str,
        a_filter: FilterTenant,
        a_params: Query,
    ):
        """get dict identify by a Id"""
        ...

    @abstractmethod
    async def get_many(
        self, a_collection: str, a_filter: FilterTenant, a_params: Query
    ):
        """return iterable of dict regarding filter"""
        ...

    @abstractmethod
    async def up_sert(
        self,
        a_collection: str,
        a_id: str,
        a_filter: FilterTenant,
        params: Query,
        a_new_dict: t.Dict[str, t.Any],
    ):
        """update or insert new dict"""
        ...

    @abstractmethod
    async def up_sert_many(
        self,
        a_collection: str,
        a_filter: FilterTenant,
        params: Query,
        a_new_dict: t.Dict[str, t.Any],
    ):
        """update or insert document with new dict regarding filter"""
        ...

    @abstractmethod
    async def delete(
        self, a_collection: str, a_id: str, a_filter: FilterTenant, query: Query
    ):
        """delete document identified by id if it exists"""
        ...

    @abstractmethod
    async def delete_many(
        self, a_collection: str, a_filter: FilterTenant, query: Query
    ):
        """ """
        ...


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
