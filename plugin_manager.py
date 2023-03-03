from typing import Any, Type
from resources import Resource

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, plugin_class):
        resource_type = plugin_class.supported_resource_type()
        if resource_type not in self.plugins:
            self.plugins[resource_type] = []
        self.plugins[resource_type].append(plugin_class())

    def invoke_plugins_for_resource(self, resource):
        resource_type = type(resource)
        if resource_type in self.plugins:
            for plugin in self.plugins[resource_type]:
                if plugin.should_run(resource):
                    plugin.run(resource)


class Plugin:
    def __init__(self):
        pass

    def should_run(self, resource):
        raise NotImplementedError

    def run(self, resource):
        raise NotImplementedError

    def get_index_fields(self):
        return {}

    @staticmethod
    def supported_resource_type() -> Type[Resource]:
        raise NotImplementedError

    def get_index_value(self, resource):
        index_fields = self.get_index_fields()
        index_values = [str(getattr(resource, field)) for field in index_fields.keys()]
        return '-'.join(index_values)