import abc
import typing as t
import os
import uuid


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

    @staticmethod
    def get_hash() -> str:
        return str(__file__ + "-" + str(uuid.uuid4()))

    @abc.abstractmethod
    async def start(self):
        """start statement for this component"""
        ...

    @abc.abstractmethod
    async def stop(self):
        """stop statement for this component"""

        ...


class YCappuccinoComponentBind(YCappuccinoComponent):

    def __init__(self):
        self._bind_field = []

    @abc.abstractmethod
    async def bind(self, a_service: t.Any):
        """bind statement for this component"""
        ...

    @abc.abstractmethod
    async def un_bind(self, a_service: t.Any):
        """unbind statement for this component"""
        ...


class DefaultMixin:
    spec_filter: t.Union[str, YCappuccinoComponent] = "main"


class _YCappuccinoType:
    def __init__(self, value):
        self.value = value


def YCappuccinoType(base_type: type, spec_filter: t.Any = None) -> type:
    class YCappuccinoTypeDefault(_YCappuccinoType, base_type, DefaultMixin):
        @classmethod
        def set_default(cls, value1: type, value2: str):
            cls.type = value1
            cls.spec_filter = value2

    YCappuccinoTypeDefault.set_default(base_type, spec_filter)

    return YCappuccinoTypeDefault


import dataclasses
from types import ModuleType
import typing as t


@dataclasses.dataclass
class ComponentDiscovered:

    module: ModuleType
    module_name: str
    path: t.Optional[str] = None


@dataclasses.dataclass
class GeneratedComponent:
    module_name: str
    instance_name: str
    instance_name_obj: str
    content: str


class IYCappuccinoComponentLoader:
    def generate(self, component_discovered: ComponentDiscovered) -> ModuleType: ...
    def load(self, component_discovered: ComponentDiscovered) -> ModuleType: ...
    def loads(self) -> ModuleType: ...


class IComponentDiscovery:

    def discover(self, path: str) -> None: ...


class IInspectModule:

    def get_ycappuccino_component(self, module: ModuleType) -> list[type]: ...

    def is_ycappuccino_component(
        self, a_klass: type, include_pelix: bool = False
    ) -> bool: ...
