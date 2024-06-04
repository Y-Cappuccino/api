import abc
from typing import Optional


class IRunner:

    def start(self) -> None: ...

    def stop(self) -> None: ...


class IFramework:

    def start(self, yml_path: str) -> None: ...

    def stop(self) -> None: ...


class YCappuccino(abc.ABC):

    @abc.abstractmethod
    def start(self) -> None: ...

    @abc.abstractmethod
    def stop(self) -> None: ...


class YCappuccinoComponent(abc.ABC):

    @abc.abstractmethod
    async def start(self):
        """start statement for this component"""
        ...

    @abc.abstractmethod
    async def stop(self):
        """stop statement for this component"""

        ...
