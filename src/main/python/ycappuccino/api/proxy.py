import json


class YCappuccinoRemote(object):
    """interface of YCappuccino component"""

    def __init__(self):
        """abstract constructor"""
        self._specifications: list = []
        self._id: str = ""
        self._component_properties: dict = {}
        self._remote_server_id: str = ""
        self._methods: list = dir(self)

    def get_component_properties_id(self) -> str:
        prop = self._component_properties.copy()
        prop["specifications"] = self._specifications
        prop["remote_server_id"] = self._remote_server_id
        prop["methods"] = self._methods

        return json.dumps(prop)

    def get_specifications(self) -> list:
        return self._specifications

    def set_specifications(self, a_specifications: list) -> None:
        self._specifications = a_specifications

    def set_component_properties(self, a_component_properties: dict) -> None:
        self._component_properties = a_component_properties.copy()
        w_object_class = self._component_properties["objectClass"]
        self._specifications = []
        for w_class in w_object_class:
            self._specifications.append(w_class)

    def set_component_id_remote(self, a_component_id_remote: str) -> None:
        self._remote_server_id = a_component_id_remote

    def id(self) -> str:
        return self._id
