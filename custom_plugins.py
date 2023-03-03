from typing import Type
from plugin_manager import Plugin
from resources import HashResource, Resource, ServiceResource


class Port80Plugin(Plugin):
    def should_run(self, resource):
        # We can make assertions about the resource here before we run it.
        ##For example, here we can specify that this  plugin should only run on port 8080 (for whatever reason).
        return isinstance(resource, ServiceResource) and resource.port == 80

    def run(self, resource):
        ##Core logic goes here.
        print("Running Port80Plugin for {}".format(resource))

    def supported_resource_type() -> Type[Resource]:
        #Used to build the PluginManager lookup table. The PluginManager stores plugins in a dict 
        #and plugins are mapped to the ResourceType they want to run.
        #Currently a plugin can only support 1 resource type but we could probably extend that easily.
        return ServiceResource



class Port443Plugin(Plugin):
    def should_run(self, resource):
        return isinstance(resource, ServiceResource) and resource.port == 443

    def run(self, resource):
        print(f"Running Port443Plugin for {resource.ip}")

    def supported_resource_type() -> Type[Resource]:
        return ServiceResource
        
class PasswordHashPlugin(Plugin):

    def should_run(self, resource):
        ##We could potentially make an assertion here - If we know what the hash type is then run (and crack). If not, don't run the plugin.
        return isinstance(resource.hash, str)

    def run(self, resource):
        ##Start cracking.
        print(f"Running PasswordHashPlugin for {resource.hash}")

    def supported_resource_type() -> Type[Resource]:
        #We tell the PluginManager we're interested in PasswordHashResources!
        return HashResource
 

class SoftwareVersionPlugin(Plugin):
    resource_types = [Resource]

    def should_run(self, resource):
        return isinstance(resource.software_version, str)

    def run(self, resource):
        print(f"Running SoftwareVersionPlugin for {resource.software_version}")

    def supported_resource_type() -> Type[Resource]:
        return ServiceResource