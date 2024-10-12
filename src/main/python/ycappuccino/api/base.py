from abc import ABC

from ycappuccino.api.core import YCappuccinoComponent


class IListComponent(YCappuccinoComponent, ABC):
    pass


class IActivityLogger(YCappuccinoComponent, ABC):
    pass


class IConfiguration(YCappuccinoComponent, ABC):
    pass
