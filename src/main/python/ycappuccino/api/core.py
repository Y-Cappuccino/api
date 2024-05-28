import abc
from typing import Optional


class IRunner:

    def start(self) -> None: ...

    def stop(self) -> None: ...


class IFramework:

    def start(self) -> None: ...

    def stop(self) -> None: ...


class YCappuccino(abc.ABC):

    @abc.abstractmethod
    def start(self) -> None: ...

    @abc.abstractmethod
    def stop(self) -> None: ...


class ComponentDiscovered:

    def __init__(self, name: str, klass: str, module: str, path: Optional[str] = None):
        self.name = name
        self.klass = klass
        self.module = module
        self.path = path
        self.ipopo_source = ""


class IComponentDiscovery:

    def discover(self) -> list[ComponentDiscovered]:
        pass
