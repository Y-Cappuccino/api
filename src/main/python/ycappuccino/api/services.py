import abc
from abc import ABC

from ycappuccino.api.core import YCappuccinoComponent


class Request(ABC): ...


class Response(ABC): ...


class IService(YCappuccinoComponent, ABC):
    @abc.abstractmethod
    async def handle(self, request: Request) -> Response: ...
