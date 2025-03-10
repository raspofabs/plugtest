import importlib
import pkgutil

discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg
    in pkgutil.iter_modules()
    if name.startswith('amber_')
}

def main() -> None:
    print("Amber core plugins:")
    for name, plugin in discovered_plugins.items():
        if hasattr(plugin, "plugin_entry_point"):
            response = plugin.plugin_entry_point()
            behaviour = response.get("behaviour", lambda a, b: a - b)
            a = 5
            b = 3
            c = behaviour(a, b)
            print(f"Plugin: {name} -> {c}")
        else:
            print(f"Not a plugin: {name}")

