# Amber plugins

A simple example showing how to do a plugin architecture.
All plugings follow a naming convention.
Check that each package has a method to call to export the behaviours you want to use.

## Amber core

Amber core can be run as a script. If it is, then it will search for
packages starting with `amber_`. This is just shamelessly ripped straight from 
https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/

```python
discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg
    in pkgutil.iter_modules()
    if name.startswith('amber_')
}
```

Then, For each package, it checks the module has an _expected function_:

```python
if hasattr(plugin, "plugin_entry_point"):
```

If it does, it can then call it and use it:

```python
response = plugin.plugin_entry_point()
behaviour = response.get("behaviour", lambda a, b: a - b)
```

## Amber add and Amber mult

These are the plug packages.
They provide a service in the form of a function you can call, taking two
numeric values.

```python
def add(a, b):
    return a + b
```

And they publish this feature through the _expected function_:

```python
def plugin_entry_point() -> dict:
    return {"behaviour": add}
```

## How it works in practice

To get this to work, the packages have to be installed while the core is running.
Using `uv run` in `amber_core` won't work, because Amber-core doesn't rely on
`amber_mult` or `amber-add`, so uv won't add them to the `.venv` it creates.
Instead, you need to make sure they are added just in time.
I used `--with` and `uvx` with relative paths to ask it to install the other
packages just in time.
I also added `-n` to force it to rebuild the `.venv` each time while I was
trying this out.

```sh
uvx -n --with ./amber_add --with ./amber_mult ./amber_core
```
