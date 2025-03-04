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
