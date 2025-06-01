import json
from pathlib import Path
from .data import load_json_file, get_cache_path
from .scanner import PedalboardScanner



class PedalboardPluginary:
    def __init__(self):
        self.plugins_path = get_cache_path("plugins")
        self.load_data()

    def load_data(self):
        if not self.plugins_path.exists():
            scanner = PedalboardScanner(autosave=True)
            scanner.scan()
        self.plugins = load_json_file(self.plugins_path)

    def as_list(self):
        return list(self.plugins.values())

    def as_json(self):
        return json.dumps(self.plugins, indent=4)


class PedalboardPlugins:
    def __init__(self):
        self.load_data()

    def load_data(self):
        scanner = PedalboardScanner(autosave=False, nologging=True)
        scanner.scan()
        self.plugins = scanner.get_plugins()

    def as_list(self):
        return list(self.plugins.values())

    def as_json(self):
        return json.dumps(self.plugins, indent=4)