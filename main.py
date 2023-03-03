from custom_plugins import PasswordHashPlugin, Port443Plugin, Port80Plugin
from plugin_manager import PluginManager
from resources import HashResource, ServiceResource


if __name__ == "__main__":
    # Create a plugin manager
    plugin_manager = PluginManager()

    # Register plugins
    plugin_manager.register_plugin(Port80Plugin)
    plugin_manager.register_plugin(Port443Plugin)
    plugin_manager.register_plugin(PasswordHashPlugin)

    #Start the scanner. Presumably start with an nmap scan, resources start coming in
    resources = [
        ServiceResource("192.168.0.1", 80, "http"),
        ServiceResource("192.168.0.2", 80, "https"),
        HashResource("9fabbecc76796ac9cb4413f5b9a074c8 ", "0"),
        #SoftwareVersionResource("Apache", "2.4.18")
        #UserCredentialsResource("bob", "BadPassword1"")
    ]
    #Combining two resources into one should presumably be easy if all resources follow a similar convention for keys. For example,
    #Suppose you had UsernameResource() and PasswordResource() these may be combined into CredentialResource(). Since they're just dictionaries
    #under the surface. Care would need to be taken to ensure that the resources defined are suitable - you don't want too few resource types or too many.
    
    # Scan each resource with the appropriate plugins
    for resource in resources:
        #print("- {}\n".format(resource))
        plugin_manager.invoke_plugins_for_resource(resource)

    #Future considerations.
    #   - Plugin should probably feed results into storage somehow.
    #   - Plugin should be able to raise new resources to be scanned.
    #   - Would be good if we could support a scheduler on the plugin_manager that's injected into each plugin so that we can register (on_run, or __init__) that we want a specific function to be called every X minutes. This would let Plugins kick off an out of band task (e.g, PasswordCraking) and then periodically poll for the results.
    #   - Currently we don't have a way of gracefully handling errors. It'd be nice if PluginManager could capture this information rather than each individual plugin.